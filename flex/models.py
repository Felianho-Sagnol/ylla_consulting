from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (FieldPanel, PageChooserPanel,
                                StreamFieldPanel, InlinePanel,
                                MultiFieldPanel, FieldRowPanel,
								)
from wagtail.core.fields import StreamField
from wagtail.core import blocks as streamfield_blocks
from wagtail.images.edit_handlers import ImageChooserPanel


from core import blocks
# Create your models here.


class About(Page):
    template = "flex/about.html"
    max_count = 1
    subpage_types = []
    parent_page_types = ["home.Home"]
    banner_image = models.ForeignKey("wagtailimages.Image",
    	blank = False,
    	null= True,
    	related_name="+",
    	on_delete = models.SET_NULL,)

    image_gauche = models.ForeignKey("wagtailimages.Image",
		blank = False,
		null= True,
		related_name="+",
		on_delete = models.SET_NULL,

		)

    title_text = models.CharField(		max_length=1000,
		blank = False,
		null = False,
		help_text="Le texte qui s'affiche sur la l'image",
		)

    sub_title = models.CharField(max_length=1000,
		blank = False,
		null = False,
		help_text="Titre du texte",)
    contenu = StreamField(
			[

				("title_and_text", blocks.TitleAndTextBlock()),
				("full_richtext", blocks.RichTextBlock()),
				("simple_richtext", blocks.SimpleRichtextBlock()),

				("cards", blocks.CardBlock()),
				("cta", blocks.CTABlock()),
				("button", blocks.ButtonBlock()),

			],
			null = True,
			blank = True
		)

    class Meta:
        verbose_name = "Page À propos"


    content_panels = Page.content_panels + [
        FieldRowPanel([
        FieldPanel("title_text", classname="col6"),
        FieldPanel("sub_title", classname="col6"),
        ], heading="Titres",
        ),
		FieldRowPanel([
			ImageChooserPanel("banner_image", classname="col6"),
			ImageChooserPanel("image_gauche", classname="col6"),
			]),

	StreamFieldPanel("contenu")
	]
