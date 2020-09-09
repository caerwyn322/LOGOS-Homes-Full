from django.db import models


class Designs(models.Model):

    design_name = models.CharField(max_length=50, default="")
    design_price = models.IntegerField()
    design_desc = models.TextField(default='')
    design_specs = models.FileField(upload_to='pdf')
    design_image = models.ImageField(upload_to='images', default='')

    def __str__(self):
        return self.design_name

    class Meta():
        verbose_name_plural = "Designs"
