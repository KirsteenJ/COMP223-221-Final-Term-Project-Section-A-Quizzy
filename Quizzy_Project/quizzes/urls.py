from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuizListView.as_view(), name='quiz_list'),
    path('create/', views.QuizCreateView.as_view(), name='quiz_create'),
    path('<int:pk>/', views.QuizDetailView.as_view(), name='quiz_detail'),
    path('<int:pk>/question/create/', views.QuestionCreateView.as_view(), name='question_create'),
    path('question/<int:question_id>/option/create/', views.OptionCreateView.as_view(), name='option_create'),
    path('<int:pk>/attempt/', views.attempt_quiz, name='attempt_quiz'),
    path('<int:pk>/results/', views.quiz_results, name='quiz_results'),
    path('<int:pk>/delete/', views.QuizDeleteView.as_view(), name='quiz_delete'),
    path('<int:pk>/question/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('question/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name='question_delete'),
    path('question/<int:question_id>/option/<int:pk>/delete/', views.OptionDeleteView.as_view(), name='option_delete'),
    path('import/', views.ImportQuizzesView.as_view(), name='import_quizzes'),
]