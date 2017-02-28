from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

USER_MODEL = get_user_model()


class Event(models.Model):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
        null=True,
    )
    creator = models.ForeignKey(
        USER_MODEL,
        blank=False,

    )
    members = models.ManyToManyField(
        USER_MODEL,
        blank=True
    )

    def __str__(self):
        return self.title
