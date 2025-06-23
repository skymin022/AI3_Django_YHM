from django.db import models

# Create your models here.
class Todo(models.Model):
    STATUS_CHOICES = [
        ('wait', '대기'),
        ('ing', '진행'),
        ('done', '완료'),
    ]
    no = models.AutoField(primary_key=True,)     # 자동 증가 필드(PK)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='wait')
    is_completed = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # 상태에 따라 완료 여부 자동 조정
        self.is_completed = self.status == 'done'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} : {self.get_status_display()}"