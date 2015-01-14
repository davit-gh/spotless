from django.db import models
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged

from mezzanine.utils.models import upload_to
from mezzanine.core.models import RichText, Orderable
from mezzanine.pages.models import Page
from django.utils.translation import ugettext_lazy as _

class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''

    content_heading = models.CharField(max_length=200,
        default="About us!")
    featured_portfolio = models.ForeignKey("Portfolio", blank=True, null=True,
        help_text="If selected items from this portfolio will be featured "
                  "on the home page.")

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image_back = FileField(verbose_name=_("Image back"),
        upload_to=upload_to("main.static.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)

    image_front = FileField(verbose_name=_("Image front"),
        upload_to=upload_to("main.static.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)
    text = models.CharField(verbose_name=_("Slide text"), max_length=400, blank=True)
    class Meta:
        verbose_name = _("Slide")
        verbose_name_plural = _("Slides")

COLUMN_CHOICES = (
    ('6', 'Two columns'), # 2 columns use span6
    ('4', 'Three columns'), # 3 columns use span4
    ('3', 'Four columns'), # 4 columns use span3
)

class Portfolio(Page):
    '''
    A collection of individual portfolio items
    ''' 
    content = RichTextField(blank = True)
    columns = models.CharField(max_length=1,choices=COLUMN_CHOICES,default='3')
    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")

class PortfolioItem(Page, RichText):
    
    featured_image = FileField(verbose_name=_("Featured Image"), upload_to=
            upload_to("main.PortfolioItem.featured_image", "portfolio"),\
            format="Image", max_length=255, null=True, blank=True)

    short_description = RichTextField(blank=True)
    categories = models.ManyToManyField("PortfolioItemCategory", 
            verbose_name=_("Categories"),\
            blank=True, related_name="portfolioitems")
    href = models.CharField(max_length=2000, blank=True,\
            help_text = "A link to the finished project (optional)")
    class Meta:
        verbose_name = _("Portfolio item")
        verbose_name_plural = _("Portfolio items")


class PortfolioItemImage(Orderable):
    portfolioitem = models.ForeignKey(PortfolioItem, related_name="images")
    file = FileField(_("File"), max_length=200, format="Image",\
        upload_to=upload_to("main.PortfolioItemImage.file", "portfolio items"))
    class Meta:
        verbose_name="Portfolio Item Image"
        verbose_name_plural="Portfolio Item Images"

class PortfolioItemCategory(Slugged):
    """
    A category for grouping portfolio items into a series.
    """
    
    class Meta:
        verbose_name=_("Portfolio Item Category")
        verbose_name_plural=_("Portfolio Item Categories")
        ordering=("title",)


class TableCell(Page):
    row1 = models.CharField(max_length=100, blank=True)
    row2 = models.CharField(max_length=100, blank=True)
    row3 = models.CharField(max_length=100, blank=True)
    row4 = models.CharField(max_length=100, blank=True)
    row5 = models.CharField(max_length=100, blank=True)
    row6 = models.CharField(max_length=100, blank=True)
    row7 = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name=_("Tablecell")
        verbose_name_plural=_("Tablecells")


class Order(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=60)
    type_of_service = models.CharField(max_length=150)
    date_time = models.DateField(max_length=50)
    frequency_of_service = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=50)

from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import settings
from mezzanine.core.models import Slugged, MetaData, Displayable, Orderable, RichText
from mezzanine.core.fields import RichTextField
 
class Translatable(models.Model):
    lang = models.CharField(max_length=5, choices=settings.LANGUAGES)
 
    class Meta:
        abstract = True
        ordering = ("lang",)
 
if "mezzanine.pages" in settings.INSTALLED_APPS:
    from mezzanine.pages.models import RichTextPage, Link
 
    class TransRichTextPage(Translatable, RichText, Slugged):
        translation = models.ForeignKey(RichTextPage, related_name="translation")
 
        class Meta:
            verbose_name = _("Translated Page")
            verbose_name_plural = _("Translated Pages")
            ordering = ("lang",)
            unique_together = ("lang", "translation")
 
    class TransLinkPage(Translatable, Slugged):
        translation = models.ForeignKey(Link, related_name="translation")
 
        class Meta:
            verbose_name = _("Translated Link")
            verbose_name_plural = _("Translated Links")
            ordering = ("lang",)
            unique_together = ("lang", "translation")
 
if "mezzanine.forms" in settings.INSTALLED_APPS:
    from mezzanine.forms import fields
    from mezzanine.forms.models import Form, FieldManager, Field
 
    class TransForm(Translatable, RichText, Slugged):
        translation = models.ForeignKey(Form, related_name="translation")
 
        button_text = models.CharField(_("Button text"), max_length=50, default=_("Submit"))
        response = RichTextField(_("Response"))
 
        class Meta:
            verbose_name = _("Translated Form")
            verbose_name_plural = _("Translated Forms")
            ordering = ("lang",)
            unique_together = ("lang", "translation")
 
    class TransField(Translatable):
        translation = models.ForeignKey(Field, related_name="translation")
        original    = models.CharField(_("Label (Original)"), max_length=settings.FORMS_LABEL_MAX_LENGTH)
        label       = models.CharField(_("Label"), max_length=settings.FORMS_LABEL_MAX_LENGTH)
 
        choices     = models.CharField(_("Choices"), max_length=1000, blank=True,
                                       help_text=_("Comma separated options where applicable. "
                                                   "If an option itself contains commas, surround the option with `backticks`."))
        default     = models.CharField(_("Default value"), blank=True,
                                       max_length=settings.FORMS_FIELD_MAX_LENGTH)
        help_text   = models.CharField(_("Help text"), blank=True, max_length=100)
 
        class Meta:
            verbose_name = _("Translated Field")
            verbose_name_plural = _("Translated Fields")
            ordering = ("lang",)
 
if "mezzanine.galleries" in settings.INSTALLED_APPS:
    from mezzanine.galleries.models import Gallery, GalleryImage
 
    class TransGallery(Translatable, Slugged, RichText):
        translation = models.ForeignKey(Gallery, related_name="translation")
 
        class Meta:
            verbose_name = _("Translated Gallery")
            verbose_name_plural = _("Translated Galleries")
            ordering = ("lang",)
 
    class TransGalleryImage(Translatable, Slugged):
        translation = models.ForeignKey(GalleryImage, related_name="translation")
        description = models.CharField(max_length=1000, blank=True)
 
        class Meta:
            verbose_name = _("Translated Image")
            verbose_name_plural = _("Translated Images")
            ordering = ("lang",)