from django.db import models


class Speaker(models.Model):

    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    website = models.URLField('website', blank=True)
    photo = models.URLField('foto')
    description = models.TextField('descrição', blank=True)
    skill = models.CharField('habilidade', max_length=100, blank=True)


    class Meta:

        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'


    def __str__(self):

        return self.name
