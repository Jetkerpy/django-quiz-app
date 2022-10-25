from django.shortcuts import render
from .models import Quiz
from django.http import JsonResponse
# Create your views here.




def quiz_view(request):
    quizes = Quiz.objects.all()

    context = {
        'quizes': quizes
    }
    return render(request, 'home.html', context)



def quiz_detail_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    quiz = Quiz.objects.get(pk = pk)



    context = {
        'quiz': quiz
    }

    return render(request, 'quiz_detail.html', context)




def quiz_data_view(request, *args, **kwargs):
    quiz_pk = kwargs.get('pk')
    quiz = Quiz.objects.get(pk = quiz_pk)

    questions = [{str(q): [a.text for a in q.get_answers()]} for q in quiz.get_questions()]
 

    return JsonResponse({
        'data': questions,
        'time': quiz.time
    })
   
    
