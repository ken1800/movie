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
    ('web app', 'Web App'),
    ('android', 'Android'),
    ('desktop app', 'Desktop App'),
    
            ]
    state= [
    ('RA', 'Recently added'),
    ('MW', 'Most Watched'),
    ('TR', 'Top Rated'),
    
            ]
    
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 600)
    image = models.ImageField(upload_to ='images')
    categories = models.CharField(choices = cate ,max_length = 20)
    status = models.CharField(choices= state,max_length = 200) 
    cast = models.CharField(max_length = 200)
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