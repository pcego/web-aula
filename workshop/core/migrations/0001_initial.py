# Generated by Django 2.1.7 on 2019-05-16 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('website', models.URLField(blank=True, verbose_name='website')),
                ('photo', models.URLField(verbose_name='foto')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'palestrante',
                'verbose_name_plural': 'palestrantes',
            },
        ),
    ]
