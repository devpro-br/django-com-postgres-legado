# Generated by Django 4.2.5 on 2023-09-21 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_cursos_option_to_managed'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='a',
            field=models.CharField(blank='', default='', max_length=255, null=True),
        ),
    ]
