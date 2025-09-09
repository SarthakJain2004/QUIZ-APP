from django.db import models
from django.contrib.auth.models import User

# ------------------ Category Model ------------------
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# ------------------ Quiz Model ------------------
class Quiz(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('hold', 'Hold'),
        ('disabled', 'Disabled'),
    )

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ------------------ Question Model ------------------
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.text

# ------------------ Option Model ------------------
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Wrong'})"

# ------------------ Attempt Model ------------------
class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True, blank=True)
    score = models.IntegerField()
    total = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title if self.quiz else 'Deleted Quiz'} ({self.score}/{self.total})"

# ------------------ Answer Model ------------------
class Answer(models.Model):
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True)
    selected_option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Answer by {self.attempt.user.username} for '{self.question}'"
