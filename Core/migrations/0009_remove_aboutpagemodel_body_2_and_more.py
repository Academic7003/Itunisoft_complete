# Generated by Django 4.0.4 on 2022-05-13 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_alter_projectsmodel_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpagemodel',
            name='body_2',
        ),
        migrations.RemoveField(
            model_name='aboutpagemodel',
            name='title_2',
        ),
    ]