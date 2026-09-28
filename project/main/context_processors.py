from .models import Task
from .views import TaskList

def flatpages_processors(request):
    step = TaskList.paginate_by
    context = {
        'user': request.user,
        'graphs_begin': Task.objects.filter(type="Булевы Функции").count() // step + 1
    }
    return context