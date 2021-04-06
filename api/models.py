from django.db import models

class Entry(models.Model):
    datum = models.DateTimeField(verbose_name="Datum", auto_now=False, auto_now_add=True)
    names = models.CharField(verbose_name="Names", max_length=200)
    cell = models.CharField(verbose_name="Address", max_length=200)
    question1 = models.BooleanField(verbose_name="Question 1")
    question2 = models.BooleanField(verbose_name="Question 2")
    temperature = models.FloatField(verbose_name="Temperature")

    class Meta:
        ordering = ["-datum"]
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
    
    def __str__(self):
        return f"{self.names}"