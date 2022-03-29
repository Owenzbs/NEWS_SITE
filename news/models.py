from django.db import models
from django.urls import reverse
# Create your models here.
class News(models.Model):
    title= models.CharField(max_length=150)
    link= models.CharField(max_length=300)
    amount_of_upvotes=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    author_name= models.CharField(max_length=150)
    
    
    def get_absolute_url(self):
        return reverse("view_news", kwargs={"news_id": self.pk})
    
        
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="News "
        verbose_name_plural="News "
        ordering=['-created_at']
        
        
class Comments(models.Model):
    author_name= models.CharField(max_length=150)
    content=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    news=models.ForeignKey( 'News', on_delete=models.PROTECT, null=True )
    
    
    
    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name="Comments "
        verbose_name_plural="Comments "
        ordering=['-created_at']