#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Quiz, Question, Option, UserAnswer
from .forms import QuizForm, QuestionForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.db.models import Max, Subquery
from django.views.generic.edit import FormView
from django import forms
from django.db import transaction
from io import StringIO
import csv

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz_list.html'
    context_object_name = 'quizzes'

class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quiz_detail.html'
    context_object_name = 'quiz'

@method_decorator(login_required, name='dispatch')
class QuizDeleteView (DeleteView):
    model = Quiz
    template_name = 'quiz_delete.html'
    success_url = reverse_lazy('quiz_list')

from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class OptionCreateView(CreateView):
    model = Option
    fields = ['question', 'text', 'is_correct']
    template_name = 'option_create.html'

    def get_success_url(self):
        question_id = self.kwargs['question_id']
        return reverse_lazy('question_detail', kwargs={'pk': question_id})

    def form_valid(self, form):
        form.instance.question = Question.objects.get(pk=self.kwargs['question_id'])
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class OptionDeleteView(DeleteView):
    model = Option
    template_name = 'option_delete.html'

    def get_success_url(self):
        question_id = self.object.question_id
        return reverse_lazy('question_detail', kwargs={'pk': question_id})

@method_decorator(login_required, name='dispatch')
class QuizCreateView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'quiz_create.html'

    def get_success_url(self):
        return reverse('quiz_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'
    context_object_name = 'question'

@method_decorator(login_required, name='dispatch')
class QuestionDeleteView (DeleteView):
    model = Question
    template_name = 'question_delete.html'

    def get_success_url(self):
        return reverse('quiz_detail', kwargs={'pk': self.object.quiz.pk})

@method_decorator(login_required, name='dispatch')
class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question_create.html'

    def form_valid(self, form):
        form.instance.quiz = Quiz.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quiz_pk'] = self.kwargs.get('pk')
        return context

    def get_success_url(self):
        return reverse('question_detail', kwargs={'pk': self.object.pk})

class CSVImportForm(forms.Form):
    csv_file = forms.FileField()

@method_decorator(login_required, name='dispatch')
class ImportQuizzesView(FormView):
    template_name = 'import_quizzes.html'
    form_class = CSVImportForm
    success_url = reverse_lazy('quiz_list')

    def form_valid(self, form):
        csv_file = form.cleaned_data['csv_file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = StringIO(data_set)
        next(io_string)

        with transaction.atomic():
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                title = column[0].strip()
                description = column[1].strip()
                question_text = column[2].strip()
                option_text = column[3].strip()
                is_correct_text = column[4].strip().replace('"', '').lower()
                is_correct = is_correct_text in ('true', '1', 't', 'yes', 'y')

                quiz, _ = Quiz.objects.get_or_create(
                    title=title,
                    defaults={'description': description, 'owner': self.request.user}
                )

                question, _ = Question.objects.get_or_create(
                    text=question_text,
                    quiz=quiz
                )

                Option.objects.create(
                    question=question,
                    text=option_text,
                    is_correct=is_correct
                )

        return super().form_valid(form)

@login_required
def attempt_quiz(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = quiz.questions.all()

    if request.method == 'POST':
        for question in questions:
            selected_option_id = request.POST.get(str(question.id))
            is_correct = False
            # The selected_option can now be set to None without violating NOT NULL constraints.
            selected_option = None if not selected_option_id else Option.objects.get(id=selected_option_id)

            if selected_option_id:
                is_correct = selected_option.is_correct

            UserAnswer.objects.create(
                user=request.user,
                question=question,
                selected_option=selected_option,  # Can be None
                is_correct=is_correct
            )
        return redirect('quiz_results', pk=quiz.pk)

    context = {
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'attempt_quiz.html', context)

@login_required
def quiz_results(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    latest_answers = UserAnswer.objects.filter(
        user=request.user,
        question__quiz=quiz
    ).values('question').annotate(
        latest_id=Max('id')
    ).values('latest_id')

    latest_user_answers = UserAnswer.objects.filter(
        id__in=Subquery(latest_answers)
    )

    score = sum(answer.is_correct for answer in latest_user_answers)
    user_answers = UserAnswer.objects.filter(
        id__in=latest_user_answers.values('id')
    ).order_by('question')

    context = {
        'quiz': quiz,
        'user_answers': user_answers,
        'score': score,
    }

    return render(request, 'quiz_results.html', context)
