from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from django.shortcuts import get_object_or_404
from django.db.models import Count

# class 기반)
from django.utils import timezone
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect

# index(최신글 list)
#def index(request):
    # return HttpResponse("Hello, world. You're at the polls index."

#    latest_question_list = Question.objects.order_by("-pub_date")[:5] #- pub_date는 최신순으로 정렬
    # latest_question_list = Question.objects.all() # 전체 조회 
    # latest_question_list = Question.objects.filter(question_text__contains="Python") # question_text에 "Python"이 포함된 질문 조회
    # latest_question_list = Question.objects.filter(pub_date__year=2023) # 2023년에 게시된 질문 조회
    # latest_question_list = Question.objects.filter(pub_date__year=2023, pub_date__month=10) # 2023년 10월에 게시된 질문 조회
    # latest_question_list = Question.objects.filter(pub_date__year=2023, pub_date__month=10, pub_date__day=1) # 2023년 10월 1일에 게시된 질문 조회
    # latest_question_list = Question.objects.exclude(question_text__contains="Python") # question_text에 "Python"이 포함되지 않은 질문 조회
#    context = {"latest_question_list": latest_question_list}#index.html에서 사용할 변수
#    return render(request, "polls/index.html", context)

# detail(상세조회)
#def detail(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, "polls/detail.html", {"question": question})

#def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, "polls/detail.html", {"question": question})

#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, "polls/results.html", {"question": question})

#def vote(request, question_id):
#    return HttpResponse(f"You're voting on question {question_id}.")

# class-based views로 하는 경우(아래) / 위는 function-based views.

# 메인 페이지 (질문 목록)
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


# 질문 상세 페이지
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "question"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

# 결과 페이지
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name = "question"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    

# 투표 처리 로직
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message":"You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1 #f는 필드 / votes 필드를 참조해서 +1 하란 의미
        selected_choice.save() 
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

from django.urls import reverse_lazy

#CRUD(Create, Read, Update, Delete) 뷰 클래스

class QuestionCreateView(generic.CreateView): #생성하기
    model = Question # 1. 질문 및 날짜 생성 필요
    fields = ["question_text", "pub_date"]  # 2. 입력 필드 설정 
    template_name = "polls/question_form.html"  # 3. 템플릿 설정
    success_url = reverse_lazy("polls:index")  # 4. 성공 후 리다이렉트 URL 설정
    
class QuestionUpdateView(generic.UpdateView): #상세보기 및 수정하기
    model = Question  # 1. 질문 모델 지정
    fields = ["question_text", "pub_date"]  # 2. 수정할 필드 설정
    template_name = "polls/question_form.html"  # 3. 템플릿 설정
    success_url = reverse_lazy("polls:index")  # 4. 성공 후 리다이렉트 URL 설정

class QuestionDeleteView(generic.DeleteView):
    model = Question  # 1. 질문 모델 지정
    #fields = ["question_text", "pub_date"]  # 2. 삭제를 할 부분으로 fields 필요 없음
    template_name = "polls/question_form_delete.html"  # 3. 템플릿 설정
    success_url = reverse_lazy("polls:index")  # 4. 성공 후 리다이렉트 URL 설정

#test용_part 8_0
def question_list(request):
    #questions = Question.objects.all()  #쿼리 과부화 유발
    questions = Question.objects.annotate(num_choices=Count('choice'))
    return render(request, 'polls/question_list.html', {'questions': questions}) #쿼리 과부화
