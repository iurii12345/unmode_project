from django.db import models

from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from base.blocks import BaseStreamBlock


class HomePage(Page):
    """
    The Home Page. This looks slightly more complicated than it is. You can
    see if you visit your site and edit the homepage that it is split between
    a:
    - Hero area
    - Body area
    - A promotional area
    - Moveable featured site sections
    """

    # Hero section of HomePage
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Homepage image'
    )
    hero_text = models.CharField(
        null=True,
        blank=True,
        max_length=400,
        help_text='Write an introduction for home page'
    )
    hero_cta = models.CharField(
        null=True,
        blank=True,
        verbose_name='Hero CTA',
        max_length=255,
        help_text='Text to display on Call to Action'
    )
    hero_cta_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Hero CTA link',
        help_text='Choose a page to link to for the Call to Action'
    )

    # Body section of the HomePage
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Home content block",
        blank=True,
        use_json_field=True
    )

    # Promo section of the HomePage
    promo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Promo image'
    )
    promo_title = models.CharField(
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    promo_text = RichTextField(
        null=True,
        blank=True,
        help_text='Write some promotional copy'
    )

    # Featured sections on the HomePage
    # You will see on templates/home/home_page.html that these are treated
    # in different ways, and displayed in different areas of the page.
    # Each list their children items that we access via the children function
    # that we define on the individual Page models e.g. BlogIndexPage
    featured_section_1_title = models.CharField(
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    featured_section_1 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='First featured section for the homepage. '
        'Will display up to three child items.',
        verbose_name='Featured section 1'
    )

    featured_section_2_title = models.CharField(
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    featured_section_2 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Second featured section for the homepage. '
        'Will display up to three child items.',
        verbose_name='Featured section 2'
    )

    featured_section_3_title = models.CharField(
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    featured_section_3 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Third featured section for the homepage. '
        'Will display up to six child items.',
        verbose_name='Featured section 3'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([

            FieldPanel('hero_text', classname="full"),
            MultiFieldPanel([
                FieldPanel('hero_cta'),
                FieldPanel('hero_cta_link'),
            ]),
        ], heading="Hero section"),
        MultiFieldPanel([
            FieldPanel('promo_image'),
            FieldPanel('promo_title'),
            FieldPanel('promo_text'),
        ], heading="Promo section"),
        FieldPanel('body'),
        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('featured_section_1_title'),
                FieldPanel('featured_section_1'),
            ]),
            MultiFieldPanel([
                FieldPanel('featured_section_2_title'),
                FieldPanel('featured_section_2'),
            ]),
            MultiFieldPanel([
                FieldPanel('featured_section_3_title'),
                FieldPanel('featured_section_3'),
            ]),
        ], heading="Featured homepage sections", classname="collapsible")
    ]

    def __str__(self):
        return self.title

    subpage_types = [
        'blog.BlogIndexPage',
        'organizations.OrganizationIndexPage',
        'base.StandardPage'
        ]
