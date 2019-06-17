from django import forms


class BoardForm(forms.Form):
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
