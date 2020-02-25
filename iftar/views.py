from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Need, Donor, Mosque
from django import forms



# Create your views here.
class IndexView(generic.ListView):
    template_name = 'iftar/index.html'
    context_object_name = 'needs_list'

    def get_queryset(self):
        #needs_taken = Donor.objects.all()
        #return needs_taken

        #works if you want to filter by approved
        #is_approved = Donor.objects.filter(is_approved=True)
        #return is_approved.values('need__description', 'name', 'is_approved').order_by('need__display_order')

        return Donor.objects.values('need__description', 'name', 'is_approved').order_by('need__display_order')
        #Works Below for figuring out needs left
        #needs_left = Need.objects.exclude(id__in=needs_taken)
        #return needs_left


class DonorCreateForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'phone', 'need', 'donation']
        labels = {'need': 'What the mosque needs', 'donation': 'What you will provide'}
        #labels = {'donation': 'What you will provide', }
#        widgets = {
#            'need': forms.RadioSelect()
#        }


class DonorCreate(generic.CreateView):
    form_class = DonorCreateForm
    model = Donor
    #fields = ['name', 'phone', 'food_or_cash', 'need']
    def get_form(self, *args, **kwargs):
        needs_taken = Donor.objects.all()
        needs_left = Need.objects.exclude(id__in=needs_taken).order_by('display_order')
        form = super(DonorCreate, self).get_form(*args, **kwargs)
        form.fields['need'].queryset = needs_left
        return form

