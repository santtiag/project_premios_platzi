from django.shortcuts import render

from django.http import HttpResponse

from polls.models import Question


def index(request):
    questions = Question.objects.all()
    # return HttpResponse(latest_question_list)
    return render(request, "index.html", {'questions': questions})
    
def detail(request, question_id):
    return HttpResponse("Estas viendo la pregunta número: %s" % question_id)

def result(request, question_id):
    return HttpResponse("Estas viendo los resultados de la pregunta número: %s" % question_id)

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta número: {question_id}")
