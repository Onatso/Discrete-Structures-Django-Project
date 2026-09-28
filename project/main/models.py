from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import  redirect, render, reverse
from django.core.validators import FileExtensionValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
#from openid.message import no_default


# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)



Difficult_choices = [
    ('Лёгкий', 'Easy'),
    ('Средний', 'Middle'),
    ('Сложный', 'Difficult')
]

Type_choices = [
    ('Булевы Функции', 'Boolean functions'),
    ('Графы', ' Graphs'),
]

class Task(models.Model):
    author = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(unique=True,null = False,)
    level = models.CharField(choices= Difficult_choices,default='Лёгкий',max_length=8)
    type = models.CharField(choices = Type_choices, default = 'Булевы Функции',max_length=20, db_index=True)


    def get_absolute_url(self):
        return  '/' + str(self.id)

    def __str__(self):
        return f'{self.type}: Задача "{self.title}"'

    class Meta:
        ordering = ['pk']


class UserTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete = models.CASCADE)
    solved_count = models.PositiveIntegerField(default=1)
    last_solved = models.DateTimeField(auto_now_add = True)


    class Meta:
        ordering = ['-last_solved']

        constraints = [
            models.UniqueConstraint(
                fields = ["user", "task"],
                name = "unique_user_task"
            )
        ]

    def increment_solve_count(self):
        self.solved_count += 1
        self.save()




    def __str__(self):
        return f'Пользователь {self.user.username} решил задачу "{self.task.title}"'


class Achievement(models.Model):
    name = models.CharField(max_length = 128,unique=True,default="Название достижения")
    description = models.TextField(unique=True,default="Описание достижения")
    image = ProcessedImageField(
        upload_to = "achievements/images/",
        verbose_name="Изображение для достижения",
        processors=[ResizeToFill(64, 64)],
        format='WEBP',
        options={'quality': 90},
        null=True,
    )
    copy_image_url = models.URLField(
        null=True,
        default='',
        verbose_name='url-ссылка на изображение',
        unique= False,
        help_text='Введите url-адрес изображения(если есть)',
    )

    def __str__(self):
        return f'Достижение "{self.name}"'


class UserAchievement(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date']
        constraints = [
            models.UniqueConstraint(
                fields = ['user','achievement'],
                name = 'unique_user_achievement'
            )
        ]

    def __str__(self):
        return f'Пользователь {self.user.username} имеет достижение "{self.achievement.name}"'

    @staticmethod
    def create_user_achievement(user=None,achievement_name=None):
        achiev = Achievement.objects.get(name = achievement_name)
        if achiev and user and user.is_authenticated:
            UserAchievement.objects.get_or_create(user = user,achievement = achiev)
            print(UserAchievement.objects.count())
            #if UserAchievement.objects.count() == Achievement.objects.all().count() - 1:
                #UserAchievement.create_user_achievement(user=user,achievement_name="Платина")


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    change_time = models.DateTimeField(auto_now=True)
    text = models.TextField(null = False,default="Текст комментария",max_length=1000)
    was_changed = models.BooleanField(default=False)
    teacher_answer = models.CharField(blank = True,max_length=500)
    admin_answer = models.CharField(blank = True,max_length=500)


    def __str__(self):
        return f'Комментарий от {self.user}: {self.text[:50]}...'


