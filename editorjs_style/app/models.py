from django.db import models
from django_editorjs_fields import EditorJsTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_images/')
    desc = models.TextField(max_length=255)
    body = EditorJsTextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
