# Generated by Django 4.0.6 on 2022-07-25 19:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('base', '0002_rename_people_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='footertext',
            name='locale',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footertext',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='footertext',
            unique_together={('translation_key', 'locale')},
        ),
    ]
