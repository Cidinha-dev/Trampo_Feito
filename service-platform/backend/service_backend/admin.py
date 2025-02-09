from django.contrib import admin

# Personalize o cabeçalho, título e índice
admin.site.site_header = "Administração Trampo Feito"
admin.site.site_title = "Trampo Feito Admin"
admin.site.index_title = "Bem-vindo ao painel de administração do Trampo Feito"

# Classe personalizada para adicionar CSS ao admin
class CustomAdminSite(admin.AdminSite):
    site_header = "Administração Trampo Feito"
    site_title = "Trampo Feito Admin"
    index_title = "Bem-vindo ao painel de administração do Trampo Feito"

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = 'admin/css/custom_admin.css'
        return context

admin.site = CustomAdminSite()
