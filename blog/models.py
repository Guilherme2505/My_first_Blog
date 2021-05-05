from django.conf import settings
from django.db import models
from django.utils import timezone

class Postagem(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def teste_de_postagem(self):
        self.pblished_date = timezone.now()
        self.save()

        def __str__(self):
            return self.tittle
            