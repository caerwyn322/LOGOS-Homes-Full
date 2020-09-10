from django.shortcuts import render
from .models import TeamMembers
from django.views.generic import TemplateView


class AboutUsView(TemplateView):

    template_name = 'about_us/About-Us.html'

    def get(self, request):
        members = TeamMembers.objects.all()
        context = {
            'members': members
        }

        return render(request, self.template_name, context)


