from django import forms
from django.forms import formset_factory
from .models import FileTemplate, LiveReport


class FileTemplateForm(forms.ModelForm):

    class Meta:
        model = FileTemplate
        fields = [
            'name',
            'description',
            'fileImport',
            'intervals',
            'live_instances',
            'save_history'
        ]


class LiveReportForm(forms.ModelForm):

    class Meta:
        model = LiveReport
        fields = [
            'live_file'
        ]
