from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Создает и возвращает пользователя с email и паролем."""
        if not email:
            raise ValueError("Email должен быть указан")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создает и возвращает суперпользователя с email."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперпользователь должен иметь is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Модель создания и регистрации пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name="Ваша почта")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Номер телефона")
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name="Фото(необязательно)")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город проживания")
    token = models.CharField(max_length=100, verbose_name="Токен", blank=True, null=True)
    tg_chat_id = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name="Телеграм чат-id")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = []
