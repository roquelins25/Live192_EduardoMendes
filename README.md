# **Como Organizar um Projeto em Python**  

Este curso tem o objetivo de ensinar sobre a padronização de projetos em Python, dividido em 4 etapas:

### **1. Estruturas de Diretório**
- Organização e estruturação de diretórios para o projeto.
- Melhores práticas para cada tipo de arquivo.

### **2. Ferramentas de Desenvolvimento**
- Ferramentas que facilitam o processo de desenvolvimento e a integração com o Git.

### **3. Ferramentas de Checagem**
- Como garantir a padronização do código, utilizando ferramentas de checagem de qualidade de código.

### **4. Automações**
- Como criar automações para facilitar o seu trabalho e aumentar a produtividade.

---

## **Lista de Comandos Básicos Mais Utilizados ao Trabalhar com Versionamento em Git**

### **1. `git config`**
Este é o primeiro comando a ser executado após instalar o Git. Ele possibilita configurar seu nome e endereço de email que ficará vinculado às alterações.

    -$ git config --global user.name "Nome do usuário"  
    -$ git config --global user.email "seu@email.com"
    
### **2. `git init`**  
Inicia ou cria um repositório.

    -$ git init

### **3. `git status`**
Permite visualizar o estado do repositório.  

    -$ git status

### **4. `git add`** 
Prepara o conteúdo para o próximo commit.  

    -$ git add nome_do_arquivo  
    -$ git add .

### **5. `git commit`** 
Salva o conteúdo atual junto com uma mensagem de registro do usuário que descreve as alterações.  
    
    -$ git commit -m "Mensagem descritiva do commit"  

### **6. `git clone`** 
Clona um repositório existente.  
    
    -$ git clone [url]
    
### **7. `git branch`** 
Uma branch nada mais é do que uma ramificação dentro do repositório. Este comando pode ser utilizado de diversas maneiras.  
    
    -$ git branch // Mostra as branches existentes em um repositório  
    -$ git branch nome_da_branch // Cria uma nova branch  
    -$ git branch -M nome_da_branch // Renomeia a branch atual  

### **8. `git log`** 
Exibe um histórico de commits. Este comando pode ser utilizado de diversas formas.  
    
    -$ git log  
    -$ git log --oneline  

### **9. `git remote`** 
Exibe o repositório remoto.  
    
    -$ git remote  
    -$ git remote -v  

### **10. `git pull`** 
Baixa o conteúdo do repositório remoto, atualizando automaticamente o repositório local.  
    
    -$ git pull  

### **11. `git push`** 
Envia o conteúdo do repositório local, atualizando automaticamente o repositório remoto.  
    
    -$ git push  
---

# **ESTRUTURA**  
No que se baseia uma boa estrutura?  
- Seperação de responsabilidade  
  - Cada coisa deve esta no seu lugar  
<img src="/img/Nosso_Projeto.png">

Todos Codigos tem que ficar no Codigo Fonte e todos os teste fica na pasta teste
src = source ( utilizado para por colocar os dados )


Arquitetura é importante
IMAGEM 2
isso é muito comum de acontecer, gerar varios arquivos e colocar versões.

Ferramentas Utilizadas
Qual a versão do PYTHON utilizar? 
Sempre usar a Ultima versão possivel ( porem existe algumas bibliotecas grandes nao tem suporte nos ultimos, nesse caso buscar qual a versão ideal para sua biblioteca )
A importancia do Python estar atualizados por motivo de funcionalidades novas.

Pyenv - é bom para utilizar sobre a atualização de python
Como instalar (Windows)
    1. Abrir site do pyenv win no github 'https://github.com/pyenv-win/pyenv-win'
    2. Executar terminal modo administrador
    3. seguir o passo a passo ( site do pyenv-win):
        a. Executar comando = Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
            a.1. Caso tenha encontrado erro como 'não pode ser carregado porque a execução de scripts foi
desabilitada neste sistema. Para obter mais informações' executar os comandos de autorizações do powershell.
            a.2. Executar comando 'Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser'
            a.3. Autorizar todo comando A ou S
        b. Precisa verificar se o BAHS esta sendo executado com Pyenv
            b.1. Abrir BASH git:
                Executar comando pyenv --version
                Caso Aparece a versão do pyenv esta tudo 'OK' em caso de erro Segue os passo a passo:
                b.1.1 - Pesquisar por Variaveis do Ambiente ( Editar as variaveis de ambiente para sua conta)
                        avançado 
                        #( Dentro de Documentos o Pyenv por padrão cria uma pasta para executar, Abrir esse local)
                        -Click na pasta pyenv-win dentro de .pyenv/pyenv-win = copiar caminho da pasta
                        - Novo => e adcionar as seguintes ambientes
                          - PYENV
                          - PYENV_ROOT
                          - PYENV_HOME
                        # Todos os 3 com o mesmo local copiado - Retirar as  "ASPAS" do caminho copiado
                b.1.2 - PATH:
                        Clicar 2x no ambiente path e adicionar 2 modos:
                          - bin ( copiar caminho dentro da pasta .pyenv/pyenv-win/bin )
                          - shims (copiar caminho dentro da pasta .pyenv/pyenv-win/shims)
                    # Mover todos eles para cima ( deixando e 1 lugar )
                        - OK em Tudo
        b. pyenv versions ( verifica todas as versões do python dentro do pyenv)
        c. pyenv global 'versão mais recente' ( esse comando eu estou configurando a versão do meu python globalmente)
           pyenv local 'versão python' ( esse comando eu utilizo quando quero instalar versões diferentes dentro de cada pasta do meu projeto)
            - Para isso tem que entrar dentro da pasta desejada "COMANDO(CD.. => 'Nome do caminho' => pyenv local 'versão' )


# Ambientes Virtuais
#-pip freeze | grep -v "^-e" | xargs pip uninstall -y ( dica top para limpar e desisnstalar as bibliotecas geral )
    - 1. O que se preocupar?
      - Versão do python dentro da pasta a ser executada
      - Dependencias dentro do codigo
      - Sempre criar um ambiente virtual para cada pasta
    - 2. Como fazer?
      - 1. Installar o Ambiente virtal dentro da pasta
            1.a - Abrir vsCode na pasta
            1.b - executar comando no terminal ( python -m venv .venv)
      - 2. Ativar ambiente virtual
        - executar comando no terminal ( source .venv/Scripts/activate )
      - 3. Pode instalalar as Bibliotecas
        - executar comando no terminal ( pip install 'nome da biblioteca' )
      - 4. Sair do ambiente virtutal
        -  executar comando no terminal ( deactivate )






        pyenv install "Versão do python desejada '3.10.2' "
