from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets import serializers
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@csrf_exempt # csrf 예외처리(테스트)
def snippet_list(request): # 모든 코드 스니펫 나열 또는 새로운 스니펫 생성
  if request.method == 'GET':
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method =='POST':
    data = JSONParser().parse(request)
    serializer = SnippetSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.error, status=400)

@csrf_exempt
def snippet_detail(request, pk): # 코드 스니펫 객체 반환, 갱신, 삭제
  try:
    snippet = Snippet.objects.get(pk=pk)
  except Snippet.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET': # retrieve
    serializer = SnippetSerializer(snippet)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT': # update
    data = JSONParser().parse(request)
    serializer = SnippetSerializer(snippet, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.error, status=400)

  elif request.method == 'DELETE':
    snippet.delete()
    return HttpResponse(status=204)




