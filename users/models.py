from django.contrib.auth.models import AbstractUser
from django.db import models

from habits.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True,
                              verbose_name='почта')
    tg_chat_id = models.CharField(max_length=50,
                                  verbose_name='телеграм chat-id',
                                  **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
