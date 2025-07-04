# Servidor IoT Flask 🚀

Este é um servidor web construído com Flask, cujo principal objetivo é atuar como um endpoint robusto para receber, processar e armazenar dados de dispositivos IoT.

## 🎯 Objetivo Principal

O foco deste projeto é fornecer uma solução de backend simples e eficiente para cenários de Internet das Coisas (IoT). Ele foi desenhado para:

-   **Receber requisições `POST`** de dispositivos IoT (como ESP32, ESP8266, Raspberry Pi, etc.).
-   **Processar e validar** os dados recebidos (neste caso, leituras de temperatura).
-   **Armazenar os dados** de forma segura e persistente em um banco de dados SQLite.
-   **Proteger o endpoint** de recebimento com um token de autenticação, garantindo que apenas dispositivos autorizados possam enviar dados.

Além do recebimento de dados, o servidor oferece uma interface web simples para visualizar as informações coletadas.

## ✨ Funcionalidades

-   **Recebimento de Dados:** Endpoint para receber dados de temperatura via requisições POST.
-   **Armazenamento:** Salva os dados de temperatura em um banco de dados SQLite.
-   **Visualização:** Páginas web para visualizar a última temperatura registrada e um histórico de todas as temperaturas.
-   **Autenticação:** Protege o endpoint de recebimento de dados com um token de autorização.

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python, Flask
-   **Banco de Dados:** SQLite com Flask-SQLAlchemy
-   **Frontend:** HTML, CSS (com templates Jinja2)
-   **Gerenciamento de Ambiente:** python-dotenv

## ⚙️ Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto localmente.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/antoniomedeiross/servidor_iot_flask.git
    cd servidor_iot_flask
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione a seguinte linha, substituindo `sua_senha_secreta` por um token de sua escolha:
    ```
    SENHA="sua_senha_secreta"
    ```

5.  **Execute a aplicação:**
    ```bash
    flask run
    ```
    O servidor estará disponível em `http://127.0.0.1:5000`.

## 🔌 Endpoints da API

### Página Inicial

-   **URL:** `/`
-   **Método:** `GET`
-   **Descrição:** Exibe a página inicial com links para as outras seções.

### Enviar Dados de Temperatura

-   **URL:** `/temperatura`
-   **Método:** `POST`
-   **Descrição:** Salva uma nova leitura de temperatura.
-   **Header de Autenticação:**
    -   `Authorization`: `seu_token_configurado_no_.env`
-   **Corpo da Requisição (JSON):**
    ```json
    {
      "temperatura": 25.5
    }
    ```
-   **Resposta de Sucesso (201):**
    ```json
    {
      "mensagem": "Temperatura:25.5°C salva com sucesso!",
      "data/hora": "YYYY-MM-DDTHH:MM:SS.ssssss"
    }
    ```
-   **Resposta de Erro (401):**
    ```json
    {
      "erro": "Acesso não autorizado."
    }
    ```

### Ver Última Temperatura

-   **URL:** `/temperatura`
-   **Método:** `GET`
-   **Descrição:** Exibe uma página HTML com a última temperatura registrada.

### Ver Todas as Temperaturas

-   **URL:** `/todas_temperaturas`
-   **Método:** `GET`
-   **Descrição:** Exibe uma página HTML com o histórico de todas as temperaturas salvas.

## 📁 Estrutura do Projeto

```
.
├── app.py                # Arquivo principal da aplicação Flask
├── requirements.txt      # Dependências do projeto
├── .env                  # Arquivo para variáveis de ambiente (não versionado)
├── instance/
│   └── temperatura.db    # Banco de dados SQLite
├── static/
│   └── global_styles.css # Folha de estilos CSS
└── templates/
    ├── index.html
    ├── todas_temperaturas.html
    └── ultima_temperatura.html
```
