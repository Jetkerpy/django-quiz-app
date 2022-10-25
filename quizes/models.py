from django.db import models

# Create your models here.

DEFF_CHOICES = (
    ('easy', 'EASY'),
    ('medium', 'MEDIUM'),
    ('hard', 'HARD'),

)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text='Duration of the quiz in minutes')
    required_score_pass = models.IntegerField(help_text="Required score in %")
    difficulty = models.CharField(max_length=6, choices=DEFF_CHOICES)

    def __str__(self):
        return f"{self.pk} --> {self.topic}."


    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions] #related to Question Model



    class Meta:
        verbose_name_plural = 'Quizes'