import requests
from django.conf import settings

from allauth.socialaccount.providers.oauth2.views import OAuth2View, OAuth2Adapter
from allauth.socialaccount.providers.base import AuthError

from .provider import iHelaProvider


class iHelaAdapter(OAuth2Adapter):
    provider_id = iHelaProvider.id

    # Fetched programmatically, must be reachable from container
    access_token_url = "{}/oAuth2/token/".format(settings.OAUTH_IHELA_SERVER_BASEURL)
    profile_url = "{}/api/v1/connected-user/".format(settings.OAUTH_IHELA_SERVER_BASEURL)

    # Accessed by the user browser, must be reachable by the host
    authorize_url = "{}/oAuth2/authorize/".format(settings.OAUTH_IHELA_SERVER_BASEURL)

    # NOTE: trailing slashes in URLs are important, don't miss it

    def complete_login(self, request, app, token, **kwargs):
        headers = {"Authorization": "Bearer {0}".format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        # extra_data = {}
        return self.get_provider().sociallogin_from_response(request, extra_data)


class BaseOAuth2iHelaView(OAuth2View):
    def perform_request(self, request, app, access_token, **kwargs):
        """
        Returns a HttpRedirectResponse instance
        """
        raise NotImplementedError

    def dispatch(self, request, *args, **kwargs):
        if "error" in request.GET or "code" not in request.GET:
            # Distinguish cancel from error
            auth_error = request.GET.get("error", None)
            if auth_error == self.adapter.login_cancelled_error:
                error = AuthError.CANCELLED
            else:
                error = AuthError.UNKNOWN
            return render_authentication_error(request, self.adapter.provider_id, error=error)
        app = self.adapter.get_provider().get_app(self.request)
        client = self.get_client(request, app)
        try:
            access_token = client.get_access_token(request.GET["code"])
            token = self.adapter.parse_token(access_token)
            token.app = app
            return self.perform_request(request, app, token, response=access_token)
            # login.token = token
            # if self.adapter.supports_state:
            #     login.state = SocialLogin.verify_and_unstash_state(request, get_request_param(request, "state"))
            # else:
            #     login.state = SocialLogin.unstash_state(request)
            # return complete_social_login(request, login)
        except (PermissionDenied, OAuth2Error, RequestException, ProviderException) as e:
            return render_authentication_error(request, self.adapter.provider_id, exception=e)
