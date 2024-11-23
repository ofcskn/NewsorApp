from django import forms

class ChatForm(forms.Form):
    """
    Form for user to input chat messages.
    """
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Type your message here...',
            'rows': 3,
            'class': 'chat-input',
        }),
        label='',
        max_length=500,
    )
