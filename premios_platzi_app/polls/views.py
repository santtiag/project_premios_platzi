from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, reverse

from django.http import HttpResponse

from polls.models import Choice, Question


def index(request):
    questions = Question.objects.all()
    return render(request, "polls/index.html", { 'questions': questions })
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", { 'question':question })

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', { 'question': question })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'No elegiste un respuesta',
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
