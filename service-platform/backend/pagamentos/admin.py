from django.contrib import admin
from .models import Assinatura

@admin.register(Assinatura)
class AssinaturaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'status', 'data_pagamento', 'valor')
    list_filter = ('status',)
    search_fields = ('usuario__username',)
