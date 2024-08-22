from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-900 rounded-lg text-gray-200 focus:outline-none focus:ring-2 focus:ring-teal-400 mb-2',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 bg-gray-900 rounded-lg text-gray-200 focus:outline-none focus:ring-2 focus:ring-teal-400 mb-2',
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 bg-gray-900 rounded-lg text-gray-200 focus:outline-none focus:ring-2 focus:ring-teal-400 mb-2',
                'rows': '4',  # Adjust the number of visible rows here
            }),
        }
