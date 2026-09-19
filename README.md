# Integração Python + Evolution API (WhatsApp)

Este repositório contém uma aplicação estruturada para interagir com o WhatsApp utilizando
a **Evolution API (v2.1.1)** orquestrada via Docker. O projeto inclui exemplos práticos de envio
de mensagens de texto, mídias e um sistema automatizado para notificação de erros (logs) da aplicação diretamente no WhatsApp.

## 🛠️ Tecnologias Utilizadas

*   **Python 3.x**: Linguagem principal para os scripts de integração.
*   **Evolution API v2.1.1**: Engine (Baileys) para a ligação e comunicação com a rede do WhatsApp.
*   **Docker & Docker Compose**: Ferramentas para gerir a infraestrutura de forma isolada.
*   **PostgreSQL 15**: Base de dados para armazenamento de instâncias e histórico da API.
*   **Redis**: Sistema de cache para otimização da aplicação.

---

## 🚀 Como Configurar e Executar o Projeto

### 1. Configurar as Variáveis de Ambiente
Crie um ficheiro chamado `.env` na raiz do projeto para configurar as credenciais da Evolution API
e as ligações de base de dados. 
*(Nota: O ficheiro `.env` está protegido e ignorado pelo Git, garantindo que as suas credenciais não sejam publicadas)*.

Exemplo de configuração base:

```env
# EVOLUTION API
AUTHENTICATION_API_KEY=Anm@88
EVO_BASE_URL=http://localhost:8080
EVO_INSTANCE_NAME=nome_instancia
EVO_PHONE_LOGGER=numero_whatsapp # Número que receberá os alertas de erro, formato -> 5500911112222

# POSTGRESQL (Apontando para o container 'postgres')
DATABASE_ENABLED=true
DATABASE_PROVIDER=postgresql
DATABASE_CONNECTION_URI=postgresql://postgres:postgres@postgres:5432/evolution?schema=public
DATABASE_CONNECTION_CLIENT_NAME=evolution_exchange

# Salvar dados no banco
DATABASE_SAVE_DATA_INSTANCE=true
DATABASE_SAVE_DATA_NEW_MESSAGE=true
DATABASE_SAVE_MESSAGE_UPDATE=true
DATABASE_SAVE_DATA_CONTACTS=true
DATABASE_SAVE_DATA_CHATS=true
DATABASE_SAVE_DATA_LABELS=true
DATABASE_SAVE_DATA_HISTORIC=true

# Ultima versão do WhatsApp
CONFIG_SESSION_PHONE_VERSION=2.3000.1047877691

# REDIS (Apontando para o container 'redis')
CACHE_REDIS_ENABLED=true
CACHE_REDIS_URI=redis://redis:6379/6
CACHE_REDIS_PREFIX_KEY=evolution
CACHE_REDIS_SAVE_INSTANCES=false
CACHE_LOCAL_ENABLED=false

# CONFIGURAÇÕES DA SESSÃO E WEBSOCKET
SERVER_TYPE=http
CONFIG_SESSION_PHONE_CLIENT_NAME=Evolution
DEFAULT_INTEGRATION=BAILEYS
WEBSOCKET_ENABLED=true
WEBSOCKET_GLOBAL_EVENTS=true
```

### 2. Subir a Infraestrutura (Docker)
O projeto utiliza um ficheiro docker-compose.yml pré-configurado com uma rede isolada (evolution-net)
para executar a API, o PostgreSQL e o Redis em simultâneo.

Agora, com o terminal localizado no diretório do projeto, pode subir a nossa Evolution API com o comando:

```Bash
docker-compose up --build
```
Após a inicialização dos contentores, ligue a sua instância do WhatsApp gerando o QR Code ou o Pairing Code através da Evolution API.

### 3. Aceder ao Dashboard de Gerenciamento (Manager)
O dashboard de gerenciamento da Evolution API estará disponível no seu navegador em:
👉 http://localhost:8080/manager

A senha para efetuar o login será o valor definido no ficheiro .env na variável AUTHENTICATION_API_KEY

### 4. Instalar Dependências Python
Crie um ambiente virtual e instale os pacotes necessários definidos no requirements.txt. O diretório do ambiente
virtual (ex: venv/) já está configurado para ser ignorado no controlo de versões.

```Bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual (Windows)
.\venv\Scripts\Activate.ps1 ou venv\Scripts\activate

# Ativar o ambiente virtual (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

## 💻 Exemplos de Uso
### Envio de Mensagem de Texto
O script send_message.py envia uma mensagem de texto simples, simulando o estado de "a escrever..."
através de um atraso de 10.000 ms definido no delay.

```Bash
python send_message.py
```

### Envio de Mídia
O script send_media.py demonstra como enviar imagens a partir de um URL público, onde é possível definir
o tipo MIME (image/jpeg), o nome do ficheiro e a legenda da imagem.
```Bash
python send_media.py
```

### Logger de Erros via WhatsApp
A classe EvolutionApi no ficheiro services/evolution_api.py encapsula as chamadas à API
e carrega as chaves diretamente do ficheiro .env.   O script principal app.py utiliza esta
estrutura num bloco try/except. Caso ocorra alguma exceção na execução (exemplo: falha ao processar uma venda),
o traceback completo do erro é formatado e enviado automaticamente por WhatsApp para o número
de suporte configurado na variável EVO_PHONE_LOGGER.
```Bash
python app.py
```

## 🛡️ Controlo de Versões (Git)
O repositório inclui um ficheiro .gitignore padronizado para projetos Python. Ele garante
que ficheiros sensíveis e locais não sejam partilhados publicamente no GitHub, ignorando
automaticamente:   
- Ficheiros de credenciais e variáveis de ambiente (.env).   
- Diretórios de ambientes virtuais (venv/, .venv, env/).   
- Ficheiros binários compilados pelo Python (__pycache__/, *.pyc).   
- Ficheiros de cache de bibliotecas e ferramentas de teste (.pytest_cache/, .mypy_cache/).   
