from django.contrib import admin


from wagtail.contrib.modeladmin.options import  (
	ModelAdmin, ModelAdminGroup,
	modeladmin_register
	)
from wagtail.admin.edit_handlers import (
                                FieldPanel,
                                MultiFieldPanel, FieldRowPanel,
                                ObjectList, TabbedInterface,
                                InlinePanel, StreamFieldPanel,
                                )

from .models import Contact
# Register your models here.




class ContactAdmin(ModelAdmin):
    model = Contact
    readonly_fields =  ( "timestamp", "updated",)
    menu_label ="Contacts"
    menu_icon ="plus-inverse"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("nom", "prenom", "email", "timestamp")
    search_fields = ["nom", "prenom", "sujet", "email"]


    panels = [
			FieldRowPanel([
				FieldPanel("nom", classname="col6"),
				FieldPanel("prenom", classname="col6"),
				]),


			FieldRowPanel([
				FieldPanel("email", classname="col6"),
				FieldPanel("type_contact", classname="col6"),
						]),


			FieldRowPanel([
				FieldPanel("sujet", classname="col5"),
				FieldPanel("message", classname="col7"),
						]),
    ]


class ContactAdminGroup(ModelAdminGroup):
    menu_label = "Contacts"
    menu_icon ="plus-inverse"
    items = (ContactAdmin,)


modeladmin_register(ContactAdminGroup,)
