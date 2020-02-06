from django.conf import settings
from django.db import models
from django.utils import timezone

'''
変更したらマイグレーションが必要なので、
↓でマイグレーションファイルを作成し
python manage.py makemigrations blog
↓で実行する
python manage.py migrate blog
'''

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    user = models.CharField(max_length=100, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Yukyu(models.Model):
	author	= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	busyo	= models.CharField(verbose_name='部署', max_length=100)
	name	= models.CharField(verbose_name='名前', max_length=100)
	riyuu	= models.CharField(verbose_name='理由', max_length=100)
	kyuka_type	= models.PositiveSmallIntegerField( verbose_name='休暇種類', choices=[ (1,'有給休暇'), (2,'特別休暇'), (3,'欠勤'), (4,'代休') ] )

	kikan	= models.PositiveSmallIntegerField( verbose_name='期間', choices=[ (1,'AM'), (2,'PM'), (3,'1日'), (4,'2日間'), (5,'3日間'), (6,'4日間'), (7,'5日間'), (8,'6日間') ] )
	start_date	= models.DateField(verbose_name='取得日', default=timezone.now)

	created_date	= models.DateTimeField(default=timezone.now)
	published_date	= models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title