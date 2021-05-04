from wagtail.contrib.modeladmin.options import  (
	ModelAdmin, ModelAdminGroup,
	modeladmin_register
	)

from .models import Carousel

# Register your models here.



class CarouselAdmin(ModelAdmin):
	model = Carousel
	menu_label = "Carousels"
	menu_icon = "chain-broken"
	menu_order = 000

	add_to_settings_menu = False
	exclude_from_explorer = False


	list_display = ("title", )
	search_fields = ("title", "sub_title",)





class AnimationGroup(ModelAdminGroup):
	menu_label = "Animation"
	menu_icon = "folder-open-inverse"
	menu_order=100
	items = (CarouselAdmin,)


modeladmin_register(AnimationGroup)
