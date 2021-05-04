from django.urls import path, re_path


from .views import (
		contact, emplacement,

			)

app_name = "contacts"





urlpatterns = [

	     path("contact/", contact, name="contact"),
	     path("emplacement/", emplacement, name="emplacement"),






]
