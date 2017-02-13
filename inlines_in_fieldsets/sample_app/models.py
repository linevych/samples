from django.db import models
from django.utils.translation import ugettext_lazy as _


class ModelA(models.Model):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        blank=True,
        null=True,
    )

    description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    model_a = models.ForeignKey(
        'ModelA',
        verbose_name='model A'
    )
    image = models.ImageField(
        upload_to='images/'
    )
