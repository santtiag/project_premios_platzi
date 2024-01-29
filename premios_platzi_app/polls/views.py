from django.http import HttpResponse

def index(request):
    return HttpResponse('Esta en la página principal de Premios Platzi App')

def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta número: {question_id}")

def result(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta número: {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta número: {question_id}")
