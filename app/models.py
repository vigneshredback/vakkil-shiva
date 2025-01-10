from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

    

CONSULTANTS_CHOICES = [
    ('Admiralty and Maritime', 'Admiralty and Maritime'),
    ('Antitrust & Competition', 'Antitrust & Competition'),
    ('Compliance, Bribery & Anti-corruption', 'Compliance, Bribery & Anti-corruption'),
    ('Corporate Insolvency & Restructuring', 'Corporate Insolvency & Restructuring'),
    ('Employment & Industrial Relations', 'Employment & Industrial Relations'),
    ('Foreign Investment & Exchange Control', 'Foreign Investment & Exchange Control'),
    ('Joint Ventures, Foreign & Technical Collaborations', 'Joint Ventures, Foreign & Technical Collaborations'),
    ('Oil & Gas, Energy and Infrastructure', 'Oil & Gas, Energy and Infrastructure'),
    ('Project Finance', 'Project Finance'),
    ('Regulatory Affairs', 'Regulatory Affairs'),
    ('Technology, Media & Telecommunication', 'Technology, Media & Telecommunication'),
    ('Aerospace and Defense', 'Aerospace and Defense'),
    ('Banking & Finance', 'Banking & Finance'),
    ('Corporate Commercial Advisory', 'Corporate Commercial Advisory'),
    ('Dispute Resolution', 'Dispute Resolution'),
    ('environment', 'Environment'),
    ('Insurance & Reinsurance', 'Insurance & Reinsurance'),
    ('Intellectual Property', 'Intellectual Property'),
    ('Mergers & Acquisitions', 'Mergers & Acquisitions'),
    ('Mining & Resources', 'Mining & Resources'),
    ('Private Equity, Venture Capital & Funds', 'Private Equity, Venture Capital & Funds'),
    ('Real Estate', 'Real Estate'),
    ('Taxation', 'Taxation'),

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
    




