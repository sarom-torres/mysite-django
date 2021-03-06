#from django import template
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
#from django.http.response import Http404
# #from django.template import context, loader

class IndexView(generic.ListView): # ListView abstrai o conceito de exibir uma lista de objetos
    template_name = 'polls/index.html' #usar um nome de template em vez de auto gerar um.
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #retorna as ultima 5 questões publicadas
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView): # DetailView abstrai o conceito de exibir uma página de detalhe para um tipo particular de objeto
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html' 

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))