from django import forms # библиотека для работы с формами
from .models import Task # импортируем модель Task из файла models

# создаём класс TaskForm, который наследуется от forms.ModelForm.
# ModelForm - класс в Джанго для создаания форм
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task # указываем что форма должна быть связана с моделью Task
        fields = ['category', 'resour', 'number', 'image', 'solution', 'answer'] # задаем поля, которые должны быть включены в форму

# Надо проверить!

        widgets = {
            'category': forms.TextInput(attrs={'placeholder': 'Category'}),
            'number': forms.NumberInput(attrs={'placeholder': 'Number'}),
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
            'answer': forms.Textarea(attrs={'placeholder': 'Answer'}),
        }
'''
        def __init__(self, *args, **kwargs):
            super(TaskForm, self).__init__(*args, **kwargs)
            self.fields['category'].required = False
            self.fields['number'].required = False
            self.fields['image'].required = False
            self.fields['answer'].required = False '''