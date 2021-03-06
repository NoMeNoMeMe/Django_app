from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# CharField is for restricted text (max length etc.)
# TextField is for unrestricted fields
# timezone.now() - execute function (not what we want now)
# timezone.now   - import function for future run
# reverse function returns url as a string
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
