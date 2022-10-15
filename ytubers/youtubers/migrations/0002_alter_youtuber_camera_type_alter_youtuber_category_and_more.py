# Generated by Django 4.1.2 on 2022-10-13 05:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('canon', 'canon'), ('sony', 'sony'), ('nikon', 'nikon'), ('red', 'red'), ('fuji', 'fuji'), ('panasonic', 'panasonic')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('comedy', 'comedy'), ('tech_review', 'tech_review'), ('finance', 'finance'), ('vlogs', 'vlogs'), ('education', 'education'), ('gaming', 'gaming')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]