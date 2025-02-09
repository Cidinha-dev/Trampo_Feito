from django.db import models
from django.contrib.auth.models import User

class Assinatura(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=[
        ('ativo', 'Ativo'),
        ('inadimplente', 'Inadimplente'),
    ])
    data_pagamento = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)

    def __str__(self):
        return f'{self.usuario.username} - {self.status}'
