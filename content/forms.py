from django.forms.models import BaseInlineFormSet
from content.models import Section


class SectionInlineFormSet(BaseInlineFormSet):
    model = Section
    prefix = 'sections'
