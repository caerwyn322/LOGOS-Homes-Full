from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Designs


class DesignView(TemplateView):

    template_name = 'designs/Designs.html'

    def get(self, request):
        designs = Designs.objects.all()
        context = {
            'designs': designs
        }

        return render(request, self.template_name, context)