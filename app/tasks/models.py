# tasks/models.py в данном файле описывем модели для хранения "задач" в базе данных
from django.db import models
from django.core.exceptions import ValidationError # обработчик ошибок
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


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
        ('EGE_06', 'ЕГЭ_06'),
        ('EGE_07', 'ЕГЭ_07'),
        ('EGE_08', 'ЕГЭ_08'),
    ]

    resour_CHOICES = [
        ('Demo_24', 'Демо_24'),
        ('Demo_23', 'Демо_23'),
        ('tester_24', 'Пробник_24'),
        ('Base(main)_24', 'Основной_24'),
        ('Statgrad_24', 'Статград_24'),
        ('Kabanov', 'Кабанов'),
        ('Polyakov', 'Поляков'),
        ('Other', 'Другое'),
    ]
    # аргументы и атрибуты:
    # blank=True указывает, что поле может оставаться пустым в формах, а также не будет требоваться для заполнения.
    # null=True покывет что поле может хранить NULL в базе данных
    # choices=CATEGORY_CHOICES создает форму с выбором вариант из списка CATEGORY_CHOICES
    # verbose_name дает название полям
    # unique=True гарантирует что зачение в БД будет унииальным
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name='Категория')
    resour = models.CharField(max_length=20, choices=resour_CHOICES, verbose_name='Ресурс')
    number = models.PositiveIntegerField(unique=True, verbose_name='№') # положительное целое число
    image = models.ImageField(upload_to='tasks_images/', verbose_name='Задание', blank=True, null=True) # изображение
    solution = models.ImageField(upload_to='tasks_images/' , verbose_name='Решение', blank=True, null=True)
    answer = models.CharField(max_length=20, verbose_name='Ответ', blank=True, null=True) # атрибут verbose_name создает подсказку пользовтелю


# с помощью класса Мета мы ограничиваем уникальность.
# unique_together  означает что комбинацией полей категория и номер не могут повторяться в БД
# ordering  Задает порядок сортировки объектов при выполнении запросов к базе данных.
    class Meta:
        unique_together = ('category', 'number')
        ordering = ['category', 'number'] # сначала будет сортировка по category, а затем по number внутри каждой категории.

# Фунция котоая проверяет: если мользователь ввел число не 4-х значное, то очистит форму
    def clean(self):
        if self.number < 1000 or self.number > 9999:
            raise ValidationError(_('Номер должен быть 4-х значный!'))

# Магический метод str возвращает строковое представление любого объекта.
    def __str__(self):
        return f"{self.category}_{self.number}"
        #return self.name'''

# Связывем пользователей и задачи с пощю внешних ключей

class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks', null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_solutions', null=True)
    solution_user = models.ImageField(upload_to='tasks_images/' , verbose_name='Решение пользователя', null=True)
    answer_user = models.CharField(max_length=20, verbose_name='Ответ пользователя', null=True)
    completed = models.BooleanField(default=False)  # Добавим поле для отслеживания выполнения задания

    class Meta:
        unique_together = ('user', 'task')  # Уникальность задания для каждого пользователя
    def __str__(self):
        return f'{self.user.login} - {self.task.number}'
