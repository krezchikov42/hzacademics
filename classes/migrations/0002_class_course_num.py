# Generated by Django 2.2.7 on 2019-11-19 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='course_num',
            field=models.CharField(default='CS0000', max_length=64),
            preserve_default=False,
        ),
    ]
