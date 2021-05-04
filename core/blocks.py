"""Streamfeld live in here
Cette page est consacrée aux champs streams
"""

from wagtail.core import blocks 
from wagtail.images.blocks import ImageChooserBlock 


class TitleAndTextBlock(blocks.StructBlock):
	""" Title and text and nothing else,"""

	title = blocks.CharBlock(required=True, help_text="Ajouter un titre")
	text = blocks.TextBlock(required=True, help_text="Ajouter un text supplémentaire")


	class Meta:
		verbose_name = "Un titre et un sous-titre"
		template = "core/title_and_text_block.html"
		icon = "edit"
		label = "Title & Text"





class CardBlock(blocks.StructBlock):
	"""Cards with image and text en button(s)
	-- Une sorte de liste

	"""

	title = blocks.CharBlock(required=True, help_text="Add your title")
	cards = blocks.ListBlock(
		blocks.StructBlock(
			[
				("image", ImageChooserBlock(required=True)),
				("title", blocks.CharBlock(required=True, max_length=77)),
				("text", blocks.TextBlock(required=True, max_length=400)),
				("button_page", blocks.PageChooserBlock(required=False)),
				("button_url", blocks.URLBlock(required=False, help_text="Si le bouton de page précédent et selectioné, cela sera utilisé en premier")),

			]
			)

		)


	class Meta:
		template = "core/card_block.html"
		icon = "placeholder"
		label = "Staff Cards"



class RichTextBlock(blocks.RichTextBlock):
	""" Richtext with all the features
	Pour les champs de text enrichi c'est-à-dire on peut formater
	les textes, mettres les images les vidéos, les liens et tout ce qu'on veux


	"""



	class Meta:
		template = "core/richtext_block.html"
		icon = "doc-full"
		label = "Text pleinement enrichi"





class SimpleRichtextBlock(blocks.RichTextBlock):
	""" A filter feater richtext option
	Ici on limite les option de formatage de texte à une selection qu'on
	veut implementer
	"""

	def __init__(self, required=True, help_text=None, editor="default", features=None, **kwargs):
		super().__init__(**kwargs)
		self.features = [
			"bold",
			"italic",
			"link",
		]




	class Meta:
		template = "core/richtext_block.html"#Ici on utilise les mêmes template que l'option complète parce qu'en réalité rien ne change
		icon  = "edit"
		label = "Text simplement enrichi"



class CTABlock(blocks.StructBlock):
	""" A simple call to action section"""

	title = blocks.CharBlock(required=True, max_length=77)
	text = blocks.RichTextBlock(required=True, features=["bold", "italic", "link"] )
	button_page =  blocks.PageChooserBlock(required=False)
	button_url = blocks.URLBlock(required=False)
	button_text = blocks.CharBlock(required=True, default="Learn More...", max_length=33)

	class Meta:
		template = "core/cta_block.html"
		icon = "placeholder"
		label = "Call to Action"



class LinkStructValue(blocks.StructValue):
	"""Additional logic for our URLs"""

	def url(self):
		button_page = self.get("button_page")
		button_url = self.get("button_url")

		if button_page:
			return button_page
		elif button_url:
			return button_url

		return None




class ButtonBlock(blocks.StructBlock):
	"""Une URL interne ou externe """

	button_page = blocks.PageChooserBlock(required=False, help_text="If selected, this url will be used first")
	button_url  = blocks.URLBlock(required=False, help_text="If added, this url will be used secondarily to the button page")


	class Meta:
		template = "core/buton_block.html"
		icon = "placeholder"
		label = "Simple bouton"
		value_class = LinkStructValue
