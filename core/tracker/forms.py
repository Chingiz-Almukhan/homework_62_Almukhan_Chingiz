from django import forms

from tracker.models import Project
from tracker.models.issue_tracker import IssueTracker


class AddEditForm(forms.ModelForm):
    class Meta:
        model = IssueTracker
        fields = ['summary', 'description', 'status', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['summary'].widget.attrs.update(
            {'placeholder': 'Введите название', 'type': 'text', 'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Введите описание', 'type': 'text', 'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['type'].widget.attrs.update({'class': 'form-control'})


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Поиск')


class DateInput(forms.DateInput):
    input_type = 'date'


class AddProjectForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput, label='Дата начала')
    end_date = forms.DateField(widget=DateInput, label='Дата окончания')

    class Meta:
        model = Project
        fields = ['name', 'start_date', 'end_date', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Введите название', 'type': 'text', 'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Введите описание', 'type': 'text', 'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update(
            {'class': 'form-control', 'min': "2018-01-01", 'max': "2090-12-31"})
        self.fields['end_date'].widget.attrs.update(
            {'class': 'form-control', 'min': "2018-01-01", 'max': "2090-12-31", 'type': 'date'})
