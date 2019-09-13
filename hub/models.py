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
    ('WB', 'Web App'),
    ('AD', 'Android'),
    ('Dsk', 'Desktop App'),
    
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
    year_production=models.DateField()
    View_counts= models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    