from django.test import TestCase
from .models import Question #test할 모델 속 class를 import
from django.utils import timezone
import datetime
from django.urls import reverse

# # def test_something(self):
# #     # 1. 테스트할 객체를 생성하고
# #     객체 = YourModel(속성)
			
# # 	# 2. 테스트할 메서드를 실행하고
# #     결과 = 객체.메서드()
			
# # 	# 3. 결과가 기대값과 같은지 확인
# #     self.assertEqual(결과, 기대값)

def create_question(question_text, days): #이 공동 유틸을 쓰지 않는다면 #polls/tests.py에서 직접 일일이 작성 필요 (자동화)
    """
    days만큼 현재 시각에서 더하거나 빼서 pub_date를 설정한 Question 생성
    (days > 0 → 미래 / days < 0 → 과거)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create (question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase): #yourModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):

        # 미래 날짜의 질문은 최근 게시된 것이 아니므로 False를 반환해야 함

        time = timezone.now() + datetime.timedelta(days=30) # time 속성변수 = 현재시간 + 30일
        future_question = Question(pub_date=time) #question 속성함수 => 속성변수 = 함수(게시일 = 30일 이후) / question은 Question 모델의 인스턴스이므로 모델값과 다름
        self.assertIs (future_question.was_published_recently(), False) #30일 이후의 게시된 글이 최근에 게시된 글이냐?  아니오라는 예상값 만약 true라면 오류 발생.

    def test_was_published_recently_with_old_question(self):

        # 1일 넘은 과거 질문은 최근 게시된 것이 아니므로 False를 반환해야 함

        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs
        (old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        1일 이내의 질문은 최근 게시된 것이므로 True를 반환해야 함
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


# 뷰 테스트: IndexView (질문 목록 페이지)
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        질문이 하나도 없을 경우, No polls are available.
        메시지를 출력해야 함
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        과거 질문은 목록 페이지에 보여야 함
        """
        question = create_question("Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question])

    def test_future_question(self):
        """
        미래 질문은 목록 페이지에 표시되지 않아야 함
        """
        create_question("Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        과거와 미래 질문이 모두 존재해도 목록에는 과거 질문만 표시되어야 함
        """
        past_question = create_question("Past question.", days=-30)
        create_question("Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"], [past_question]
        )

    def test_two_past_questions(self):
        """
        여러 개의 과거 질문이 있을 경우, 최신 순으로 모두 표시되어야 함
        """
        question1 = create_question("Past question 1.", days=-30)
        question2 = create_question("Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )


# 뷰 테스트: DetailView (질문 상세 페이지)
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        미래 질문의 상세 페이지는 접근할 수 없고, 404 오류가 발생해야 함
        """
        future_question = create_question("Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        과거 질문의 상세 페이지는 정상적으로 접근되어야 하고, 질문 내용이
        표시되어야 함
        """
        past_question = create_question("Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)