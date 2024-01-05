from django.db import models


# Create your models here.

## 게시판
class Board(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)  # 제목
    content =models.TextField(blank=False, null=False)  # 내용
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)  # 첨부파일
    views = models.IntegerField(default=0)  # 조회수
    
    def __str__(self):
        return f'[{self.pk}] {self.title}'
    
    