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

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            # 'image': forms.FileInput(attrs={'class': 'form-control mb-3'}),
            'district': forms.Select(attrs={'class': 'form-control mb-3'}),
            'consultant': forms.Select(attrs={'class': 'form-control mb-3'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
        }







    