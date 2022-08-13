from django.db import models

from modelcluster.models import ClusterableModel

from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    MultiFieldPanel,
)
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page, TranslatableMixin
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from .blocks import BaseStreamBlock


@register_snippet
class Person(index.Indexed, ClusterableModel):
    """
    A Django model to store Person objects.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI (e.g. /admin/snippets/base/people/)

    `Person` uses the `ClusterableModel`, which allows the relationship with
    another model to be stored locally to the 'parent' model (e.g. a PageModel)
    until the parent is explicitly saved. This allows the editor to use the
    'Preview' button, to preview the content, without saving the relationships
    to the database.
    https://github.com/wagtail/django-modelcluster
    """
    first_name = models.CharField("First name", max_length=254)
    last_name = models.CharField("Last name", max_length=254)
    job_title = models.CharField("Job title", max_length=254)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name', classname="col6"),
                FieldPanel('last_name', classname="col6"),
            ])
        ], "Name"),
        FieldPanel('job_title'),
        FieldPanel('image')
    ]

    search_fields = [
        index.SearchField('first_name'),
        index.SearchField('last_name'),
    ]

    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition('fill-50x50').img_tag()
        except:  # noqa: E722 FIXME: remove bare 'except:'
            return ''

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


@register_snippet
class FooterText(TranslatableMixin, models.Model):
    """
    This provides editable text for the site footer. Again it uses the
    decorator `register_snippet` to allow it to be accessible via
    the admin. It is made accessible on the template via a template tag
    defined in base/templatetags/ navigation_tags.py
    """
    body = RichTextField()

    panels = [
        FieldPanel('body'),
    ]

    def __str__(self):
        return "Footer text"

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = 'Footer texts'


@register_snippet
class Country(TranslatableMixin, models.Model):
    """
    This provides editable text for the site footer. Again it uses the
    decorator `register_snippet` to allow it to be accessible via
    the admin. It is made accessible on the template via a template tag
    defined in base/templatetags/ navigation_tags.py
    """
    name = models.CharField(
        max_length=254
    )

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return '{}'.format(self.name)

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = 'Countries'


class StandardPage(Page):
    """
    A generic content page. On this demo site we use it for an about page but
    it could be used for any type of page content that only needs a title,
    image, introduction and body field
    """
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; width between 1000px and 3000px.'
    )
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page body",
        blank=True,
        use_json_field=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        FieldPanel('body'),
        FieldPanel('image'),
    ]

    parent_page_types = ['home.HomePage']
