from django.db import models


class YourModel(models.Model):
    name = models.CharField(max_length=200)
    relation = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.name
