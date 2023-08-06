
iHela Provider
==============

iHela Provider is a simple Django app to enable oAuth2 authentication with django-allauth.

Quick start
-----------


#. Install `django-allauth <https://github.com/pennersr/django-allauth>`_
    ``pip install django-allauth`` and following the `install guide <https://django-allauth.readthedocs.io/en/latest/installation.html>`_
#. 
   Add "ihelaprovider" to your INSTALLED_APPS setting like this:

   .. code-block:: python

       INSTALLED_APPS = [
           ...
           "allauth",
           "allauth.account",
           "allauth.socialaccount",
           "ihelaprovider",
       ]

#. 
   Include the polls URLconf in your project urls.py like this:

   .. code-block:: python

       path("oAuth2/", include("ihelaprovider.urls")),

#. 
   Run ``python manage.py migrate`` to create the polls models.

#. 
   Start the development server and visit http://127.0.0.1:8000/admin/
   to the iHela provider with the application credentials given (you'll need the Admin app enabled).

Visit `iHela <https://ihela.online>`_ and `django-allauth <https://github.com/pennersr/django-allauth>`_.
