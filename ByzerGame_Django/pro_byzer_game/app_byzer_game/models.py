from django.db import models
from django.contrib import admin

# Create your models here.


class Race(models.Model):
    name = models.CharField(max_length=10)
    order = models.PositiveIntegerField(default=0, db_index=True)
    def __str__(self):
        return self.name

class Card(models.Model):

    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    CATEGORY_CHOICES = [
        ('spirit', 'スピリット'),
        ('ultimate', 'アルティメット'),
        ('brave', 'ブレイヴ'),
        ('nexus', 'ネクサス'),
        ('magic', 'マジック'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    cost = models.IntegerField()
    reduction_symbol = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=10)
    race = models.ManyToManyField(Race, blank=True, related_name='races')
    effect_text = models.TextField(blank=True, null=True)
    symbol = models.CharField(max_length=10 ,blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)
    explain = models.TextField(blank=True, null=True)
    priority = models.PositiveIntegerField(db_index=True, verbose_name="move")

    # 並べ替え用。
    class Meta:
        ordering = ['priority'] 
    def __str__(self):
        return f"{self.id}: {self.name}"
    
    # priorityを表示するためのメソッド
    @admin.display(description='priority')
    def get_prio(self):
        return self.priority
    
    # priorityを自動で設定するためのメソッド
    def save(self, *args, **kwargs):
        if not self.priority:
            #max_priority = self.__class__.objects.aggregate(models.Max('priority'))['priority__max']
            self.priority = 10
        super().save(*args, **kwargs)
    
    
