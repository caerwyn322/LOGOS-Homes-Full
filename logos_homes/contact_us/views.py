from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Contacts
from .form import ContactForm


class ContactView(TemplateView):

    template_name = 'contact_us/Contact-Us.html'

    def get(self, request):
        form = ContactForm
        context = {
            'forms': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                mail = Contacts()
                mail.email = form.cleaned_data['email']
                mail.name = form.cleaned_data['name']
                mail.contact_number = form.cleaned_data['contact_number']
                mail.message = form.cleaned_data['message']
                mail.save()
            else:
                form = ContactForm()
        return self.get(request)