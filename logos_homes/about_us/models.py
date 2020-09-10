from django.db import models


class TeamMembers(models.Model):

    member_name = models.CharField(max_length=50, default='')
    member_bio = models.TextField()
    member_position = models.CharField(max_length=20, default='')
    member_image = models.ImageField(upload_to='images', default='')

    def __str__(self):
        return self.member_name

    class Meta():
        verbose_name_plural = "Team Members"

