import requests
from django.conf import settings

from allauth.socialaccount.providers.oauth2.views import OAuth2View, OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView

from .provider import iHelaProvider
from .base import iHelaAdapter, BaseOAuth2IHelaView


class GetClientMixin(BaseOAuth2IHelaView):
    def get_account():
        pass

    def perform_request(self, request, app, access_token, **kwargs):
        pass


oauth2_login = OAuth2LoginView.adapter_view(iHelaAdapter)
oauth2_callback = OAuth2CallbackView.adapter_view(iHelaAdapter)
