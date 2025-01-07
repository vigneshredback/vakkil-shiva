from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

    

CONSULTANTS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('archived', 'Archived'),
]

DISTRICT_CHOICES = [
    ('ariyalur', 'Ariyalur'),
    ('chengalpattu', 'Chengalpattu'),
    ('chennai', 'Chennai'),
    ('coimbatore', 'Coimbatore'),
    ('cuddalore', 'Cuddalore'),
    ('dharmapuri', 'Dharmapuri'),
    ('dindigul', 'Dindigul'),
    ('erode', 'Erode'),
    ('kallakurichi', 'Kallakurichi'),
    ('kanchipuram', 'Kanchipuram'),
    ('kanyakumari', 'Kanyakumari'),
    ('karur', 'Karur'),
    ('krishnagiri', 'Krishnagiri'),
    ('madurai', 'Madurai'),
    ('mayiladuthurai', 'Mayiladuthurai'),
    ('nagapattinam', 'Nagapattinam'),
    ('namakkal', 'Namakkal'),
    ('nilgiris', 'Nilgiris'),
    ('perambalur', 'Perambalur'),
    ('pudukottai', 'Pudukottai'),
    ('ramanathapuram', 'Ramanathapuram'),
    ('ranipet', 'Ranipet'),
    ('salem', 'Salem'),
    ('sivaganga', 'Sivaganga'),
    ('tenkasi', 'Tenkasi'),
    ('thanjavur', 'Thanjavur'),
    ('theni', 'Theni'),
    ('thoothukudi', 'Thoothukudi'),
    ('tiruchirappalli', 'Tiruchirappalli'),
    ('tirunelveli', 'Tirunelveli'),
    ('tirupattur', 'Tirupattur'),
    ('tiruppur', 'Tiruppur'),
    ('tiruvallur', 'Tiruvallur'),
    ('tiruvannamalai', 'Tiruvannamalai'),
    ('tiruvarur', 'Tiruvarur'),
    ('vellore', 'Vellore'),
    ('viluppuram', 'Villupuram'),
    ('virudhunagar', 'Virudhunagar'),
]



class TeamMembers(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    district = models.CharField(
        max_length=100,
        choices=DISTRICT_CHOICES,
        default='chennai'
    )
    # image = models.ImageField()
    consultant = models.CharField(
        max_length=100,
        choices=CONSULTANTS_CHOICES,
        default='unknown'
    )
    facebook = models.URLField(max_length=100,blank=True,null=True)
    twitter = models.URLField(max_length=100,blank=True,null=True)
    linkedin = models.URLField(max_length=100,blank=True,null=True)
    instagram = models.URLField(max_length=100,blank=True,null=True)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    biography = RichTextField()
    research = RichTextField()
    education = RichTextField()
    working = RichTextField()


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'my team'
        ordering = ['name']
    




