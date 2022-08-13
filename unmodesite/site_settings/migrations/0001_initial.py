# Generated by Django 4.0.6 on 2022-07-25 18:08

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagtailimages', '0024_index_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Facebook page URL')),
                ('instagram', models.CharField(blank=True, help_text='Your Instagram username, without the @', max_length=255)),
                ('telegram', models.CharField(blank=True, help_text='Your Telegram username, without the @', max_length=255)),
                ('twitter', models.CharField(blank=True, help_text='Twitter account URL', max_length=255)),
                ('youtube', models.URLField(blank=True, help_text='YouTube channel or user account URL')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Social media',
            },
        ),
        migrations.CreateModel(
            name='ImportantPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donate_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GoogleApiSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_maps_api_key', models.CharField(blank=True, help_text='The API Key used for Google Maps.', max_length=255, verbose_name='Google Maps API Key')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Google API',
            },
        ),
        migrations.CreateModel(
            name='ContactSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', wagtail.fields.RichTextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Branding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favicon', to='wagtailimages.image', verbose_name='Favicon')),
                ('logo', models.ForeignKey(blank=True, help_text='Brand logo used in the navbar and throughout the site', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logo')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
