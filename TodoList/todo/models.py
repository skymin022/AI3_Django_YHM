from django.db import models

# Create your models here.
class Todo(models.Model):
    no = models.AutoField(primary_key=True,)     # 자동 증가 필드(PK)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "완료" if self.is_completed else "미완료"
        return f"{self.title} : {status}"