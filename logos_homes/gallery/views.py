from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Projects, ProjectImages


class GalleryView(TemplateView):

    template_name = 'gallery/Gallery.html'

    def get(self, request):
        current_projects = Projects.objects.filter(project_status=False).all()
        previous_projects = Projects.objects.filter(project_status=True).all()
        images = ProjectImages.objects.all()
        context = {
            'current_projects': current_projects,
            'previous_projects': previous_projects,
            'images': images
        }

        return render(request, self.template_name, context)

    def get_images(self, fk):
        image_set = ProjectImages.objects.filter(image_project=fk).all()
        return image_set
