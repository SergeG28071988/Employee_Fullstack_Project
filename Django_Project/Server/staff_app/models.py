from django.db import models

# Create your models here.

class Employee(models.Model):
    photo = models.ImageField(upload_to='uploads/images',
                              help_text="Введите фото",
                              verbose_name="Фото сотрудника",
                              null=False, blank=False)  
    full_name = models.CharField(max_length=100, verbose_name='ФИО', null=False, blank=False) 
    position = models.CharField(max_length=100, verbose_name="Должность", null=False, blank=False)
    department = models.CharField(max_length=100, verbose_name="Отдел", null=False, blank=False)
    salary = models.DecimalField(verbose_name="Оклад", max_digits=10, decimal_places=2)
    date_hired = models.DateField(verbose_name="Дата приема на работу", null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"