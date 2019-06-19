# forms.py
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


# 기존 form에서 내가 원하는 부분만 추출하기
class CustomUserChangeForm(UserChangeForm):
    # 모델에 대한 정보가 담기는 곳
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')




