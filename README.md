
#### 1.1. Criar o Diretório do Projeto

No terminal, execute os comandos abaixo para organizar o projeto:

mkdir service-platform

cd service-platform

mkdir frontend backend database payments blog static templates deployment

  

O que está acontecendo aqui?

- mkdir service-platform: Crie a pasta principal do projeto chamada service-platform.
    
- cd service-platform: Entrada no diretório criado.
    
- mkdirpara subdiretórios : Cria os subdiretórios para organizar o projeto:
    

  

- frontend: Aqui será desenvolvido o frontend (interface do usuário).
    
- backend: Contém o código Django para gerenciar APIs e lógica do servidor.
    
- database: Scripts SQL ou backups relacionados ao banco de dados PostgreSQL.
    
- payments: Lógica e configurações para integração com sistemas de pagamento.
    
- blog: Código para gerenciar o blog integrado ao site.
    
- static: Arquivos como CSS, JavaScript e imagens.
    
- templates: Páginas HTML que serão renderizadas pelo Django.
    
- deployment: Arquivos para configurar e hospedar o projeto na AWS.
    

---

#### 1.2. Criar o Ambiente Virtual

Um ambiente virtual isolado das dependências do Python para evitar conflitos com outros projetos.

python -m venv venv

- python -m venv venv: Crie um ambiente virtual chamado venv na pasta atual.
    

- O ambiente virtual mantém as bibliotecas específicas do projeto independente das instaladas globalmente no sistema.
    

---

#### 1.3. Ativar o Ambiente Virtual

Após criar o ambiente virtual, active-o com o comando correto para o sistema operacional:

Linux/Mac :  
  
source venv/bin/activate

  

Janelas :  
  
venv\Scripts\activate

-   
    



- Você "entra" no ambiente virtual.
    
- Após ativar, o terminal indicará que não há ambiente virtual com algo como (venv)no início da linha.
    

---

#### 1.4. Instalar Django e Dependências

Dentro do ambiente virtual, instale o Django e o driver do PostgreSQL:

pip install django psycopg2-binary

  

Explicação:

- pip install: Comando para instalar pacotes Python.
    
- django: O framework principal para criar o backend do projeto.
    
- psycopg2-binary: Um driver necessário para conectar o Django ao banco de dados PostgreSQL.
    

---

#### 1.5. Criar o Projeto Django

Agora, crie o projeto Django no diretório backend:

cd backend

django-admin startproject service_platform .

  

caso necessario:

sudo apt install python3-django

  

Explicação:

- cd backend: Navegue para o diretório onde o backend será criado.
    
- django-admin startproject service_platform .:
    

  

- Crie um novo projeto Django chamado service_platform.
    
- O ponto .no final instrui o Django a criar os arquivos diretamente no diretório atual, evitando subpastas desnecessárias.
    

Após este comando, a estrutura no diretório backend será:

  

backend/

├── manage.py          # Ferramenta para gerenciar o projeto Django

└── service_platform/  # Diretório principal do projeto

    ├── __init__.py    # Arquivo que marca a pasta como um módulo Python

    ├── asgi.py        # Configuração para servidores ASGI

    ├── settings.py    # Configurações do projeto (banco, apps, etc.)

    ├── urls.py        # Rotas principais do projeto

    └── wsgi.py        # Configuração para servidores WSGI

---

#### 1.6. Executar o Servidor de Desenvolvimento

Instale o Django no ambiente virtual Enquanto o ambiente virtual estiver ativado, instale o Django novamente:  
  
pip install django

- Por que isso é necessário? O Django precisa estar instalado no ambiente virtual ativo. Se você instalou fora dele, o Python dentro do ambiente não o regular.
    

Verifique se o Django foi instalado . Confirme a instalação com:  
  
pip show django

Isso deve exibir informações sobre a versão do Django instalada. Caso não aplique nada, o Django não foi instalado no ambiente virtual.

Execute novamente o servidor Volte para o diretório onde está o arquivo 

manage.py e tente executar o servidor novamente:  
  
python manage.py runserver

  

2. Acesse no navegador:
    

- URL : http://127.0.0.1:8000​
    

Se tudo estiver configurado corretamente, você verá a página inicial padrão do Django.

---


### Próximos Passos

Aplicar as Migrações Padrão O Django possui algumas migrações básicas relacionadas aos aplicativos internos, como admin, auth, sessions, etc.

sair  
  
python manage.py migrate

8. Explicação:
    

- Esse comando configura o banco de dados com as tabelas básicas necessárias para o funcionamento do Django, incluindo autenticação de usuários e sessões.
    

---

Testar a Página de Administração O Django vem com um painel administrativo pronto. Após aplicar as migrações, crie um superusuário para acessá-lo:  
  
python manage.py createsuperuser

9. Você deve fornecer:
    

- Nome de usuário 
    
- E-mail (opcional)
    
- Senha
    

10. Após criar o superusuário, acesse o painel administrativo em: http://127.0.0.1 : 8000 /admin
    

---

11. Testar Configuração
    

- Verifique se a página inicial padrão do Django ( [http ://127.0.0.1 :8000/](http://127.0.0.1:8000/) ) aparece corretamente.
    
- Verifique se o painel de administração ( http://127.0.0.1 : 8000 /admin ) está acessível e funcional.
    

---

Senha: admin@trampo  
site: trampofeito.br

email: [de.trampofeito@gmail.com](mailto:de.trampofeito@gmail.com) 

senha: admin@trampo



  
**

# Projeto Django - Trampo Feito

Este guia fornece um passo a passo detalhado para criar um projeto Django desde o início, incluindo a configuração do ambiente, implementação do sistema e customização do painel administrativo.

---

## 1. **Configuração do Ambiente**

### 1.1 Criar Ambiente Virtual
No terminal, execute:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 1.2 Instalar Django e Dependências
```bash
pip install django jazzmin
```

---

## 2. **Criar o Projeto e Estrutura Inicial**

### 2.1 Criar o Projeto Django
```bash
django-admin startproject service_backend .
```
Estrutura:
```
backend/
├── manage.py
├── service_backend/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    ├── wsgi.py
```

### 2.2 Criar Aplicativos
```bash
python manage.py startapp servicos
python manage.py startapp pagamentos
```
Estrutura:
```
backend/
├── servicos/
├── pagamentos/
```

---

## 3. **Configuração de Apps e Banco de Dados**

### 3.1 Registrar Apps
No `settings.py`, adicione em `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'servicos',
    'pagamentos',
    'jazzmin',
]
```

### 3.2 Configurar Banco de Dados
Configure a conexão com o banco no `settings.py` (exemplo com SQLite):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

---

## 4. **Modelos de Dados**

### 4.1 Serviços
Crie `servicos/models.py`:
```python
from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
```

### 4.2 Pagamentos
Crie `pagamentos/models.py`:
```python
from django.db import models

class Pagamento(models.Model):
    metodo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metodo} - R$ {self.valor:.2f}"
```

---

## 5. **Administração**

### 5.1 Registrar Modelos no Admin
Atualize `servicos/admin.py`:
```python
from django.contrib import admin
from .models import Servico

admin.site.register(Servico)
```

Atualize `pagamentos/admin.py`:
```python
from django.contrib import admin
from .models import Pagamento

admin.site.register(Pagamento)
```

### 5.2 Personalizar Jazzmin
No `settings.py`, configure:
```python
JAZZMIN_SETTINGS = {
    "site_title": "Admin Trampo Feito",
    "site_header": "Trampo Feito",
    "welcome_sign": "Bem-vindo ao Trampo Feito Admin",
    "show_ui_builder": True,
}
```

---

## 6. **URLs e Views**

### 6.1 Configurar URLs
No `service_backend/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicos/', include('servicos.urls')),
]
```

### 6.2 Criar Views para Serviços
No `servicos/views.py`:
```python
from django.shortcuts import render
from .models import Servico

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/lista_servicos.html', {'servicos': servicos})
```

### 6.3 Configurar URLs de Serviços
Crie `servicos/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_servicos, name='lista_servicos'),
]
```

---

## 7. **Templates e Estáticos**

### 7.1 Estrutura de Templates
Estrutura recomendada:
```
backend/
├── templates/
|   ├── servicos/
|       └── lista_servicos.html
|   └── homepage.html
```

### 7.2 Exemplo de Template: `homepage.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Trampo Feito</title>
</head>
<body>
    <h1>Bem-vindo ao Trampo Feito!</h1>
    <a href="/servicos/">Procurar Serviços</a>
</body>
</html>
```

### 7.3 Configurar Estáticos
No `settings.py`:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
Para coletar estáticos:
```bash
python manage.py collectstatic
```

---

## 8. **Iniciar o Servidor**
Execute:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Acesse o projeto em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 9. **Extensões e Melhorias Futuras**
- **Implementar Busca**: Adicione um form para busca de serviços.
- **Autenticação**: Configure login e área restrita.
- **Integração com Pagamentos**: Utilize gateways como PayPal ou Stripe.
- **Hospedagem**: Publique o projeto no Heroku ou AWS.

Este guia abrange desde a criação do projeto até configurações de personalização. Altere conforme suas necessidades!


    ----------------
    

**
