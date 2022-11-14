from django.contrib.auth.models import AbstractUser
from django.db import models


class Student(AbstractUser):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')
    email = models.EmailField(verbose_name="Почта")

    USERNAME_FIELD = ['email']
    REQUIRED_FIELDS = []

    def get_full_name(self):
        if self.middle_name is not None:
            return f'{self.last_name} {self.first_name} {self.middle_name}'
        else:
            return f'{self.last_name} {self.first_name}'


class Application(models.Model):
    FORM_OF_EDUCATION_CHOICES = [
        ('Очная', 'Очная'),
        ("Очно-заочная", "Очно-заочная"),
        ("Заочная", "Заочная")
    ]
    BASE_OF_EDUCATION_CHOICES = [
        ('договорная', "договорная"),
        ('бюджетная', "бюджетная"),
        ('на платной основе', "на платной основе"),
    ]
    PROGRAM_OF_EDUCATION_CHOICES = [
        ("аспирантура", "аспирантура"),
        ("СПО", "СПО"),
        ("бакалавриат", "бакалавриат"),
        ("специалитета", "специалитет"),
        ("магистратура", "магистратура"),
        ("ординатура", "ординатура"),
        ("подготовка научно-педагогических кадров в аспирантуре",
         "подготовка научно-педагогических кадров в аспирантуре"),
    ]

    address = models.TextField(max_length=255, verbose_name='Адрес регистрации')
    phone_number = models.CharField(max_length=10, verbose_name='Номер телефона')
    date_of_born = models.DateField(verbose_name='Дата рождения')
    passport = models.CharField(max_length=13, verbose_name='Паспорт')
    issue_authority = models.TextField(max_length=255, verbose_name="Организация выдавшая паспорт")
    citizenship = models.CharField(max_length=50, verbose_name="Гражданство")
    status = models.BooleanField(null=True, blank=True, verbose_name="Статус заявления")

    college = models.CharField(max_length=120, verbose_name="Предыдущее место обучения")
    specialization = models.CharField(max_length=120, verbose_name='Специальность')
    grade = models.IntegerField(verbose_name='Курс')

    form_of_education = models.CharField(
        verbose_name='Форма обучения',
        max_length=12,
        choices=FORM_OF_EDUCATION_CHOICES,
    )
    base_of_education = models.CharField(
        verbose_name='Основа обучения',
        max_length=10,
        choices=BASE_OF_EDUCATION_CHOICES
    )
    program_of_education = models.TextField(
        verbose_name='Программа обучения',
        max_length=53,
        choices=PROGRAM_OF_EDUCATION_CHOICES
    )

    def get_phone_number(self):
        return f'+7{self.phone_number}'

    def get_education_info(self):
        return f'{self.college} {self.specialization} {self.grade}'

