from django.db import models

# Create your models here.
class hub(models.Model):
    language = [
    ('PY', 'Python'),
    ('JS', 'Java Script'),
    ('JV', 'Java'),
    ('KOT', 'Kotlin'),
    ('PHP', 'PHP'),
    ('HT', 'Html'),
    ('R', 'R'),
                ]
    cate = [
    ('W', 'Web App'),
    ('A', 'Android'),
    ('D', 'Desktop App'),
    
            ]
    state= [
    ('RA', 'Recently added'),
    ('MW', 'Most Watched'),
    ('TR', 'Top Rated'),
    
            ]
    
    
    def language_default():
        return {"language": "Python"}

 #contact_info = JSONField("ContactInfo", default=contact_default)
    
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 600)
    image = models.ImageField(upload_to ='images')
    category = models.CharField(choices = cate ,max_length = 20)
    status = models.CharField(choices= state,max_length = 200) 
    cast = models.CharField(max_length = 200)
    language = models.CharField(choices= language,max_length = 200, default=language_default) 
    year_production=models.DateField()
    View_counts= models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class CodeLinks(models.Model):
        link_choice=(
                ('D','Download_link'),
                ('W','Watch_link'),
                
        )
        cod = models.ForeignKey(hub, on_delete=models.CASCADE)
        type = models.CharField(choices=link_choice,max_length = 600)
        link =models.URLField()
        
        def __str__(self):
                return self.type