from django.http import HttpResponse, JsonResponse
from flask import jsonify

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_tasks(request):
    """curl -i http://localhost:5000/api/tasks"""
    return JsonResponse({'tasks': tasks})


def get_task(request, task_id):
    """curl -i http://localhost:5000/api/tasks/3"""
    task = [task for task in tasks if task_id == task['id']]
    if len(task) == 0:
        return JsonResponse({'error': 'Not Found'})
    return JsonResponse({'task': task[0]})

