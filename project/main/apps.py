from django.apps import AppConfig


# class MainConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'main'


class AchievementConfig(AppConfig):
    # нам надо переопределить метод ready, чтобы при готовности нашего приложения импортировался
    # модуль со всеми функциями обработчиками

    name = 'main'

    def ready(self):
        import main.signals