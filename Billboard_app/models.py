from django.db import models

# Create your models here.
class Messages(models.Model):
    msg_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    user_id = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)


def get_new_posts():
    posts = Billboard.objects.all()
    return posts
