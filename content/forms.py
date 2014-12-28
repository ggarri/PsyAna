from django.forms.formsets import BaseFormSet
from django.forms.models import BaseInlineFormSet
from content.models import Section, Page


class PageFormSet(BaseFormSet):
    model = Page
    prefix = 'sections'
    max_num = 0
    absolute_max = 10
    validate_max = True

    class Meta:
        prefix = ''


class SectionFormSet(BaseFormSet):
    model = Section
    prefix = 'sections'

    class Meta:
        model = Section
        prefix = 'sections'


class SectionInlineFormSet(BaseInlineFormSet):
    model = Section
    parent_model = Page
    prefix = 'sections'

    class Meta:
        prefix = 'sections'
        parent_model = Page
        model = Section
