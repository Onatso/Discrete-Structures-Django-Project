from .models import *
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,View
from datetime import datetime
from django.shortcuts import redirect,render,reverse,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import check_password

from .tasks_solutions import boolean_solutions

from .tasks_solutions.graphs_solutions import (
    graphs_task1, graphs_task2, graphs_task3,
    graphs_task4, graphs_task5,graphs_task6,
    graphs_task7, graphs_task8, graphs_task9,
    graphs_task10, graphs_task11, graphs_task12

)




from pathlib import Path

main_dir = Path(__file__).parent

graphs_solutions_dir = main_dir / "tasks_solutions" / "graphs_solutions"


# Create your views here.

class TaskList(ListView):

    model = Task

    template_name = 'task_list.html'

    context_object_name = 'Tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_request = self.request.GET
        context['date'] = datetime.utcnow()
        return context

    paginate_by = 3


class TaskDetail(DetailView,):
    model = Task

    ordering = '-pk'

    template_name = "template_title.html"

    context_object_name = 'task'

    templates_root_dir = "tasks_details/"


    def get(self, request, *args, **kwargs):
         obj = self.get_object()

         name = obj.title

         if name == "Булева функция от n аргументов":
            self.set_template_name("boolean_functions/1/1.html")

         elif name == "Остаточная функция":
             self.set_template_name("boolean_functions/2/2.html")


         elif name == "Вектор функции":
             self.set_template_name("boolean_functions/3/3.html")

         elif name == "Игра - имя  функции":
             self.set_template_name("boolean_functions/4/4.html")
             print(request.user.is_authenticated)

         elif name == "Существенные и фиктивные переменные":
             self.set_template_name("boolean_functions/5/5.html")

         elif name == "Игра - ДНФ":
             self.set_template_name("boolean_functions/6/6.html")

         elif name == "Игра - КНФ":
             self.set_template_name("boolean_functions/7/7.html")

         elif name == "СДНФ":
             self.set_template_name("boolean_functions/8/8.html")

         elif name == "СКНФ":
             self.set_template_name("boolean_functions/9/9.html")

         elif name == "Предполные классы б.ф":
             self.set_template_name("boolean_functions/10/10.html")

         elif name == "Полные системы б.ф":
             self.set_template_name("boolean_functions/11/11.html")

         elif name == "Алгоритм ДНФ":
             self.set_template_name("boolean_functions/12/12.html")



         elif name == "Обход графа в глубину":

             self.set_template_name("graphs/1/1.html")

         elif name == "Правильность обхода в глубину":

             self.set_template_name("graphs/2/2.html")

         elif name == "Обход графа в ширину":

             self.set_template_name("graphs/3/3.html")

         elif name == "Правильность обхода в ширину":

             self.set_template_name("graphs/4/4.html")

             print(request.user.is_authenticated)

         elif name == "Число компонент связности графа":

             self.set_template_name("graphs/5/5.html")

         elif name == "Правильность числа компонент связности":

             self.set_template_name("graphs/6/6.html")

         elif name == "Минимальное оставное дерево":

             self.set_template_name("graphs/7/7.html")

         elif name == "Нахождение кратчайших путей от вершины":

             self.set_template_name("graphs/8/8.html")

         elif name == "Матрица кратчайших путей":

             self.set_template_name("graphs/9/9.html")

         elif name == "Кодирование Прюфера":

             self.set_template_name("graphs/10/10.html")

         elif name == "Декодирование Прюфера":

             self.set_template_name("graphs/11/11.html")

         elif name == "Раскраска графа":

             self.set_template_name("graphs/12/12.html")

         return super().get(request,*args,**kwargs)

    def set_template_name(self,html_name):
        self.template_name = self.templates_root_dir + html_name


    def post(self,request,*args,**kwargs):
        Post = self.request.POST
        task = self.get_object()
        name = task.title
        print(name)

        if name == "Булева функция от n аргументов":
            n = int(Post.get('hiddenFormInput1'))
            ans = boolean_solutions.task1(n)
            return JsonResponse({'ans': ans})

        elif name == "Остаточная функция":
            vector = Post['vector']
            zeroOrOne = int(Post['zeroOrOne'])
            argument = int(Post['argument'])
            ans = boolean_solutions.task2(vector,argument,zeroOrOne)
            return JsonResponse({'ans': ans})

        elif name == "Вектор функции":
            zero = Post.get('input1')
            one = Post.get('input2')
            var = int(Post.get('input3'))
            ans = boolean_solutions.task3(zero,one,var)
            return JsonResponse({'ans': ans})

        elif name == "Игра - имя  функции":
            is_first_achievement = Post['is_first_achievement']
            if is_first_achievement:
                UserAchievement.create_user_achievement(user = request.user,achievement_name="Вы были приглашены на кафедру")

        elif name == "Существенные и фиктивные переменные":
            binary_string = Post["binary_string"]
            user_answer = Post["user_answer"]
            print(user_answer,boolean_solutions.task5(binary_string))
            ans = (user_answer == boolean_solutions.task5(binary_string))
            if ans:
                UserAchievement.create_user_achievement(user=request.user, achievement_name="Морфеусу нравится ваш выбор")
                user_task = UserTask.objects.filter(user = request.user,task=task).first()
                if user_task:
                    user_task.increment_solve_count()
                else:
                    UserTask.objects.create(user = request.user,task=task)


            return JsonResponse({'ans': ans})

        elif name == "Игра - ДНФ":
            if "input_password" in self.request.POST.keys():
                input_password = self.request.POST.get("input_password")
                passw_current_or_not = False
                if check_password(input_password,self.request.user.password):
                    passw_current_or_not = True
                return JsonResponse({"passw_current_or_not" : passw_current_or_not})
            if "binary_function" in Post and "user_dnf" in Post:
                bin_func = Post["binary_function"]
                user_dnf = Post["user_dnf"]
                is_dnf = boolean_solutions.task6(bin_func,user_dnf)
                if is_dnf and is_dnf != 'Error: invalid expression':
                    UserAchievement.create_user_achievement(user=request.user, achievement_name="on the half way to become a linuxoid")
                return JsonResponse({'is_dnf' : is_dnf})


        elif name == "Игра - КНФ":
            func = Post.get('function')
            knf_or_not = Post.get('knf_or_not')
            res = boolean_solutions.task7(func,knf_or_not)
            if res:
                UserAchievement.create_user_achievement(user=request.user,achievement_name="Оценка - отлично!")
            return JsonResponse({'res' : res})

        elif name == "СДНФ":
            if "IsAchiev" in Post.keys():
                UserAchievement.create_user_achievement(user=request.user,achievement_name="А не много хочешь?")
            else:
                vector = Post.get("vector")
                return JsonResponse({'res': boolean_solutions.task8(vector)})

        elif name == "СКНФ":
            vector = Post.get("vector")
            res = boolean_solutions.task9(vector)
            return JsonResponse({'res':res })


        elif name == "Предполные классы б.ф":
            bin = Post["bin"]
            user_ans = Post["user_ans"]
            print(user_ans)
            right_or_not = user_ans == boolean_solutions.task10(bin)
            if right_or_not:
                user = request.user
                user_task = UserTask.objects.filter(user = request.user,task=task).first()
                if user_task:
                    user_task.increment_solve_count()
                    user_task.save()
                    if user_task.solved_count == 32:
                        UserAchievement.create_user_achievement(user=user, achievement_name="Ад для эпилептика")
                else:
                    UserTask.objects.create(user = user, task = task)

            return JsonResponse({'right_or_not':right_or_not })


        elif name == "Полные системы б.ф":
            bin_mas = list(Post.get("input1").split(","))
            choice = Post.get("input2")
            right_or_not = choice == boolean_solutions.task11(bin_mas)
            if right_or_not:
                UserAchievement.create_user_achievement(user=request.user,achievement_name="Неужели я хуже десятой?")
            return JsonResponse({'right_or_not':right_or_not })

        elif name == "Алгоритм ДНФ":
            bin_function = Post['bin_function']
            return JsonResponse({'min_dnf' : boolean_solutions.task12(bin_function)})



        elif name == "Обход графа в глубину":
            string = Post.get("string")
            path = path = graphs_task1.task1(graphs_task1.to_zero_index(string))
            return JsonResponse({"path": path})

        elif name == "Правильность обхода в глубину":
            item_sequence = Post["item_sequence"]
            way = Post["way"]
            right_or_not = graphs_task2.task2(graphs_task2.to_zero_index(item_sequence), list(map(int, way.split())))
            return JsonResponse({"right_or_not": right_or_not})

        elif name == "Обход графа в ширину":
            value = Post.get("value")
            path = graphs_task3.task3(graphs_task3.to_zero_index(value))
            return JsonResponse({"path": path})

        elif name == "Правильность обхода в ширину":
            item_count = Post["item_count"]
            path = Post["path"]
            right_or_not = graphs_task4.task4(graphs_task4.to_zero_index(item_count), list(map(int, path.split())))
            return JsonResponse({"right_or_not": right_or_not})


        elif name == "Число компонент связности графа":

            edges_count = Post.get("edges_count")
            components_count = graphs_task5.task56(graphs_task5.to_zero_index(edges_count))
            return JsonResponse({"components_count": components_count})

        elif name == "Правильность числа компонент связности":
            components_count = Post["components_count"]
            right_components_count = graphs_task6.task56(graphs_task6.to_zero_index(components_count))
            return JsonResponse({"right_components_count": right_components_count})


        elif name == "Минимальное оставное дерево":

            print(1)

        elif name == "Нахождение кратчайших путей от вершины":

            print(1)

        elif name == "Матрица кратчайших путей":

            print(1)

        elif name == "Кодирование Прюфера":

            print(1)

        elif name == "Декодирование Прюфера":

            print(1)

        elif name == "Раскраска графа":

            print(1)


        return HttpResponse('Приветствуем на BoolPlayGround!')


class AchievementList(ListView):
    model = Achievement
    template_name = "achievements.html"
    ordering = "id"
    context_object_name = "achievements"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        all_user_achievements = user.userachievement_set.all()
        context['user_achievements'] = [user_achievement for user_achievement in all_user_achievements]
        all_achievements = context['achievements']
        users_all_count = User.objects.all().count()

        achievement_percents = {
            achievement.id : round(100 * achievement.userachievement_set.all().count() / users_all_count,2) for achievement in all_achievements
        }
        for achievement in all_achievements:
            print(achievement.userachievement_set.all().count())
        context['achievement_percents'] = achievement_percents
        return context


class CommentList(ListView):

    model = Comment

    template_name = "sign/comments.html"

    context_object_name = "Comments"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request

        need_task_id = int(request.path.split('/')[1])
        need_task = Task.objects.get(id = need_task_id)
        need_comments = need_task.comment_set.all().order_by("-change_time")
        context['task'] = need_task
        context['comments'] = need_comments
        if not request.user.is_authenticated:
            context['user_is_teacher'] = False
        else:
            context['user_is_teacher'] = Teacher.objects.filter(user = request.user).exists()
        return context

    def get(self,request,*args,**kwargs):
        return super().get(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        POST = self.request.POST
        comment_text = POST.get('input')
        task_id = int(POST['task_id'])
        task = Task.objects.get(id = task_id)
        new_comment = Comment(user = request.user, task = task, text = comment_text)
        new_comment.save()
        return redirect(request.path)


class CommentDetail(DetailView):
    model = Comment
    template_name = "sign/comment_detail.html"

    def get_object(self, queryset=None):
        comment_pk = self.kwargs.get("comment_pk")
        return get_object_or_404(
            Comment,
            pk = comment_pk
        )

    def post(self,request,*args,**kwargs):
        Post = request.POST
        current_comment = self.get_object()
        if current_comment:
            current_comment.delete()
            print(current_comment.pk)
            print(request.POST.get("comment_id"))
            return JsonResponse({
                "success": True
            })
        else:
            return JsonResponse({
                "success": False
            })




class CommentUpdate(UpdateView):
    model = Comment

    fields = ["text"]

    template_name = "sign/comment_update.html"




    def get_object(self, queryset=None):
        # Получаем и task_pk и comment_pk из URL
        task_pk = self.kwargs.get('pk')
        comment_pk = self.kwargs.get('comment_pk')

        print(comment_pk)
        return get_object_or_404(
            Comment,
            pk=comment_pk,
        )


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object.text)
        form = self.get_form()
        if form.is_valid():
            form.save()
            return JsonResponse({
                "success": True,
                "text": self.object.text,
                "id": self.object.id
            })

        return JsonResponse({
            "success": False,
            "errors": form.errors.as_json()
        })


@login_required()
def commentAnswerView(request):

    comment_id = request.POST.get('comment_id')
    print(request.POST)
    answer_type = request.POST.get('answer_type')
    answer_text = request.POST.get('answer_text')
    try:
        comment = Comment.objects.get(id=comment_id)
        print(comment)
        if answer_type == 'teacher':
            comment.teacher_answer = answer_text
        elif answer_type == 'admin':
            comment.admin_answer = answer_text
        print(answer_type)
        comment.save()
        return JsonResponse({'success': True})
    except Comment.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Комментарий не найден'}, status=404)
