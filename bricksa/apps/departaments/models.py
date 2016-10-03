#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from bricksa.apps.projects.models import Project


class Departament(models.Model):
    project = models.ForeignKey(
        Project,
        verbose_name=_('Project')
    )
    bedrooms_with_dress = models.CharField(
        _('Bedrooms with dress'),
        max_length=50,
        blank=False,
        null=False,
        default=0
    )
    bedrooms_with_closet = models.CharField(
        _('Bedrooms with closet'),
        max_length=50,
        blank=False,
        null=False,
        default=0
    )
    complete_bathrooms = models.CharField(
        _('Complete bathrooms'),
        max_length=50,
        blank=False,
        null=False,
        default=0
    )
    half_bathrooms = models.CharField(
        _('Half bathrooms'),
        max_length=50,
        blank=False,
        null=False,
        default=0
    )
    living_room = models.BooleanField(
        _('Living room'),
        blank=False,
        null=False,
        default=False
    )
    dinning_room = models.BooleanField(
        _('Dinning room'),
        blank=False,
        null=False,
        default=False
    )
    kitchen = models.BooleanField(
        _('Kitchen'),
        blank=False,
        null=False,
        default=False
    )
    linen_closet = models.BooleanField(
        _('Linen closet'),
        max_length=50,
        blank=False,
        null=False,
        default=False
    )
    service_yard = models.CharField(
        _('Service yard'),
        max_length=50,
        blank=False,
        null=False,
    )
    garden = models.CharField(
        _('Garden'),
        max_length=50,
        blank=False,
        null=False,
    )
    roof_garden = models.CharField(
        _('Roof garden'),
        max_length=50,
        blank=False,
        null=False,
    )
    terrace = models.CharField(
        _('Terrace'),
        max_length=50,
        blank=False,
        null=False,
    )
    parking_places = models.CharField(
        _('Parking places'),
        max_length=50,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Departament')
        verbose_name_plural = _('Departaments')

    def __unicode__(self):
        return 'Departament - %s' % self.project.name