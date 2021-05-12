from django.db.models import fields
from .models import *
from django import forms


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'field'}),
            'Duration': forms.TextInput(attrs={'class': 'field'}),
        }


class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = "__all__"

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'field'}),
            'Duration': forms.TextInput(attrs={'class': 'field'}),
            'Host': forms.TextInput(attrs={'class': 'field'}),
            'Participants': forms.Textarea(attrs={'class': 'field'}),

        }


class AudiobookForm(forms.ModelForm):
    class Meta:
        model = Audiobook
        fields = "__all__"

        widgets = {
            'Title': forms.TextInput(attrs={'class': 'field'}),
            'Author': forms.TextInput(attrs={'class': 'field'}),
            'Narrator': forms.TextInput(attrs={'class': 'field'}),
            'Duration': forms.TextInput(attrs={'class': 'field'}),

        }
