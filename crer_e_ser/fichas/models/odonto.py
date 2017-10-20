from django.db import models

class Ficha(models.Model):
    escovacao_diaria = models.CharField(max_length=20, blank=False)
    escova = models.CharField(max_length=20, blank=False)
    troca_de_escova = models.CharField(max_length=20, blank=False)
    usa_creme_dental = models.BooleanField(blank=False)
    foi_ao_dentista = models.BooleanField(blank=False)



    