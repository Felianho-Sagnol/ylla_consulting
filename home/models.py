from django.db import models
from django import forms
from django.shortcuts import render
from django.db.models.signals import pre_save


from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (
                                FieldPanel, PageChooserPanel,
                                StreamFieldPanel, InlinePanel,
                                MultiFieldPanel,
                                ObjectList, TabbedInterface,
                                FieldRowPanel,
                                )
from wagtail.core.fields import RichTextField,  StreamField
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks as streamfield_blocks

from wagtail.contrib.routable_page.models import RoutablePageMixin, route


#Local import
from core import blocks
from utils.generator_utils import unique_slug_generator




# Create your models here.




class Home(RoutablePageMixin, Page):
    template = "home.html"
    subpage_types = ["flex.About"]
    max_count = 1
    parent_page_types = ["wagtailcore.Page"]
    class Meta:
        verbose_name = "Accueil"
        verbose_name ="Accueil"


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        carousels = Carousel.objects.filter(affiche=True)
        context["carousels"] = carousels
        return context


Home._meta.get_field("title").verbose_name ="Titre"



class Carousel(models.Model):

	image 		    = models.ForeignKey("wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name="+")
	title 		    = models.CharField("Titre", max_length=200, blank=True, null=True, help_text="Ajouter un titre")
	sub_title 	    = models.CharField("Sous titre", max_length=250, blank=True, null=True, help_text="Ajouter un sous-titre")
	link_text       = models.CharField("Texte du lien", max_length=200, blank=True, null=True, help_text="Ajouter le texte du lien")
	affiche         = models.BooleanField(default=True)




	class Meta:
		verbose_name = "Carousel"
		verbose_name_plural = "Carousels"


	def __str__(self):
		return "Carousel {title}".format(title=self.title)




	panels = [
	ImageChooserPanel("image"),
	FieldRowPanel([
		FieldPanel("title", classname="col6"),
		FieldPanel("sub_title", classname="col6"),

        FieldPanel("link_text", classname="col6"),
		]),

		FieldPanel("affiche", widget=forms.CheckboxInput),

	]
