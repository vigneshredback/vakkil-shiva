from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Consultants(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'consultant type'
        ordering = ['name']


class Districts(models.Model):
    name = models.CharField(max_length=50,verbose_name='District in TN')

    def __str__(self):
        return self.name
    

class TeamMenbers(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/teammembers')
    consultant = models.ForeignKey(Consultants, on_delete=models.CASCADE)
    facebook = models.URLField(max_length=100,blank=True,null=True)
    twitter = models.URLField(max_length=100,blank=True,null=True)
    linkedin = models.URLField(max_length=100,blank=True,null=True)
    instagram = models.URLField(max_length=100,blank=True,null=True)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    biography = models.TextField()
    education = HTMLField()
    working = HTMLField()
    research = HTMLField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'my team'
        ordering = ['name']
    




