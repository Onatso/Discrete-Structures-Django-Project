from django.urls import path
# Импортируем созданное нами представление
from .views import *



urlpatterns = [
   path('', TaskList.as_view(),name = 'task_list'),

   path('<int:pk>', TaskDetail.as_view(),name = 'task_detail'),

   path('achievements/', AchievementList.as_view(),name = "achievement_list"),

   path('<int:pk>/comments',CommentList.as_view(),name = "comment_list"),

   path('<int:pk>/comments/<int:comment_pk>',CommentDetail.as_view(),name = "comment_detail"),

   path('<int:pk>/comments/<int:comment_pk>/update', CommentUpdate.as_view(), name = "comment_update"),

   path('comment/answer/', commentAnswerView, name='comment_answer'),

]


