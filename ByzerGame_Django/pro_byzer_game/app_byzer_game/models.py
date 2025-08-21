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
    race1 = models.ForeignKey('Race', on_delete=models.SET_NULL, blank=True, null=True, related_name='race1_cards')
    race2 = models.ForeignKey('Race', on_delete=models.SET_NULL, blank=True, null=True, related_name='race2_cards')
    race3 = models.ForeignKey('Race', on_delete=models.SET_NULL, blank=True, null=True, related_name='race3_cards')
    effect_text = models.TextField(blank=True, null=True)
    symbol = models.CharField(max_length=10 ,blank=True, null=True)
    EXPANSION_CHOICES = [
        ('1st' , '1st'),
        ('2nd' , '2nd'),
    ]
    expansion = models.CharField(max_length=10, choices=EXPANSION_CHOICES, blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)
    explain = models.TextField(blank=True, null=True)
    priority = models.PositiveIntegerField(db_index=True, blank=True, null=True) 

    # # 並べ替え用。
    # class Meta:
    #     ordering = ['priority'] 
    # def __str__(self):
    #     return f"{self.id}: {self.name}"
    
    # # priorityを表示するためのメソッド
    # @admin.display(description='priority')
    # def get_prio(self):
    #     return self.priority
    
    # 系統を表示するためのメソッド
    @admin.display(description='系統')
    def get_race(self):
        str1 = str(self.race1) if self.race1 else ''
        str2 = ('・' + str(self.race2)) if self.race2 else ''
        str3 = ('・' + str(self.race3)) if self.race3 else ''
        return str1 + str2 + str3
    
    # 保存時のメソッド。
    def save(self, *args, **kwargs):

        # IDと表示優先度を自動で設定。
        if not self.id and not self.priority:
            # 色の判別
            if self.color == '赤紫緑白黄青':
                id_initial = 'S'
                pri_initial = '7'
            elif self.color[0] == '赤':
                id_initial = 'R'
                pri_initial = '1'
            elif self.color[0] == '紫':
                id_initial = 'P'
                pri_initial = '2'
            elif self.color[0] == '緑':
                id_initial = 'G'
                pri_initial = '3'
            elif self.color[0] == '白':
                id_initial = 'W'
                pri_initial = '4'
            elif self.color[0] == '黄':
                id_initial = 'Y'
                pri_initial = '5'
            elif self.color[0] == '青':
                id_initial = 'B'
                pri_initial = '6'

            # カテゴリの判別
            if self.category == 'スピリット':
                id_initial += 'S'
                pri_initial += '1'
            elif self.category == 'アルティメット':
                id_initial += 'U'
                pri_initial += '2'
            elif self.category == 'ブレイヴ':
                id_initial += 'B'
                pri_initial += '3'
            elif self.category == 'ネクサス':
                id_initial += 'N'
                pri_initial += '4'
            elif self.category == 'マジック':
                id_initial += 'M'
                pri_initial += '5'

            # コストの2桁表現を追加
            id_initial += f'{self.cost:02d}'
            pri_initial += f'{self.cost:02d}'

            # 末尾3桁の連番を探す
            count = 1
            while True:
                id_candidate = id_initial + f"{count:03d}"  
                if Card.objects.filter(id=id_candidate).exists():
                    count += 1
                else:
                    self.id = id_candidate
                    self.priority = int(pri_initial + f"{count:03d}")  
                    break

        super().save(*args, **kwargs)
    
