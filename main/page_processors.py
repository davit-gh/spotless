from mezzanine.pages.page_processors import processor_for
from .models import HomePage, Slide
from .models import Portfolio, PortfolioItem, PortfolioItemCategory
from django.http import HttpResponseRedirect
from datetimewidget.widgets import DateTimeWidget
from django.conf import settings
from main.forms import PayPalPaymentsFormCustom
from django.core.urlresolvers import reverse

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

from django.http import HttpResponseRedirect
#from django import forms
from mezzanine.forms.models import Form
from django.template import RequestContext
from mezzanine.forms.forms import FormForForm
from django.shortcuts import render
#ACCEPTABLE_FORMATS = ['%Y-%m-%d %H:%M:%S']
#class OrderForm(forms.Form):
#    field_5 = forms.CharField()
#    date_time = forms.DateField(input_formats=ACCEPTABLE_FORMATS, widget=DateTimeWidget(usel10n=True,bootstrap_version=3))

@processor_for("orderform")
def order_form_processor(request,page):
    
    if request.method == 'POST':
        new = request.POST.copy()
        new.__setitem__('field_8',request.POST['field_8'])
        request.POST=new
        form = FormForForm(page.form, RequestContext(request),
                       request.POST or None, request.FILES or None)
#        pdb.set_trace()
        if form.is_valid():
            form.save() 
        else:
            return render(request,'pages/orderform.html',{'form':form})           
        name, price = request.POST['field_7'].split(' - $')
        ppl = '1' if request.POST['field_12'] == 'Paypal'else '0'
        #if page.form.is_valid():

        redirect = request.path + "?sent=1&price="+price+"&name="+name+"&ppl="+ppl
        return HttpResponseRedirect(redirect)
 
    name, price = page.form.fields.get(label="Type of Service").default.split('$')
 
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": price,
        "item_name": name.split(" -")[0],
        
    "custom": price+request.user.username,
        "notify_url": "http://www.taxinmiasin.com" + reverse('paypal-ipn'),
        "return_url": "http://www.taxinmiasin.com/ppl_return/",
        "cancel_return": "http://www.taxinmiasin.com/cancel/",
    }

    paypal_form = PayPalPaymentsFormCustom(initial=paypal_dict)
            #pdb.set_trace()
    return {'paypal_form':paypal_form}
        
    
@processor_for("faq")
def faq_processor(request,page):
    links = Link.objects.filter(parent=page)
    #pdb.set_trace()
    return {'links': links}