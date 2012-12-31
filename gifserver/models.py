from django.db import models


# the site of the gif in question
# gs = Gifsite(url="http://bukk.it/", name='bukk.it', date_added=timezone.now())
class Gifsite(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField('date added')
    active = models.BooleanField()

    def __unicode__(self):
        return self.name


# the gif. i mean, that's why we're here, right?
# g.gif_set.create(name="noregrets.gif", url="http://bukk.it/noregrets.gif", date_added=timezone.now())
class Gif(models.Model):
    gifsite = models.ForeignKey(Gifsite)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    date_added = models.DateTimeField('date added')
    active = models.BooleanField()

    def __unicode__(self):
        return self.name
