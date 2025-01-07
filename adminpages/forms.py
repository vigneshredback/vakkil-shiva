from django import forms
from app.models import TeamMembers
from ckeditor.widgets import CKEditorWidget


class CustomteamMembersForm(forms.ModelForm):

    description = forms.Textarea

    class Meta:
        model = TeamMembers
        fields = '__all__'

        # widgets = {
        #     'biography': forms.Textarea(attrs={'rows': 4, 'class': 'cke'}),
        #     'research': forms.Textarea(attrs={'rows': 4, 'class': 'cke'}),
        #     'education': forms.Textarea(attrs={'rows': 4, 'class': 'cke'}),
        #     'working': forms.Textarea(attrs={'rows': 4, 'class': 'cke'}),
        # }







    