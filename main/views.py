from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import Order
from main.forms import OrderForm
import pdb

def order(request):
#    pdb.set_trace()
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        #pdb.set_trace()
        if form.is_valid():
            # Form processing goes here.
            redirect = request.path + "?sent=1"
            return HttpResponseRedirect(redirect)
    return render(request, 'pages/order.html', {"form": form})
