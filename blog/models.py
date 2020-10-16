from django.db import models


from account.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题', blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='博主')
    content = models.TextField(verbose_name='内容')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
