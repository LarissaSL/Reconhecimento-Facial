# 🖥️🧑‍🦰 APP Web de Reconhecimento Facial

Este é um aplicativo web desenvolvido em Python e Flask para realizar o reconhecimento facial. Ele permite que os usuários carreguem novas imagens para treino e realizem o reconhecimento facial com base nas imagens enviadas. Além disso, ao ser identificado no sistema, o usuário poderá acessar um painel com mais informações sobre a aula. Ao fazer login durante o período da aula, o usuário recebe presença.

---

<br><br>

## 🚀👩‍💻 Time de Desenvolvimento

-  [Larissa Silva](https://github.com/LarissaSL) como Desenvolvedora Fullstack
-  [Wesley Silva](https://github.com/WesleyS08) como Desenvolvedor Fullstack

---

<br><br>

## 📌 Pré-requisitos de Tecnologias

Para iniciar o projeto, você precisa ter os seguintes requisitos instalados:

- **[Python 3.13](https://www.python.org/downloads/)**  
  Verifique se você tem o Python instalado no seu ambiente de desenvolvimento. Caso contrário, instale a versão mais recente.

- **IDE para PYTHON**  
  Você pode escolher entre as seguintes opções de IDE:
  - [Visual Studio Code (Recomendada)](https://code.visualstudio.com/)
  - [PyCharm para Windows](https://www.jetbrains.com/pt-br/pycharm/download/?section=windows)

---

<br><br><br>

## 📑 Índice
### 1. Inclusões
- [Inclusões](#-1-inclus%C3%B5es)

### 2. Funcionalidades
- [Funcionalidades](#%EF%B8%8F-2-funcionalidades)

### 3. Padrões de Commit
- [Padrões de Nomenclatura nos Commits](#-3-padr%C3%B5es-de-nomenclatura-nos-commits)

### 4. Bibliotecas Externas
- [Bibliotecas Externas](#%EF%B8%8F%EF%B8%8F-4-bibliotecas-externas)
- [Flask](#1-flask)
- [Numpy](#2-numpy)
- [OpenCV](#3-opencv)

### 5. Rodando a Aplicação Web
- [Rodando o Arquivo app.py](#%EF%B8%8F-5-rodando-a-aplica%C3%A7%C3%A3o-web)

### 6. Cadastro de Imagens
- [Entendendo o Cadastro de Imagens](#6-entendendo-o-cadastro-de-imagens)

### 7. Treinar o Reconhecimento Facial
- [Passos para Treinar o Reconhecimento Facial](#%EF%B8%8F-7-passos-para-treinar-o-reconhecimento-facial)
- [Entendendo o Controller de Reconhecimento Facial](#-71-entendendo-o-controller-de-reconhecimento-facial)

### 8. Reconhecimento Facial
- [Reconhecimento Facial](#-8-reconhecimento-facial)

### Extra 
- [Tecnologias](#%EF%B8%8F%EF%B8%8F-tecnologias)
- [Apêndices](#-ap%C3%AAndices)
- [Verificando PIP](#-verificar-se-o-pip-est%C3%A1-instalado-e-configurado)

---

<br><br><br>

## 🎯 1. Inclusões

- ✅ Criação do Readme do APP

---

<br><br>

## ⚙️ 2. Funcionalidades

- 🟢 Endpoint para Receber Imagens para Treino
- 🟢 Script para Renomear Imagens 
- 🟢 Script para Separar as Imagens para Treino e Teste
- 🟢 Endpoint para Acessar o Painel do Aluno por Reconhecimento Facial

<br>

**🔝 [Voltar ao Índice](#-%C3%ADndice)**

---

<br><br><br>

## 📓 3. Padrões de Nomenclatura nos Commits

Abaixo segue uma tabela onde explicamos um padrão para nossos commits.

| **Tipo**    | **Descrição**                                                   |
|-------------|-----------------------------------------------------------------|
| **FEAT**    | Para novos recursos                                             |
| **FIX**     | Solucionando um problema                                        |
| **RAW**     | Arquivo de configs, dados, features, parâmetros                 |
| **BUILD**   | Arquivos de build e dependências                                |
| **PERF**    | Mudança de performance                                          |
| **REMOVE**  | Exclusão de arquivos, diretórios ou código                      |
| **CHORE**   | Atualizações de tarefas de build, configs de admin, pacotes, etc|
| **REFACTOR**| Refatorações sem alterar funcionalidade                         |
| **TESTE**   | Alterações em teste                                             |
| **CI**      | Mudanças relacionadas a integração contínua                     |
| **DOCS**    | Mudanças na documentação                                        |
| **CLEANUP** | Remover trechos desnecessários                                  |
| **STYLE**   | Formatações de código                                           |

`Exemplo de uso:`
```
git commit -m "FEAT - CRUD de Usuarios"
```

<br>

**🔝 [Voltar ao Índice](#-%C3%ADndice)**

---

<br><br><br>

# 🖥️🛠️ 4. Bibliotecas Externas

## Algumas das Bibliotecas Externas usadas no Projeto
- Flask
- Numpy
- Opencv

### 1. Flask
Flask é um microframework para a web em Python.
Para instalar o Flask, use o seguinte comando:
```cmd
pip install Flask
```

### 2. Numpy
NumPy é uma biblioteca para computação científica com Python, oferecendo suporte para arrays e matrizes multidimensionais, além de funções matemáticas de alto nível.
Para instalar o NumPy, use o seguinte comando:
```cmd
pip install numpy
```

### 3. OpenCV
OpenCV é uma biblioteca de visão computacional que permite manipulação e análise de imagens.
Para instalar o OpenCV, use o seguinte comando:
```cmd
pip install opencv-python
```
<br>

Também precisaremos usar esta:
```cmd
pip install opencv-contrib-python
```

**⚠️ Nota:** Caso a IDE não consiga baixar alguma Biblioteca, basta das esse comando de pip install "nomeDaBiblioteca".

<br>

**🔝 [Voltar ao Índice](#-%C3%ADndice)**

---

<br><br><br>

# 🖥️ 5. Rodando a Aplicação Web

## ✅ Rodando o arquivo app.py

- Para iniciar a Aplicação Web, basta rodar o arquivo app.py, localizado na raiz do projeto.

<br>

**🔝 [Voltar ao Índice](#-%C3%ADndice)**

---

<br><br><br>

# 6. Entendendo o Cadastro de Imagens
Essa rota foi criada para facilitar o cadastro de novas Imagens para Treino. Para isto basta acessar a rota , pela navbar, clicando em `Cadastro` ou pela URL:
```
http://localhost:5000/img-treino/feedback?carregando=true
```

<br>

**⚠️ Nota:** Essas imagens estão configuradas para seguirem o nome colocado no arquivo `Imagem Controller` conforme imagem abaixo.

![image](https://github.com/user-attachments/assets/c298ce94-baf1-41f5-86ad-cd60dc7ff69f)

---

<br><br>

# 🛠️ 7. Passos para Treinar o Reconhecimento Facial
Depois de cadastrarmos as imagens, precisamos renomear elas com um identificador único e separar elas para treino e teste.

<br>

1. Vá até a pasta `Helpers`
2. Vá em renomear_fotos.py, note que os identificadores únicos vinculados está sendo configurado nesse trecho de código.
```python
alunos_ra = {
    "larissa": "123456", # Identificador é a Larissa, vinculado ao Identificador único 123456
    "wesley": "13713" # Identificador é o Wesley, vinculado ao Identificador único 13713
}
```

**⚠️ Nota:** Note que a intenção era utilizar o RA do Aluno, porém o modelo não consegue ter uma boa Acurrácia utilizando o RA, logo como solução foi usado um código aleatório para cada Aluno.

<br>

4. Execute o Script `renomear_fotos.py`
5. Execute o Script `distribuir_fotos_treino_praticas.py`
6. Execute o Script `treinamento-yale.py`
7. Execute o Script `teste-yale.py` - (Ao executar esse Script você será capaz de ver a Acurrácia obtida).

<br>

--- 

## 📝 7.1. Entendendo o Controller de Reconhecimento Facial
Note que no Controller do Reconhecimento Facial, temos a função `gerar_frames`, ela é responsável por mostrar na tela o nome da pessoa que está sendo reconhecida. Conforme abaixo:

<br> 

- Código de associação de Identificador único ao nome da Pessoa Identificada:
![image](https://github.com/user-attachments/assets/f79b0df3-c1c0-4ac1-be02-d83fa875d748)


- Imagem da Identificação para o usuário conseguir visualizar:


<br>
                            
---

<br><br>

# 🧑‍🦰 8. Reconhecimento Facial

- Para acessar o Reconhecimento Facial, execute a Aplicação Web:

- Basta executar o arquivo `app.py`.

- Ir em `Acessar Painel`

![image](https://github.com/user-attachments/assets/dbc65183-0843-4f58-b9d8-6f8ab26c20b2)

- Clicar em `Iniciar Reconhecimento Facial`

<br>

**📃✅ Caso dê certo o Reconhecimento:**

![image](https://github.com/user-attachments/assets/4f2137d5-91ad-4924-8642-0391e4f02205)

<br>

**📃❌ Caso dê Erro:**

![image](https://github.com/user-attachments/assets/36eab6fa-74da-4fb4-93ca-8a8f8df24c25)


<br>

**🔝 [Voltar ao Índice](#-%C3%ADndice)**

---

<br><br><br>

## 🖥️✔️ Tecnologias

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
- ![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

<br><br>

## 📌 Apêndices

## ✅ Verificar se o PIP está instalado e configurado:
O PIP é usado para baixar bibliotecas externas, como `cv2` (OpenCV), por isso precisamos verificar se ele está instalado no seu ambiente de trabalho.

### Verificando a instalação do PIP
1. Abra o Prompt de Comando e digite:
    ```cmd
    pip --version
    ```
2. Se o PIP estiver instalado corretamente, você verá uma mensagem com a versão do PIP instalada, algo parecido com:
    ```
    pip 21.0.1 from C:\Python39\lib\site-packages\pip (python 3.9)
    ```

### Caso o PIP não esteja instalado
Se você não vê a mensagem com a versão do PIP, siga os passos abaixo para adicioná-lo ao Path do sistema:

1. **Localize o diretório de instalação do Python**
   - Normalmente, o Python é instalado em um diretório semelhante a:
     ```
     C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python39
     ```
   - Substitua `Python39` pela versão específica do Python instalada no seu sistema.

2. **Encontre o diretório `Scripts`**
   - O PIP é instalado no subdiretório `Scripts` dentro do diretório do Python. O caminho completo será algo como:
     ```
     C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python39\Scripts
     ```

3. **Adicionar `Scripts` ao Path do Sistema**
   - Abra o Painel de Controle e vá para **Sistema e Segurança** > **Sistema** > **Configurações avançadas do sistema**.
   - Clique no botão **Variáveis de Ambiente**.
   - Na seção **Variáveis do sistema**, localize e selecione a variável `Path`, e clique em **Editar**.
   - Clique em **Novo** e cole o caminho do diretório `Scripts` que você copiou anteriormente:
     ```
     C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python39\Scripts
     ```
   - Clique em **OK** em todas as janelas para fechar e salvar as configurações.

4. **Verifique novamente a instalação do PIP**
   - Abra um novo Prompt de Comando e digite:
     ```cmd
     pip --version
     ```
   - Você deve agora ver a mensagem com a versão do PIP instalada.

### Resultado esperado
Quando o PIP está instalado corretamente, você deve ver algo semelhante a:
![Resultado esperado do comando pip --version](https://github.com/user-attachments/assets/874cb2fc-000a-40c0-a164-d9f801d74686)

<br>
