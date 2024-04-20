from django.db import models
class Task(models.Model):
    title       = models.CharField    (max_length= 200)
    completed   = models.BooleanField (default=False)
    discription = models.TextField    (blank=True,null=True)
    created     = models.DateTimeField(auto_now_add = True)
    user_id     = models.CharField    (max_length=200)
    
    def __str__(self) -> str:
        return self.title    
