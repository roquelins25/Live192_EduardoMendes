**Como organizar um Projeto em Python**
Esse curso que estou realizando vem com o ambito de aprender sobre padronização para todo projeto em Python.
Sera divido em 4 etapas:
**1 - Estruturas de Diretório**
     -E mais algumas coisas importantes
**2 - Ferramentas de Desenvolvimento**
     -Facilitando a vida
**3 - Ferramentas de Checagem**
     -Padronizando código entre linhas
**4 - Automações**
     -Algumas maniera de facilitar a vida

Lista de comandos básicos mais utilizados ao trabalhar com versionamento em Git
git config: Este é o primeiro comando a ser executado após instalar o Git. Ele possibilita configurar seu nome e endereço de email que ficará vinculado às alterações.
$ git config --global user.name "Nome do usuário"
$ git config --global user.email "seu@email.com"
git init: Inicia ou cria um repositório.
$ git init
git status: Permite visualizar o estado do repositório.
$ git status
git add: Prepara o conteúdo para o próximo commit.
$ git add nome_do_arquivo
$ git add .
git commit: Salva o conteúdo atual junto com uma mensagem de registro do usuário que descreve as alterações.
$ git commit -m "Mensagem descritiva do commit"
git clone: Clona um repositório existente.
$ git clone [url]
git branch: Uma branch nada mais é do que uma ramificação dentro do repositório. Este comando pode ser utilizado de diversas maneiras.
$ git branch // Mostra as branches existentes em um repositório
$ git branch nome_da_branch // Cria uma nova branch
$ git branch -M nome_da_branch // Renomeia a branch atual
git log: Exibe um histórico de commits. Este comando pode ser utilizado de diversas formas.
$ git log
$ git log --oneline
git remote: Exibe o repositório remoto.
$ git remote
$ git remote -v
git pull: Baixa o conteúdo do repositório remoto, atualizando automaticamente o repositório local.
$ git pull
git push: Envia o conteúdo do repositório local, atualizando automaticamente o repositório remoto.
$ git push

**ESTRUTURA**
No que se baseia uma boa estrutura?
 -Seperação de responsabilidade
    -Cada coisa deve esta no seu lugar
<img src="/img/Nosso_Projeto.png">
