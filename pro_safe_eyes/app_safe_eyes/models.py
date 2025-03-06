from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.

# コメントモデル。
class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)   # コメントID。主キー。
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE) # 外部キー。デフォルトユーザーモデル。
    #category = models.CharField(max_length=255) # コメントカテゴリ。不要かも。
    content = models.TextField(null=True , blank=True) # コメント内容。
    datetime = models.DateTimeField(default=timezone.now) # 投稿した時刻。
    # choices用リスト。
    CONDITION_CHOICES = [
        (1, "良い"),
        (2, "普通"),
        (3, "悪い"),
    ]
    physical_health = models.IntegerField(choices=CONDITION_CHOICES, default=2) # 身体の調子。
    mental_health = models.IntegerField(choices=CONDITION_CHOICES, default=2) # メンタルの調子。
     
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
         return reverse('home')