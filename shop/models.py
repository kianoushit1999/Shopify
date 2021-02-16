from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class SlideShow(models.Model):
    title = models.CharField(max_length=128)
    context = models.TextField()
    price = models.IntegerField(
        verbose_name=_("price"))
    image = models.ImageField(
        upload_to='homepage/'
    )