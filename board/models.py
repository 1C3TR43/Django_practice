from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    writer = models.ForeignKey(User, models.CASCADE, related_name="boards", verbose_name="작성자")
    title = models.CharField(max_length=100, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 시간")
    
    def __str__(self):
        return f"{self.writer.username} : {self.title}"

class Comment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    board = models.ForeignKey(Board, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.comment