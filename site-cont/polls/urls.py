from django.urls import path
from . import views

app_name = 'polls' # configura o namespace da aplicação
urlpatterns = [
    # ex:/polls/
    path('',views.index, name='index'),
    # ex:/polls/34/
    #name pode ser usado para refereciar o caminho nos templates
    path('<int:question_id>/',views.detail,name='detail'),
    # ex:/polls/34/results
    path('<int:question_id>/results',views.results,name='results'),
    # ex:/polls/34/vote
    path('<int:question_id>/vote',views.vote,name='vote')
    ]
