from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class Branding(BaseSetting):
    logo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Logo',
        help_text='Brand logo used in the navbar and throughout the site'
    )
    favicon = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='favicon',
        verbose_name='Favicon',
    )

    panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel('logo'),
                ImageChooserPanel('favicon'),
            ],
            heading='Branding'
        )
    ]


@register_setting
class GoogleApiSettings(BaseSetting):
    """
    Settings for Google API services.
    """
    class Meta:
        verbose_name = 'Google API'

    google_maps_api_key = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Google Maps API Key',
        help_text='The API Key used for Google Maps.'
    )


@register_setting
class ContactSettings(BaseSetting):
    address = RichTextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
    )

    panels = [
        FieldPanel('address'),
        FieldPanel('email'),
    ]


@register_setting
class ImportantPages(BaseSetting):
    donate_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('donate_page'),
    ]


@register_setting
class SocialMediaSettings(BaseSetting):
    class Meta:
        verbose_name = 'Social media'

    facebook = models.URLField(
        blank=True,
        help_text='Facebook page URL'
    )
    instagram = models.CharField(
        blank=True,
        max_length=255,
        help_text='Your Instagram username, without the @'
    )
    telegram = models.CharField(
        blank=True,
        max_length=255,
        help_text='Your Telegram username, without the @'
    )
    twitter = models.CharField(
        blank=True,
        max_length=255,
        help_text='Twitter account URL'
    )
    youtube = models.URLField(
        blank=True,
        help_text='YouTube channel or user account URL'
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('facebook'),
                FieldPanel('instagram'),
                FieldPanel('telegram'),
                FieldPanel('twitter'),
                FieldPanel('youtube'),
            ],
            heading='Links'
        )
    ]
