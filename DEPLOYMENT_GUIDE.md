# Guia de Despliegue Permanente - MeuFreteFácil

## Visão Geral

Este guia fornece instruções passo a passo para desplegar a aplicação MeuFreteFácil em uma plataforma de hospedagem permanente. A aplicação foi preparada com todos os arquivos necessários para despliegue em contêineres.

## Arquivos de Configuração Preparados

A aplicação agora inclui os seguintes arquivos de configuração:

- **Dockerfile**: Define a imagem Docker da aplicação
- **.dockerignore**: Especifica arquivos a serem ignorados na construção Docker
- **Procfile**: Configuração para plataformas como Heroku
- **render.yaml**: Configuração específica para Render
- **railway.json**: Configuração específica para Railway
- **requirements.txt**: Dependências Python com versões fixas
- **runtime.txt**: Versão do Python (3.11.0)

## Opções de Despliegue Recomendadas

### Opção 1: Render (Recomendado para Começar)

**Vantagens**: Fácil de usar, nível gratuito disponível, despliegue automático do GitHub

**Passos**:

1. Acesse [render.com](https://render.com) e crie uma conta
2. Clique em "New +" e selecione "Web Service"
3. Conecte seu repositório GitHub
4. Configure as seguintes opções:
   - **Name**: meufretefacil
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Clique em "Create Web Service"
6. Seu aplicativo estará disponível em um link temporário (ex: `https://meufretefacil.onrender.com`). O próximo passo será configurar seu domínio personalizado.

### Opção 2: Railway

**Vantagens**: Interface limpa, despliegue automático, tempo de atividade > 99,95%

**Passos**:

1. Acesse [railway.app](https://railway.app) e crie uma conta
2. Clique em "New Project"
3. Selecione "Deploy from GitHub"
4. Conecte seu repositório
5. Railway detectará automaticamente o `railway.json` e `Dockerfile`
6. Configure as variáveis de ambiente se necessário
7. Clique em "Deploy"

### Opção 3: DigitalOcean App Platform

**Vantagens**: Melhor relação custo-benefício, escalabilidade garantida, suporte confiável

**Passos**:

1. Acesse [digitalocean.com](https://www.digitalocean.com) e crie uma conta
2. Vá para "App Platform"
3. Clique em "Create App"
4. Selecione seu repositório GitHub
5. Configure o seguinte:
   - **Source**: GitHub
   - **Repository**: seu repositório
   - **Branch**: main
6. DigitalOcean detectará automaticamente o `Dockerfile`
7. Clique em "Next" e configure as variáveis de ambiente
8. Clique em "Create Resources"

### Opção 4: Back4App

**Vantagens**: Nível gratuito generoso, integração com GitHub, suporte excelente

**Passos**:

1. Acesse [back4app.com](https://www.back4app.com) e crie uma conta
2. Clique em "Create a New App"
3. Selecione "Container as a Service"
4. Conecte seu repositório GitHub
5. Configure o `Dockerfile` como a imagem base
6. Clique em "Deploy"

## Preparação do Repositório GitHub

Antes de desplegar, certifique-se de que seu repositório GitHub contém:

```bash
meufretefacil/
├── app.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── Dockerfile
├── .dockerignore
├── render.yaml
├── railway.json
├── .gitignore
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── motorista.py
│   │   ├── transportadora.py
│   │   ├── Programacao.py
│   │   └── HistoricoProgramacao.py
│   └── routes/
│       ├── __init__.py
│       ├── motorista.py
│       ├── transportadora.py
│       ├── upload.py
│       ├── historico.py
│       └── busca.py
├── templates/
│   └── index.html
├── static/
│   └── js/
│       └── app.js
└── instance/
    └── freteconnect.db
```

## Variáveis de Ambiente

Se necessário, configure as seguintes variáveis de ambiente na plataforma de despliegue:

- **FLASK_ENV**: `production`
- **FLASK_DEBUG**: `0`
- **PYTHONUNBUFFERED**: `1`

## Verificação Pós-Despliegue

Após o despliegue, verifique se:

1. A aplicação está acessível via HTTPS
2. O cabeçalho com navegação está visível
3. Todos os links funcionam corretamente
4. Não há erros no console do navegador
5. O banco de dados foi criado corretamente

## Solução de Problemas

### Erro: "ModuleNotFoundError"
- Verifique se `requirements.txt` contém todas as dependências
- Certifique-se de que os arquivos de modelo estão no diretório correto

### Erro: "Port already in use"
- A plataforma de despliegue atribui automaticamente uma porta
- Não é necessário especificar a porta no comando de inicialização

### Erro: "Database locked"
- Verifique se apenas uma instância da aplicação está rodando
- Considere usar um banco de dados gerenciado (PostgreSQL) em produção

## Próximos Passos

### Passo 1: Enviar o Código para o GitHub (Seu Repositório)

Este é o passo mais importante e que você precisa fazer primeiro.

1.  **Crie um novo repositório vazio** no seu GitHub (ex: `meufretefacil`).
    -   **NÃO** adicione `README`, `.gitignore` ou `License` ao criar.
2.  **Me forneça o link HTTPS** desse repositório (ex: `https://github.com/SeuUsuario/meufretefacil.git`).
3.  Eu usarei o Git para enviar todos os arquivos corrigidos para o seu repositório.

### Passo 2: Implantação na Plataforma (Usando Render como Exemplo)

Siga os passos da **Opção 1: Render** (linhas 21-36) no guia.

### Passo 3: Configurar o Domínio Personalizado (`meufretefacil.com.br`)

Após o Render implantar o site e ele estiver online em um link temporário (ex: `https://meufretefacil.onrender.com`), você precisará conectar seu domínio:

1.  **No Render:**
    -   Vá para o painel do seu serviço (`meufretefacil`).
    -   Clique na aba **"Settings"** (Configurações) ou **"Domains"** (Domínios).
    -   Clique em **"Add a Custom Domain"** (Adicionar Domínio Personalizado).
    -   Digite seu domínio: `meufretefacil.com.br`
    -   O Render fornecerá um **registro CNAME** (ex: `web.render.com`) e um **registro A** (com um endereço IP).

2.  **No seu Provedor de Domínio (Onde você comprou o `meufretefacil.com.br`):**
    -   Acesse o painel de controle do seu domínio (onde você gerencia o DNS).
    -   Vá para a seção de **Gerenciamento de DNS** ou **Zona DNS**.
    -   **Adicione o registro CNAME** fornecido pelo Render para o subdomínio `www` (ex: `www CNAME web.render.com`).
    -   **Adicione o registro A** fornecido pelo Render para o domínio raiz (`@` ou `meufretefacil.com.br`).

3.  **Aguarde:** Pode levar de 1 a 24 horas para que as alterações de DNS se propaguem.

4.  **Verifique no Render:** O Render verificará automaticamente e, quando o DNS estiver configurado corretamente, seu site estará acessível em `https://meufretefacil.com.br`.

## Próximos Passos

1. Escolha uma das opções de despliegue acima
2. Crie uma conta na plataforma
3. Conecte seu repositório GitHub
4. Configure as variáveis de ambiente
5. Despliegue a aplicação
6. Teste a funcionalidade completa
7. Configure seu domínio personalizado (`meufretefacil.com.br`)

## Suporte

Para questões sobre despliegue, consulte a documentação oficial:
- [Render Documentation](https://render.com/docs)
- [Railway Documentation](https://docs.railway.app)
- [DigitalOcean App Platform Documentation](https://docs.digitalocean.com/products/app-platform)
- [Back4App Documentation](https://www.back4app.com/docs)
