from django.contrib.gis.db import models
from django.contrib.gis import geos
from .utils import geocoder


class People(models.Model):
    username = models.CharField(verbose_name='姓名', max_length=52)
    sex = models.CharField(verbose_name='性别', max_length=2, default='男')
    age = models.IntegerField(verbose_name='年龄', default=0)
    address = models.CharField(verbose_name='地址', max_length=24)
    location = models.PointField(verbose_name='位置', geography=True, blank=True, null=True)

    def __str__(self):
        return self.username

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.location:
            try:
                lng, lat = geocoder(self.address)
            except Exception:
                pass
            else:
                self.location = geos.Point(lng, lat)
        super(People, self).save()
