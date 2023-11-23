from django.db import models
from django.utils.html import mark_safe



class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT ='DR','Draft'
        PUBLISH = 'PB', 'Publish'

    owner = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(default='defaultblog.png')
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.PUBLISH)

    def image_tag(self):
        return mark_safe('<img src="/mediafile/%s" width="70" height="70" />' % (self.image))

    image_tag.short_description = 'Image'

    def __str__(self) -> str:
        return self.owner
    
    

    