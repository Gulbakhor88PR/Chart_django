from django.db import models


class Post(models.Model):
    class Meta:
        verbose_name = 'Arxiv'
        verbose_name_plural = 'Arxivlar'

    nomi = models.CharField(max_length=50)
    mazmuni = models.TextField()

    def __str__(self):
        return self.nomi
    




