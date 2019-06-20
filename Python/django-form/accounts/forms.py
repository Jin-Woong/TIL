# forms.py
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # settings.AUTH_USER_MODEL 에 등록한 accounts
        fields = UserCreationForm.Meta.fields


# 기존 form에서 내가 원하는 부분만 추출하기
class CustomUserChangeForm(UserChangeForm):
    # 모델에 대한 정보가 담기는 곳
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')




