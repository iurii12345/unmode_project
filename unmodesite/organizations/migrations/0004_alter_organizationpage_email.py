# Generated by Django 4.0.7 on 2022-08-12 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_organizationpage_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationpage',
            name='email',
            field=models.EmailField(blank=True, default=4567, help_text='Email', max_length=254),
            preserve_default=False,
        ),
    ]
