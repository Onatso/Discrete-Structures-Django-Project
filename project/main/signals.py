#from Tools.demo.mcast import sender
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives,mail_managers
from .models import UserAchievement,Achievement, UserTask,Task, Comment
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from celery import shared_task




@receiver(post_save, sender=UserAchievement)
def notify_users_about_achievement(sender, instance, created, **kwargs):
    if created:
        from .tasks import send_achievement_email
        send_achievement_email.delay(instance.user.id, instance.achievement.id)
        if instance.user.userachievement_set.all().count() == Achievement.objects.all().count() - 1:
            UserAchievement.create_user_achievement(user=instance.user, achievement_name="Платина")


@receiver(post_save,sender = UserTask)
def task_create_signal(sender, instance, created,**kwargs):
    if created:
        if instance.user.usertask_set.all().count() == Task.objects.all().count():
            UserAchievement.create_user_achievement(user= instance.user, achievement_name="И это всё?")


@receiver(post_save,sender = Comment)
def comment_change_signal(sender, instance,created,**kwargs):
    if not created and not instance.was_changed:
        instance.was_changed = True
        instance.save(update_fields = ['was_changed'])