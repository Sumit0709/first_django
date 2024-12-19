from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }

    return render(request, "polls/index.html", context)

def home(request):
    return HttpResponse("Hello, world. You're at the HOME page.")


# Questions related views

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        choices = Choice.objects.all().filter(question_id=question.id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question, "choices": choices})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)