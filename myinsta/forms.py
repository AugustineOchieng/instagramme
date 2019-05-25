from django import forms
from .models import Image, Comments, Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'date_posted','poster_id']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['date_posted', 'author']

   
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'userId']