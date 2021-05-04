from django.urls import re_path, path

from .views import (

			about,
			GenerateLesCodePdf
			)








app_name = "flex"





urlpatterns = [

		path("about", about, name="about"),



		]
