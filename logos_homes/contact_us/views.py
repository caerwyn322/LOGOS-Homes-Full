from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Contacts
from .form import ContactForm


class ContactView(TemplateView):

    template_name = 'contact_us/Contact Us.html'

    def get(self, request):
        form = ContactForm
        context = {
            'forms' : form
        }

        return render(request, self.template_name, context,)

