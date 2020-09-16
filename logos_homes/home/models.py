from django.db import models


class Home(models.Model):

    bio = models.TextField(default='')
    main_image = models.ImageField(upload_to='images', default='')
    slider_image_1 = models.ImageField(upload_to='images', default='')
    slider_image_2 = models.ImageField(upload_to='images', default='')
    slider_image_3 = models.ImageField(upload_to='images', default='')


