from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import  Response
from next_gap.task import analyze_repo_task
from celery.result import AsyncResult
from rest_framework import status

@api_view(['POST'])
def start_task(request):
    try:
        data = request.data
        repo_url = data.get('repo_url')
        pr_number = data.get('pr_number')
        github_token = data.get('github_token')
        
        if not repo_url or not pr_number:
            return Response({
                "error": "Missing required fields: repo_url and pr_number"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        task = analyze_repo_task.delay(repo_url, pr_number, github_token)
        
        return Response({
            "task_id": task.id,
            "status": "Task Started"
        })
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def Task_status_view(request, task_id):
    try:
        result = AsyncResult(task_id)
        response = {
            "task_id": task_id,
            "status": result.state,
            "result": result.result if result.ready() else None
        }
        return Response(response)
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

