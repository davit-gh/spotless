from mezzanine.pages.page_processors import processor_for
from .models import HomePage, Slide
from .models import Portfolio, PortfolioItem, PortfolioItemCategory
from django.http import HttpResponseRedirect
from datetimewidget.widgets import DateTimeWidget

@processor_for(Portfolio)
def portfolio_processor(request, page):
    '''
    Adds a portfolio's portfolio items to the context
    '''
    # get the Portfolio's items, prefetching categories for performance
    items = PortfolioItem.objects.published(
        for_user=request.user).prefetch_related('categories')
    items = items.filter(parent=page)
    # filter out only cateogries that are user in the Portfolio's items
    categories = PortfolioItemCategory.objects.filter(
        portfolioitems__in=items).distinct()
    return {'items': items, 'categories': categories}


@processor_for(PortfolioItem)
def portfolioitem_processor(request, page):
    '''
    Adds a portfolio's portfolio items to the context
    '''
    portfolioitem = PortfolioItem.objects.published(
        for_user=request.user).prefetch_related(
        'categories', 'images').get(id=page.portfolioitem.id)
    return {'portfolioitem': portfolioitem}
import pdb
@processor_for(HomePage)
def home_processor(request, page):
    items = PortfolioItem.objects.published(
        for_user=request.user).prefetch_related('categories')
    items = items.filter(parent=page.homepage.featured_portfolio)
    #pdb.set_trace()
    
    return {'items': items}

from main.models import TableCell
from mezzanine.pages.models import Link
@processor_for('table')
def table_processor(request, page):
    tablecells = TableCell.objects.filter(parent=page)
    links = Link.objects.filter(parent=page)
    #pdb.set_trace()
    return {'tablecells': tablecells, 'links': links}

from django import forms
ACCEPTABLE_FORMATS = ['%Y-%m-%d %H:%M:%S']
class OrderForm(forms.Form):
    field_5 = forms.CharField()
#    date_time = forms.DateField(input_formats=ACCEPTABLE_FORMATS, widget=DateTimeWidget(usel10n=True,bootstrap_version=3))

@processor_for("orderform")
def order_form_processor(request,page):
    if request.method == 'POST':
        new = request.POST.copy()
        new.__setitem__('field_8',request.POST['field_8'])
        request.POST=new
        #pdb.set_trace()
    
@processor_for("faq")
def faq_processor(request,page):
    links = Link.objects.filter(parent=page)
    #pdb.set_trace()
    return {'links': links}