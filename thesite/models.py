from django.db import models

class pages(models.Model):
    page_title = models.CharField(max_length=200)
    
    # ...
    def __unicode__(self):
        return self.page_title

