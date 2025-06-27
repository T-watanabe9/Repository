from django.db import models
from django.contrib import admin

# Create your models here.


class Race(models.Model):
    name = models.CharField(max_length=10)
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
    race = models.ManyToManyField(Race, related_name='races')
    effect_text = models.TextField(blank=True, null=True)
    symbol = models.CharField(max_length=10 ,blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)
    explain = models.TextField(blank=True, null=True)
    priority = models.PositiveIntegerField(default=0, editable=False, db_index=True, verbose_name="move")

    # 並べ替え用。
    class Meta:
        ordering = ['priority'] 

    def __str__(self):
        return f"{self.id}: {self.name}"
    
    @admin.display(description='priority')
    def get_prio(self):
        return self.priority
    
    