from django.db import models

class WordDefinition(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField(max_length=256)
    adittional_meaning_1 = models.CharField(max_length=256, blank=True, null=True)
   additional_meaning_2 = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.word
