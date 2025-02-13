from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Home
from about_us.models import TeamMembers
from gallery.models import Projects


class HomeView(TemplateView):

    template_name = 'home/Home.html'

    def get(self, request):
        details = Home.objects.all()
        team = TeamMembers.objects.all()
        previous_projects = Projects.objects.filter(project_status=True).all()
        context = {
            'details': details,
            'team': team,
            'projects': previous_projects
        }

        return render(request, self.template_name, context)