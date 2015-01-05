from django import forms
from main.models import Order
from datetimewidget.widgets import DateTimeWidget

PAYMENT_CHOICES = [
    ('in_cash', 'in cash'),
    ('with_paypal', 'with Paypal')
]
FREQ_CHOICES = [
    ('one_time', '1 time'),
    ('weekly', 'weekly'),
    ('bi-weekly', 'bi-weekly'),
    ('tri-weekly', 'tri-weekly'),
    ('monthly', 'monthly')
]
TYPE_CHOICES = [
    ('1_bedroom', '1 bedroom - $55'),
    ('2_bedroom', '2 bedroom - $75'),
    ('3_bedroom', '3 bedroom - $95'),
    ('4_bedroom', '4 bedroom - $125'),
    ('5 bedroom', '5 bedroom - $155'),
    ('6_bedroom', '6 bedroom - $185'),
]
ACCEPTABLE_FORMATS = ['%Y-%m-%d %H:%M:%S']
class OrderForm(forms.ModelForm):
    address = forms.CharField()
    city = forms.CharField()
    type_of_service = forms.ChoiceField(choices=TYPE_CHOICES)
    date_time = forms.DateField(input_formats=ACCEPTABLE_FORMATS, widget=DateTimeWidget(usel10n=True,bootstrap_version=3))
    frequency_of_service = forms.ChoiceField(choices=FREQ_CHOICES)
    payment_type = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Order

from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.widgets import ValueHiddenInput, ReservedValueHiddenInput
 
class PayPalPaymentsFormCustom(PayPalPaymentsForm):
    image_url = forms.CharField(widget=ValueHiddenInput)
    custom = forms.CharField(widget=ValueHiddenInput)
    hosted_button_id = forms.CharField(widget=ValueHiddenInput)
