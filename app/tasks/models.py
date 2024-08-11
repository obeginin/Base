from django.db import models

# создаём модель для Задач
class Task(models.Model):
    # AutoField()- автоназначение для первичного ключа.
    # primary_key=true - задаёт текущее поле в качестве первичного ключа
    id = models.AutoField(primary_key=True)
    CATEGORY_CHOICES = [
        ('EGE_01', 'ЕГЭ_01'),
        ('EGE_02', 'ЕГЭ_02'),
        ('EGE_03', 'ЕГЭ_03'),
        ('EGE_04', 'ЕГЭ_04'),
        ('EGE_05', 'ЕГЭ_05'),
    ]

    resour_CHOICES = [
        ('Demo_24', 'Демо_24'),
        ('Demo_24', 'Демо_24'),
        ('tester_24', 'Пробник_24'),
        ('Base(main)_24', 'Основной_24'),
        ('Statgrad_24', 'Статград_24'),
        ('Kabanov', 'Кабанов'),
        ('Polyakov', 'Поляков'),
    ]
    # аргумент choices создает форму с выбором вариант'''
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name='Категория')
    resour = models.CharField(max_length=20, choices=resour_CHOICES, verbose_name='Ресурс')
    number = models.PositiveIntegerField( verbose_name='№') # положительное целое число
    image = models.ImageField(upload_to='tasks_images/', verbose_name='Задание') # изображение
    solution = models.ImageField(upload_to='tasks_images/' , verbose_name='Решение')
    answer = models.CharField(max_length=20, verbose_name='Ответ') # атрибут verbose_name создает подсказку пользовтелю


# с помощью класса Мета мы ограничиваем уникальность.
# это означает что комбинацией полей категория и номер не могут повторяться в БД
    class Meta:
        unique_together = ('category', 'number')

# Магический метод str возвращает строковое представление любого объекта.
    def __str__(self):
        return f"{self.category}_{self.number}"
        #return self.name'''