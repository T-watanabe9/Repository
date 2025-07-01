from django.db import models
from django.contrib import admin

# Create your models here.


class Race(models.Model):
    name = models.CharField(max_length=10)
    order = models.PositiveIntegerField(default=0, db_index=True)
    def __str__(self):
        return self.name

class Card(models.Model):

    id = models.CharField(primary_key=True, max_length=10, editable=False)
    name = models.CharField(max_length=100)
    CATEGORY_CHOICES = [
        ('スピリット', 'スピリット'),
        ('アルティメット', 'アルティメット'),
        ('ブレイヴ', 'ブレイヴ'),
        ('ネクサス', 'ネクサス'),
        ('マジック', 'マジック'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    cost = models.IntegerField()
    reduction_symbol = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=10)
    #race = models.ManyToManyField(Race, blank=True, related_name='races')
    race1 = models.ForeignKey('Race', on_delete=models.SET_NULL, blank=True, null=True, related_name='race1_cards')
    race2 = models.ForeignKey('Race', on_delete=models.SET_NULL, blank=True, null=True, related_name='race2_cards')
    race3 = models.ForeignKey('Race', on_delete=models.SET_NULL, blank=True, null=True, related_name='race3_cards')
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
    
    # 系統を表示するためのメソッド
    @admin.display(description='系統')
    def get_race(self):
        str1 = str(self.race1) if self.race1 else ''
        str2 = ('・' + str(self.race2)) if self.race2 else ''
        str3 = ('・' + str(self.race3)) if self.race3 else ''
        return str1 + str2 + str3
    
    # IDを自動で設定するためのメソッド
    def save(self, *args, **kwargs):
        if not self.id:

            # 色の判別
            if self.color == '赤紫緑白黄青':
                id_initial = 'S'
            elif self.color[0] == '赤':
                id_initial = 'R'
            elif self.color[0] == '紫':
                id_initial = 'P'
            elif self.color[0] == '緑':
                id_initial = 'G'
            elif self.color[0] == '白':
                id_initial = 'W'
            elif self.color[0] == '黄':
                id_initial = 'Y'
            elif self.color[0] == '青':
                id_initial = 'B'

            # カテゴリの判別
            if self.category == 'スピリット':
                id_initial += 'S'
            elif self.category == 'アルティメット':
                id_initial += 'U'
            elif self.category == 'ブレイヴ':
                id_initial += 'B'
            elif self.category == 'ネクサス':
                id_initial += 'N'
            elif self.category == 'マジック':
                id_initial += 'M'

            # コストの2桁表現を追加
            id_initial += f'{self.cost:02d}'

            # 末尾3桁の連番を探す
            count = 1
            while True:
                id_candidate = id_initial + f"{count:03d}"  
                if Card.objects.filter(id=id_candidate).exists():
                    count += 1
                else:
                    self.id = id_candidate
                    break
        super().save(*args, **kwargs)
    
