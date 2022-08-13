from __future__ import unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import TaggedItemBase

from wagtail.contrib.routable_page.models import RoutablePageMixin
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail.models import Page, Orderable
from wagtail.search import index


from base.blocks import BaseStreamBlock


class OrganizationCountryRelationship(Orderable, models.Model):
    page = ParentalKey(
        'OrganizationPage',
        related_name='organization_country_relationship',
        on_delete=models.CASCADE)
    country = models.ForeignKey(
        'base.Country',
        related_name='country_organization_relationship',
        on_delete=models.CASCADE)

    panels = [
        FieldPanel('country')
    ]


class OrganizationPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'OrganizationPage',
        related_name='tagged_items',
        on_delete=models.CASCADE)


class OrganizationPage(Page):
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='vfbd'
        )
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page body",
        blank=True,
        use_json_field=True
        )
    address = models.TextField(
        help_text='Address',
        null=True,
        blank=True
        )
    phone_number = models.CharField(
        help_text='Phone number',
        max_length = 30,
        null=True,
        blank=True
        )
    site = models.URLField(
        help_text='Site',
        null=True,
        blank=True)
    email = models.EmailField(
        help_text='Email',
        max_length = 254,
        blank=True)
    tags = ClusterTaggableManager(
        through=OrganizationPageTag,
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        FieldPanel('logo'),
        FieldPanel('body'),
        InlinePanel(
            'organization_country_relationship',
            label="Country(s)",
            panels=None,
            min_num=0),
        FieldPanel('address'),
        FieldPanel('phone_number'),
        FieldPanel('site'),
        FieldPanel('email'),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def countries(self):
        countries = [
            n.country for n in self.organization_country_relationship.all()
        ]

        return countries

    @property
    def get_tags(self):
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    parent_page_types = ['OrganizationIndexPage']

    subpage_types = []


class OrganizationIndexPage(RoutablePageMixin, Page):
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    parent_page_types = ['home.HomePage']

    subpage_types = ['OrganizationPage']

    def children(self):
        return self.get_children().specific().live()

    def get_organizations(self, tag=None):
        organizations = OrganizationPage.objects.descendant_of(
            self).live().order_by('-title')
        if tag:
            organizations = organizations.filter(tags=tag)
        return organizations

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_organizations(), 6)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        context = super(OrganizationIndexPage, self).get_context(request)
        # OrganizationPage objects (get_organizations) are passed through pagination
        organizations = self.paginate(request, self.get_organizations())
        context['organizations'] = organizations
        return context
