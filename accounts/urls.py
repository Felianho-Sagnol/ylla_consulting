from django.urls import path, re_path
from django.contrib.auth.views import LogoutView


from .views import (
		# login_page,
		# register_page,

		account_home_view,
		# View based Class
		LoginView,

		AccountHomeView,

		AccountEmailActivateView,

		UserDetailUpdateView,

		register,

			)

app_name = "accounts"





urlpatterns = [

	     path("login/", LoginView.as_view(), name="login"),
	     path("register/", register, name="register"),

		 path("logout/", LogoutView.as_view(), name="logout"),

	     path("", account_home_view, name="home"),

	     re_path(r'^email/confirme/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name="email_activate"),

	     path("email/resend-activation", AccountEmailActivateView.as_view(), name="resend_activation"),
	     path("update", UserDetailUpdateView.as_view(), name="user_update"),





]
