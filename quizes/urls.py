from django.urls import path
from .views import (
    quiz_view,
    quiz_detail_view,
    quiz_data_view,

)

app_name = 'quizes'

urlpatterns = [
    path('', quiz_view, name = 'home'),
    path('quiz/<int:pk>/', quiz_detail_view, name = 'quiz_detail'),
    path('quiz/<int:pk>/data', quiz_data_view, name = 'quiz_data'),
    
    
]