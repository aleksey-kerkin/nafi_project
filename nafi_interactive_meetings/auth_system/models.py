from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("У пользователя должна быть почта")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(email=email, **kwargs)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password=password, **kwargs)

        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    LEGAL = "LP"
    NATURAL = "NP"
    PERSONS = [
        (LEGAL, "Юридическое лицо"),
        (NATURAL, "Физическое лицо"),
    ]

    email = models.EmailField("Email адрес", max_length=255, unique=True)
    name = models.CharField("Имя пользователя", max_length=255)
    middlename = models.CharField("Отчество", blank=True, null=True, max_length=255)
    lastname = models.CharField("Фамилия", blank=True, null=True, max_length=255)
    phone = PhoneNumberField("Номер телефона", blank=True)
    position = models.CharField("Должность", blank=True, null=True, max_length=127)
    entity = models.CharField("Физ./Юр. лицо", choices=PERSONS, default=NATURAL, max_length=17)
    organization = models.CharField("Организация", blank=True, null=True, max_length=255)
    business_area = models.CharField("Сфера деятельности", default="Безработный", max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "business_area"]

    def full_name(self):
        return f"{self.lastname} {self.name} {self.middlename}"

    def short_name(self):
        return self.name

    def __str__(self):
        return f"{self.name}({self.email})"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
