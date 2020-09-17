from django.db import models


class Projects(models.Model):

    project_name = models.CharField(max_length=50, default='')
    project_desc = models.TextField(default='')
    project_main_image = models.ImageField(upload_to='images', default='')
    project_status = models.BooleanField(default=False)
    # project_sub_images = models.ImageField(upload_to='images', max_length=5, default='')
    project_specs = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.project_name

    class Meta():
        verbose_name_plural = "Projects"


class ProjectImages(models.Model):

    image_name = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='images', default='')
    image_project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_project.project_name + " " + self.image_name

    class Meta():
        verbose_name_plural = "Project Images"
