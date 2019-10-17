from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    comments = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'rows': 4, 'cols': 40, 'placeholder': 'Comments'}))