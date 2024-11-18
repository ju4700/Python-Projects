from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    affiliate_link = models.URLField()
    platform_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)  # Add this field

    def __str__(self):
        return self.title
