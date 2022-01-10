from django.db import models
from django.utils import timezone 
from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from modelcluster.fields import ParentalKey


class ClientIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]


class ClientPage(Page):
    birth_day = models.DateField("Birthday", default= timezone.now)
    first_name = models.CharField(max_length=250, default='')
    last_name = models.CharField(max_length=250, default='')
    address = models.CharField(max_length=250, default='')
    intro = RichTextField(blank=True, default='')
    avatar = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('first_name'),
        index.SearchField('last_name'),
        index.SearchField('address'),
        index.SearchField('intro'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('birth_day'),
        FieldPanel('last_name'),
        FieldPanel('first_name'),
        FieldPanel('address'),
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('avatar'),
    ]