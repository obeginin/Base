from django import forms # библиотека для работы с формами
from .models import Task # импортируем модель Task из файла models

# создаём класс TaskForm, который наследуется от forms.ModelForm.
# ModelForm - класс в Джанго для создаания форм
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task # указываем что форма должна быть связана с моделью Task
        fields = ['category', 'resour', 'number', 'image', 'solution', 'answer'] # задаем поля, которые должны быть включены в форму