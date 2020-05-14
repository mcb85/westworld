
# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    
    first_name = models.CharField(max_length=256, blank=False, null=False)

    last_name = models.CharField(max_length=256, blank=False, null=False)

    email = models.EmailField(max_length=256, blank=False, null=False)

    age = models.IntegerField(blank=True, null=True)

    created = models.DateTimeField(default= timezone.now())
    modified= models.DateTimeField(default= timezone.now())



    def __str__(self):
        """ Sensible string representation of a user."""
        return "{0} {1} | {2}".format(self.first_name, self.last_name, 
                self.email)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)