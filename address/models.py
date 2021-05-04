from django.db import models


from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.


@register_setting(icon="group")
class SocialMediaSettings(BaseSetting):
	"""
	Model pour enregistrer les réseau sociaux
	"""

	facebook 		= models.URLField(blank=True, null=True, help_text="Lien de la page Facebook")
	instagram     	= models.URLField(blank=True, null=True, help_text="Lien de page Instagram")
	twitter 		= models.URLField(blank=True, null=True, help_text="Lien de la page Twitter")
	youtube 		= models.URLField(blank=True, null=True, help_text="Lien de la page YuTube")
	pinterest 		= models.URLField(blank=True, null=True, help_text="Lien de la page Pinterest")
	linkedin		= models.URLField(blank=True, null=True, help_text="Lien de la page LinkedIn")
	tiktok			= models.URLField(blank=True, null=True, help_text="Lien de la page TikTok")




	panels = [

		MultiFieldPanel([
			FieldPanel("facebook"),
			FieldPanel("instagram"),
			FieldPanel("twitter"),
			FieldPanel("youtube"),
			FieldPanel("pinterest"),
			FieldPanel("linkedin"),
			FieldPanel("tiktok"),

			], heading="Règlage des réseaux sociaux"),
	]



	class Meta:
		verbose_name = "Résaux sociaux"

	def get_admin_display_title(self):
		return "Réseaux sociaux"


@register_setting(icon="mail")
class AddressSettings(BaseSetting):
	"""
	Model pour le règlage des adresses
	"""
	telephone = models.CharField("N° Tel", blank=True, null=True, max_length=20, help_text="Votre numéro de téléphone")
	fax = models.CharField("FAX", blank=True, null=True, max_length=20, help_text="Nº FAX")
	email 	  = models.EmailField("Email", blank=True, null=True, help_text="Votre adresse email")
	address  = models.CharField("Adresse", max_length=100, blank=True, null=True, help_text="Votre adresse")
	open_hours  = models.CharField("Heures d'ouverture", max_length=100, blank=True, null=True, help_text="Heures d'ouverture")


	panels = [
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel("telephone", classname="col6"),
				FieldPanel("fax", classname="col6"),
						]),
			FieldPanel("email"),
			FieldPanel("address"),
			FieldPanel("open_hours"),
			], heading="Règlage des adresses"),

	]



	class Meta:
		verbose_name = "Adresses"


	def get_admin_display_title(self):
		return "Adresses"
