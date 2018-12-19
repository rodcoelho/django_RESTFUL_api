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
# ------------------------ CREATE/READ ------------------------ #
# ------------------------------------------------------------- #
@csrf_exempt
def get_many_tasks(request):

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


@csrf_exempt
def get_one_task(request, task_id):
    task = [task for task in tasks if task['id'] == task_id]

    if request.method == "GET":
        """curl -i http://localhost:8000/api/tasks/3"""
        if len(task) == 0:
            return JsonResponse({'error': 'Not Found'})
        return JsonResponse({'task': task[0]})

    elif request.method == 'PUT':
        """curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:8000/api/tasks/2"""  # noqa
        request_json_body = json.loads(request.body)

        # -------------- catch mistakes -------------- #
        if len(task) == 0:
            return JsonResponse({'error': 'null'})
        if not request_json_body:
            return JsonResponse({'error': 'null'})
        if 'title' in request_json_body and not isinstance(request_json_body['title'], str):
            return JsonResponse({'error': 'null'})
        if 'description' in request_json_body and not isinstance(request_json_body['description'], str):
            return JsonResponse({'error': 'null'})
        if 'done' in request_json_body and type(request_json_body['done']) is not bool:
            return JsonResponse({'error': 'null'})

        # --------------- update dict --------------- #
        task[0]['title'] = request_json_body.get('title', task[0]['title'])
        task[0]['description'] = request_json_body.get('description', task[0]['description'])
        task[0]['done'] = request_json_body.get('done', task[0]['done'])
        return JsonResponse({'task': task[0]})

    elif request.method == "DELETE":
        """curl -X "DELETE"  http://localhost:8000/api/tasks/1"""  # noqa
        if len(task) == 0:
            return JsonResponse({'error': 'null'})
        tasks.remove(task[0])
        return JsonResponse({'result': True})


