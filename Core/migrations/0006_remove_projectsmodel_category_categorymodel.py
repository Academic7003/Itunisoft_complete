# Generated by Django 4.0.4 on 2022-05-13 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_alter_partnersmodel_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectsmodel',
            name='category',
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='models', to='Core.projectcategoriesmodel')),
            ],
        ),
    ]
