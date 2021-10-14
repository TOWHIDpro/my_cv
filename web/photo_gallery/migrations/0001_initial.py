# Generated by Django 3.2.5 on 2021-09-24 06:26

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=500)),
                ('content', froala_editor.fields.FroalaField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('edited', models.DateField(auto_now=True)),
            ],
        ),
    ]