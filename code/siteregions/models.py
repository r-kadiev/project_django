from django.db import models

class Site(models.Model):
    domain = models.CharField(max_length=255)

    def __str__(self):
        return self.domain

class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SiteRegion(models.Model):
    OPTION = 'option'
    COOKIE = 'cookie'
    SUBDOMAIN = 'subdomain'
    TYPE_CHOICES = [
        (OPTION, 'Option'),
        (COOKIE, 'Cookie'),
        (SUBDOMAIN, 'Subdomain')
    ]
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


