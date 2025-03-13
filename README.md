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