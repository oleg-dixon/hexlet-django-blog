from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Менеджером bulk_create можно создать сразу несколько статей, пример
# a = Article.objects.bulk_create([
#     Article(name="my super article", body="my content"), 
#     Article(name="my two super article", body="my two content"),
#     Article(name="my three super article", body="my three content"),
# ])