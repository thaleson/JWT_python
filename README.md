# Sistema de Autenticação com Flask 🔒

Este é um projeto de sistema de autenticação simples, construído com Flask, que permite registro e login de usuários. O sistema utiliza JWT (JSON Web Tokens) para autenticação, com níveis de permissão para usuários (SUPERUSER e USER). 

## Funcionalidades

- Registro de novos usuários
- Login de usuários existentes
- Mensagens de feedback amigáveis
- Logout
- Sistema de níveis de permissão (SUPERUSER e USER)

## Pré-requisitos

Antes de começar, verifique se você tem os seguintes softwares instalados:

- [Python](https://www.python.org/downloads/) (versão 3.6 ou superior)
- [pip](https://pip.pypa.io/en/stable/) (gerenciador de pacotes para Python)

## Instalação

Siga estas instruções para configurar o projeto em seu ambiente local.

### 1. Clone o repositório

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

#### Windows

```bash
python -m venv venv
```

#### macOS e Linux

```bash
python3 -m venv venv
```

### 3. Ative o ambiente virtual

#### Windows

```bash
venv\Scripts\activate
```

#### macOS e Linux

```bash
source venv/bin/activate
```

### 4. Instale as dependências

Com o ambiente virtual ativado, instale as dependências necessárias com:

```bash
pip install -r requirements.txt
```

**Nota:** Se você não possui o arquivo `requirements.txt`, você pode criar um com as dependências essenciais do projeto. Um exemplo básico seria:

```
Flask
Flask-WTF
Flask-Login
PyJWT
```

### 5. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

```bash
SECRET_KEY=seu_segredo_aqui
```

### 6. Execute o projeto

Com tudo configurado, você pode executar o projeto com o comando:

```bash
flask run
```

Por padrão, o aplicativo estará disponível em `http://127.0.0.1:5000/`.

## Uso

### 1. Acesse a página inicial

Navegue até `http://127.0.0.1:5000/` no seu navegador.

### 2. Registre um novo usuário

Clique em **Register** e preencha o formulário para criar uma nova conta.

### 3. Faça login

Após o registro, você pode fazer login usando as credenciais que você criou.

### 4. Navegação

Depois de logado, você terá acesso a páginas específicas com base no seu nível de permissão.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).


