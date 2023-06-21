from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')

    # タグは複数紐づく。また、タグを設定しないことも可能にしている(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='タグ')

    def __str__(self):
        return self.title

        group = forms.ModelChoiceField(
        queryset=GoodsGroup.objects.all(),  # 選択肢となるデータの一覧
        label='グループ', required=False, empty_label='選択してください'
    )

# Create your models here.
