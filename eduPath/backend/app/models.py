from django.db import models

# Create your models here.
class University(models.Model):
    id = models.AutoField(primary_key=True)
    university_name = models.CharField(max_length=100)
    university_image = models.TextField()
    university_overview = models.TextField()
    university_fields = models.CharField(max_length=100)
    university_location = models.CharField(max_length=100)
    university_ranking = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    website = models.URLField()

    def __str__(self):
        return self.university_name