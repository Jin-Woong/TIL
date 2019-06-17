from django import forms
from .models import Board


class BoardForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'title',
                'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        # textarea 처럼 꾸밀 수 있다.
        label='내용',
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'cols': 50,
                'placeholder': 'Enter the content',
                'class': 'content-type',
            }
        )
    )

    class Meta:
        model = Board
        fields = ('title', 'content',)
