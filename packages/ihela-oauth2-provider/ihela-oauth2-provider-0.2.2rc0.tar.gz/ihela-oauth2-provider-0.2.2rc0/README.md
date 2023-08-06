iHela Provider
==============

iHela Provider is a simple Django app to enable oAuth2 authentication with django-allauth.

Quick start
-----------
1. Install [django-allauth](https://github.com/pennersr/django-allauth)
    `pip install django-allauth` and following the [install guide](https://django-allauth.readthedocs.io/en/latest/installation.html)
2. Add "ihelaprovider" to your INSTALLED_APPS setting like this:

    ```python
    INSTALLED_APPS = [
        ...
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
        "ihelaprovider",
    ]
    ```

3. Include the polls URLconf in your project urls.py like this::

    ```python
    path("oAuth2/", include("ihelaprovider.urls")),
    ```

4. Add `OAUTH_IHELA_SERVER_BASEURL` setting to `settings.py`  and fill it with ihela server url. Please visit iHela documentation sites for more. 

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to add the iHela provider with the application credentials given (you'll need the Admin app enabled).

Visit [iHela](https://ihela.online) and [django-allauth](https://github.com/pennersr/django-allauth).
