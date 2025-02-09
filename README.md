
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
    

O que acontece aqui?

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

### Recapitulando: Fluxo até Aqui

3. Criamos a estrutura básica do projeto.
    
4. Configuramos um ambiente virtual Python.
    
5. Instalamos Django e o driver do PostgreSQL.
    
6. Criamos o projeto Django no diretório backend.
    
7. Testamos o servidor de desenvolvimento para garantir que tudo funcione.
    

  

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

wix: TrampoFeito@123456

  
**

### 1.1. Crie o Diretório do Projeto

mkdir projeto_django

cd projeto_django

  

### 1.2. Crie e Ative um Ambiente Virtual

python3 -m venv venv

source venv/bin/activate

  

### 1.3. Instale o Django e Outras Bibliotecas Necessárias

pip install django psycopg2-binary django-jazzmin

  

---

## 2. Criação do Projeto e Configuração Inicial

### 2.1. Crie o Projeto Django

django-admin startproject service_backend .

  

### 2.2. Estrutura Inicial do Projeto

projeto_django/

├── manage.py

├── service_backend/

│   ├── __init__.py

│   ├── asgi.py

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

  

---

## 3. Configurações do Projeto

### 3.1. Edite settings.py

Adicione as seguintes configurações no arquivo service_backend/settings.py:

#### Configuração do Banco de Dados (PostgreSQL):

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': 'nome_do_banco',

        'USER': 'usuario_do_banco',

        'PASSWORD': 'senha_do_banco',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}

  

#### Configurações de Arquivos Estáticos:

import os

  

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

  

#### Integração com Jazzmin:

INSTALLED_APPS = [

    'jazzmin',

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    # Apps personalizados

    'servicos',

    'pagamentos',

]

  

JAZZMIN_SETTINGS = {

    "site_title": "Admin Trampo Feito",

    "site_header": "Trampo Feito",

    "welcome_sign": "Bem-vindo ao Trampo Feito Admin",

    "show_ui_builder": True,

}

  

---

## 4. Crie os Apps

### 4.1. Criar Apps Personalizados

python manage.py startapp servicos

python manage.py startapp pagamentos

  

### 4.2. Atualize INSTALLED_APPS

Edite service_backend/settings.py para incluir os apps criados:

INSTALLED_APPS += [

    'servicos',

    'pagamentos',

]

  

---

## 5. Modelos e Banco de Dados

### 5.1. Modelos

#### Serviços: servicos/models.py

from django.db import models

  

class Servico(models.Model):

    nome = models.CharField(max_length=255)

    descricao = models.TextField()

    preco = models.DecimalField(max_digits=10, decimal_places=2)

    criado_em = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)

  

    def __str__(self):

        return self.nome

  

#### Pagamentos: pagamentos/models.py

from django.db import models

  

class Pagamento(models.Model):

    metodo = models.CharField(max_length=50)

    valor = models.DecimalField(max_digits=10, decimal_places=2)

    data_pagamento = models.DateTimeField(auto_now_add=True)

  

    def __str__(self):

        return f"{self.metodo} - R$ {self.valor}"

  

### 5.2. Migrações do Banco de Dados

python manage.py makemigrations

python manage.py migrate

  

---

## 6. Admin Django

### 6.1. Personalize o Admin

#### servicos/admin.py

from django.contrib import admin

from .models import Servico

  

@admin.register(Servico)

class ServicoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'preco', 'criado_em', 'atualizado_em')

    search_fields = ('nome',)

  

#### pagamentos/admin.py

from django.contrib import admin

from .models import Pagamento

  

@admin.register(Pagamento)

class PagamentoAdmin(admin.ModelAdmin):

    list_display = ('metodo', 'valor', 'data_pagamento')

    search_fields = ('metodo',)

  

---

## 7. URLs e Views

### 7.1. URLs Globais: service_backend/urls.py

from django.contrib import admin

from django.urls import path, include

  

urlpatterns = [

    path('admin/', admin.site.urls),

    path('servicos/', include('servicos.urls')),

]

  

### 7.2. URLs dos Apps

#### Serviços: servicos/urls.py

from django.urls import path

from . import views

  

urlpatterns = [

    path('', views.lista_servicos, name='lista_servicos'),

    path('adicionar/', views.adicionar_servico, name='adicionar_servico'),

]

  

#### Views de Serviços: servicos/views.py

from django.shortcuts import render

from .models import Servico

  

# Listar serviços

def lista_servicos(request):

    servicos = Servico.objects.all()

    return render(request, 'servicos/lista_servicos.html', {'servicos': servicos})

  

# Adicionar serviço

def adicionar_servico(request):

    if request.method == 'POST':

        form = ServicoForm(request.POST)

        if form.is_valid():

            form.save()

            return render(request, 'servicos/sucesso.html')

    else:

        form = ServicoForm()

    return render(request, 'servicos/adicionar_servico.html', {'form': form})

  

---

## 8. Templates e Estilos

### 8.1. Estrutura de Templates

backend/templates/

├── homepage.html

└── servicos/

    ├── lista_servicos.html

    ├── adicionar_servico.html

    └── sucesso.html



## 9. Estilizando com CSS

### Estrutura do Diretório de Estáticos

static/

└── css/

    └── style.css

  



## 10. Finalização

### Comandos para Gerenciar o Servidor

Iniciar o servidor:  
python manage.py runserver

-   
    
- Parar o servidor: Ctrl + C
    

Aplicar migrações:  
python manage.py makemigrations

python manage.py migrate

-   
    ----------------
    

**
