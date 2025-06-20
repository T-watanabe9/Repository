from django.db import models

# Create your models here.
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
    race =  models.CharField(max_length=20, blank=True, null=True)
    effect_text = models.TextField(blank=True, null=True)
    symbol = models.CharField(max_length=10 ,blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)
    explain = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}: {self.name}"
    
    