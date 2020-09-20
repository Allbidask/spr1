from django.db import models
from django.db.models import Max

# Create your models here.
class Article(models.Model):
    class Meta():
    	db_table= "article"
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)
    def __str__(self):
        return self.article_title
	
    
	
class Comments(models.Model):
	class Meta():
		db_table='comments'
	comments_text = models.TextField()
	comments_article = models.ForeignKey(Article, on_delete=models.CASCADE)
	def __str__(self):
		return self.comments_text
		
	
	
class Tretya(models.Model):
	class Meta():
		db_table='tretya'
	tretya_text = models.TextField()
	tretya_int = models.IntegerField(default=0)
	def __str__(self):
		return self.tretya_text
		
		
class Coin(models.Model):
	class Meta():
		db_table='coin_pd'
	MarketName = models.TextField()
	Birja = models.TextField()
	Bid = models.TextField() #тут надо сделать нормальный флоат
	id = models.IntegerField(primary_key=True)
	def __str__(self):
		return self.MarketName
		


class Time1(models.Model):		
	t = models.DateTimeField()
	
	def __str__(self):
		return self.t
