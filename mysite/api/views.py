from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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


# ------------------------------------------------------------- #
# ------------------------ READ/UPDATE ------------------------ #
# ------------------------------------------------------------- #
@csrf_exempt
def get_tasks(request):

    if request.method == "GET":
        """curl -i http://localhost:5000/api/tasks"""
        return JsonResponse({'tasks': tasks})

    elif request.method == "POST":
        """curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:8000/api/tasks/"""  # noqa
        request_json_body = json.loads(request.body)
        if not request_json_body or 'title' not in request_json_body:
            return JsonResponse({'error': 'null'})
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': request_json_body['title'],
            'description': request_json_body.get("description", ""),
            'done': False
                }
        tasks.append(task)
        return JsonResponse({'task': task})


def get_task(request, task_id):
    """curl -i http://localhost:8000/api/tasks/3"""
    task = [task for task in tasks if task_id == task['id']]
    if len(task) == 0:
        return JsonResponse({'error': 'Not Found'})
    return JsonResponse({'task': task[0]})

