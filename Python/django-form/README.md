# User model

 accounts/models.py 수정

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='followings',
    )
```



django_form/settings.py 수정

```python
#...
#...
AUTH_USER_MODEL = 'accounts.user'
```



accounts/admin.py 수정

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(User, UserAdmin)
```



