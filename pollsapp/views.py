from django.shortcuts import render
from .models import Question, Choice

# Create your views here.


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'index.html', context)


def vote(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    context = {
        'question': question,
        'options': options
    }

    # if request.method == 'POST':
    #     inputvalue = request.POST['choice']
    #     selection_option = options.get(id=inputvalue)
    #     selection_option.vote += 1
    #     selection_option.save()

    return render(request, 'vote.html', context)


def result(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    context = {
        'question': question,
        'options': options
    }

    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 1
        selection_option.save()

    return render(request, 'result.html', context)
