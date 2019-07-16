from django import forms

from . import models


class ProfileForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.EmailInput())
    confirm_email=forms.EmailField(widget=forms.EmailInput())
    bio = forms.Textarea()

    class Meta:
        model = models.Profile
        fields = [
            #'avatar',
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'qualification',
            'keywords',
            'bio',
            'city',
            'state',
            'country',
            'favorite_animal',
            'hobby',
            'area_of_experince',
            'price',
            'experince',
            'cover',

        ]

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        bio = cleaned_data.get("bio")

        if email != confirm_email:
            raise forms.ValidationError(
                "Emails must match!"
            )

        if len(bio) < 10:
            raise forms.ValidationError(
                "Bio must be 10 characters or longer!"
            )
'''
class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [
        'project_title',
        'project_description',
        ]
    def clean(self):
        cleaned_data = super(ProjectForm, self).clean()
        email = cleaned_data.get("project_title")
        confirm_email = cleaned_data.get("project_description")
'''
