from django.contrib import admin
from main.models import HomePage, Slide, TableCell
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from main.models import Portfolio, PortfolioItem, PortfolioItemImage, PortfolioItemCategory
#from main.models import Order
#from cartridge.shop.forms import ProductAdminForm

class SlideAdmin(TabularDynamicInlineAdmin):
	model=Slide


class HomePageAdmin(PageAdmin):
	inlines = [SlideAdmin,]


class PortfolioItemImageInline(TabularDynamicInlineAdmin):
	model=PortfolioItemImage

class PortfolioItemAdmin(PageAdmin):
	inlines=(PortfolioItemImageInline, )

#admin.site.register(Order,PageAdmin)
admin.site.register(HomePage,HomePageAdmin)
admin.site.register(TableCell,PageAdmin)
admin.site.register(Portfolio,PageAdmin)
admin.site.register(PortfolioItem,PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)

from django.contrib import admin
from mezzanine.conf import settings
 
if "mezzanine.pages" in settings.INSTALLED_APPS:
    from mezzanine.pages.models import RichTextPage, Link
    from mezzanine.pages.admin import PageAdmin, LinkAdmin
    from models import TransRichTextPage, TransLinkPage
 
    #
    # Richtext
    #
    class TransInline(TabularDynamicInlineAdmin):
        model  = TransRichTextPage
        fields = ("lang", "title", "content")
 
    class TransPageAdmin(PageAdmin):
        inlines   = (TransInline,)
 
    admin.site.unregister(RichTextPage)
    admin.site.register(RichTextPage, TransPageAdmin)
 
    #
    # Link
    #
    class TransLinkInline(TabularDynamicInlineAdmin):
        model = TransLinkPage
        fields = ("lang", "title", "slug")
 
    class TransLinkAdmin(LinkAdmin):
        inlines  = (TransLinkInline,)
 
    admin.site.unregister(Link)
    admin.site.register(Link, TransLinkAdmin)
 
if "mezzanine.forms" in settings.INSTALLED_APPS:
    from mezzanine.forms.models import Form, Field
    from mezzanine.forms.admin import FormAdmin, FieldAdmin
    from models import TransField, TransForm
 
    #
    # Form
    #
    class TransFormInline(TabularDynamicInlineAdmin):
        model = TransForm
        fields = ("lang", "title", "content", "button_text", "response")
 
    class TransFormAdmin(FormAdmin):
        inlines = (FieldAdmin, TransFormInline)
 
    admin.site.unregister(Form)
    admin.site.register(Form, TransFormAdmin)
 
    class TransFieldInline(TabularDynamicInlineAdmin):
        model = TransField
        fields = ("lang", "original", "label", "choices", "default", "help_text")
 
    class TransFieldAdmin(admin.ModelAdmin):
        inlines = (TransFieldInline, )
        fields = ("label", "choices", "default", "help_text")
    admin.site.register(Field, TransFieldAdmin)
 
#
# Gallery
#
if "mezzanine.galleries" in settings.INSTALLED_APPS:
    from mezzanine.galleries.models import Gallery, GalleryImage
    from mezzanine.galleries.admin import GalleryAdmin, GalleryImageInline
    from models import TransGallery, TransGalleryImage
 
    class TransGalleryInline(TabularDynamicInlineAdmin):
        model  = TransGallery
        fields = ("lang", "title", "content", )
 
    class TransGalleryAdmin(GalleryAdmin):
        inlines = (GalleryImageInline, TransGalleryInline, )
 
    admin.site.unregister(Gallery)
    admin.site.register(Gallery, TransGalleryAdmin)