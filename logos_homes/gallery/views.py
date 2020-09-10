from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Projects, ProjectImages


class GalleryView(TemplateView):

    template_name = 'gallery/Gallery.html'

    def get(self, request):
        projects = Projects.objects.all()
        project_images = Projects.projectImages_set.all()
        context = {
            'projects': projects,
            'project_images': project_images
        }

        return render(request, self.template_name, context)