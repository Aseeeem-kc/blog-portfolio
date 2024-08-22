from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 bg-gray-900 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:ring-2 focus:ring-teal-400 placeholder-gray-500",
                "placeholder": "Your Name"
            }
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-4 py-2 bg-gray-900 border border-gray-700 rounded-lg text-gray-200 focus:outline-none focus:ring-2 focus:ring-teal-400 placeholder-gray-500",
                "placeholder": "Leave a comment!",
                "rows": 4 
            }
        )
    )
