from django.forms.formsets import BaseFormSet
from django.forms.models import BaseInlineFormSet, ModelForm
from content.models import Section, Page


class PageFormSet(BaseFormSet):
    model = Page
    prefix = 'sections'
    max_num = 0
    absolute_max = 10
    validate_max = True

    class Meta:
        prefix = ''


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['template', 'skeleton', 'title', 'subtitle', 'text', 'head_photo', 'css_class']
        prefix = 'sections'


class SectionInlineFormSet(BaseInlineFormSet):
    model = Section
    parent_model = Page
    prefix = 'sections'

    class Meta:
        prefix = 'sections'
        parent_model = Page
        model = Section
