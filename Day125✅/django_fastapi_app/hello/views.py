from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def hello_world(request):
    """Django hello world view"""
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({
            'message': 'Hello World from Django!',
            'framework': 'Django'
        })
    
    context = {
        'message': 'Hello World from Django!',
        'framework': 'Django',
        'endpoints': [
            {'name': 'FastAPI Hello', 'url': '/api/hello'},
            {'name': 'FastAPI Hello with Name', 'url': '/api/hello/jane'},
            {'name': 'FastAPI Docs', 'url': '/docs'},
        ]
    }
    return render(request, 'hello/index.html', context)

def hello_name(request, name):
    """Django hello with name parameter"""
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({
            'message': f'Hello {name} from Django!',
            'framework': 'Django'
        })
    
    context = {
        'message': f'Hello {name} from Django!',
        'name': name,
        'framework': 'Django',
        'endpoints': [
            {'name': 'FastAPI Hello', 'url': '/api/hello'},
            {'name': 'FastAPI Hello with Name', 'url': '/api/hello/jane'},
            {'name': 'FastAPI Docs', 'url': '/docs'},
        ]
    }
    return render(request, 'hello/hello_name.html', context) 