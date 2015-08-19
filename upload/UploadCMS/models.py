from random import random
import hashlib
from django.db import models


class Band(models.Model):

    """A model of a rock band."""
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    guid = models.CharField(max_length=100)
    type = models.CharField(choices=(
        ('p', "Public"),
        ('r', "Private"),
    ),
        max_length=1, default='p'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'band'
        verbose_name_plural = 'bands'

    def __str__(self):
        return self.name

    # count members by band
    def get_members_count(self):
        return self.band.count()

    def get_band_detail_url(self):
        return u"/repositories/%i" % self.id

    def save(self, *args, **kwargs):
        self.guid = hashlib.md5(str(random()).encode('utf-8')).hexdigest()
        super(Band, self).save(*args, **kwargs)


class Member(models.Model):

    """A model of a rock band member."""
    name = models.CharField("Member's name", max_length=200)
    instrument = models.CharField(choices=(
        ('g', "Guitar"),
        ('b', "Bass"),
        ('d', "Drums"),
        ('v', "Vocal"),
        ('p', "Piano"),
    ),
        max_length=1
    )

    band = models.ForeignKey("Band", related_name='band')

    class Meta:
        ordering = ['name']
        verbose_name = 'member'
        verbose_name_plural = 'members'

    def __str__(self):
        return self.name
