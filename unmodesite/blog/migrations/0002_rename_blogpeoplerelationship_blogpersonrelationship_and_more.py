# Generated by Django 4.0.6 on 2022-07-25 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_people_person'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPeopleRelationship',
            new_name='BlogPersonRelationship',
        ),
        migrations.RenameField(
            model_name='blogpersonrelationship',
            old_name='people',
            new_name='person',
        ),
    ]
