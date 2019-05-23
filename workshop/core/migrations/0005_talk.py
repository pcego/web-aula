# Generated by Django 2.1.7 on 2019-05-21 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190521_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='título')),
                ('date', models.DateField(verbose_name='data')),
                ('start', models.TimeField(verbose_name='início')),
                ('description', models.TextField(verbose_name='descrição')),
                ('speakers', models.ManyToManyField(to='core.Speaker')),
            ],
            options={
                'verbose_name': 'palestra',
                'verbose_name_plural': 'palestras',
            },
        ),
    ]