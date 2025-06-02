from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from django.shortcuts import get_object_or_404

# index(최신글 list)
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index."

    latest_question_list = Question.objects.order_by("-pub_date")[:5] #- pub_date는 최신순으로 정렬
    # latest_question_list = Question.objects.all() # 전체 조회 
    # latest_question_list = Question.objects.filter(question_text__contains="Python") # question_text에 "Python"이 포함된 질문 조회
    # latest_question_list = Question.objects.filter(pub_date__year=2023) # 2023년에 게시된 질문 조회
    # latest_question_list = Question.objects.filter(pub_date__year=2023, pub_date__month=10) # 2023년 10월에 게시된 질문 조회
    # latest_question_list = Question.objects.filter(pub_date__year=2023, pub_date__month=10, pub_date__day=1) # 2023년 10월 1일에 게시된 질문 조회
    # latest_question_list = Question.objects.exclude(question_text__contains="Python") # question_text에 "Python"이 포함되지 않은 질문 조회
    context = {"latest_question_list": latest_question_list}#index.html에서 사용할 변수
    return render(request, "polls/index.html", context)

# detail(상세조회)
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")