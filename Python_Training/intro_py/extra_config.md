# Encontrando a pasta de instalação da distribuição Anaconda.
  
- No menu iniciar, na pasta Anaconda3, clique na opção **Anaconda prompt (anaconda3)**

!!! warning Atenção
    Esse comando não funciona no **Anaconda powershell prompt (anaconda3)**

![](figs/atalho_extra_01.jpg)

- Na tela do  **prompt**, digite ```where anaconda```. O comando mostar o caminho para o arquivo anaconda.exe.

![](figs/atalho_extra_02.jpg)
   
## Montando o caminho do ambiente IDLE

- Use o caminho mostrado pelo comando até a pasta ```...\anaconda3\``` e complete o caminho com ```Lib\idlelib\idle.pyw``` ou ```\Scripts\idle.exe```


## Setting up on Windows

!!! note 
    The instructions below are based on Windows 10.

### IDLE

O IDLE é uma interface básica para programação do CPython. Idle, em inglês significa ocioso. Em computação pode significar que o processador já executou as instruções e aguarda novos comandos. Levando em consideração:

1. o senso de humor dos criadores do Python,
2. e que o nome da linguagem é uma homenagem ao grupo de humor [Monty Python](https://en.wikipedia.org/wiki/Monty_Python)

O nome deste ambiente pode ser uma homenagem a um dos membros do grupo, o ator, músico, escritor e comediante [Eric Idle](https://en.wikipedia.org/wiki/Eric_Idle).

A simplicidade da interface IDLE é uma vantagem quando se esta começando a programar pela linguagem Python. Podemos focar na lógica de programação e características da linguagem em uma interface sem muitas distrações ou necessidades de configuração.


#### Para acessar a interface IDLE da instalação Anaconda no Windows:

##### Criando um atalho para o IDLE

1. Clique com o botão direito na área de trabalho
   ![](figs/atalho_01.jpg)

2. coloque o caminho do atalho conforme instruções abaixo:
   ![](figs/atalho_02.jpg)

   - Quando a distribuição conda é instalada apenas para o usuário atual **(just me)** use:<br> ```%USERPROFILE%\anaconda3\Scripts\idle.exe``` <br> ou <br> ```%USERPROFILE%\anaconda3\Lib\idlelib\idle.pyw```<br><br>


   - Quando a distribuição conda é instalada para todos os usuários **(all users)**:<br> ```%PROGRAMDATA%\anaconda3\Scripts\idle.exe``` <br> ou <br> ```%PROGRAMDATA%\anaconda3\Lib\idlelib\idle.pyw``` <br><br>


    !!! warning
         Caso tenha instalado a distribuição em um outro caminho e não saiba qual, ou não tenha conseguido localizar o IDLE com as instruções acima, acesse o link:
         [Encontrando a pasta de instalação da distribuição Anaconda](./extra_config.md)

3.  Copie o caminho para o IDLE e clique em avançar
    ![](figs/atalho_03.jpg)

4. Clique em concluir

    ![](figs/atalho_04.jpg)

5. Execute o atalho e, na tela do IDLE, digite: ```print("hello, world")``` e aperte **enter**

    ![](figs/idle_hello_world.jpg)

## Instalando o Chocolatley (opcional)

Os sitemas operacionais baseados em Linux, bem como o MacOs, possuem aplicações de linha de comando para instalar *software*. Este tipo de recurso é muito prático na resolução de problemas e conflitos. Atualmente o Windows está testando um software do género, chamado Win-get. Enquanto o win-get não estiver suficientemente robusto, a melhor alternativa para este tipo de tarefa é um programa desenvolvido por terceiros, o **Chocolatey**.

Abra um terminal o **Windows PowerShell** como administrador. Para verificar as permissões de instalação de programas via powershell, digite e cole o código abaixo:

```Get-ExecutionPolicy```

Caso a resposta seja ```Restricted``` copie e cole o código abaixo:

```Set-ExecutionPolicy AllSigned```

Para instalar o **Chocolatey**, copie e cole o código abaixo:

``` Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) ```




## Instalando o gerenciador de pacotes Mamba (opcional)

A distribuição Anaconda instala uma aplicação de linha de comando ```conda```. Essa aplicação serve para gerenciar pacotes e ambientes no Python. Com o crescimento do número de pacotes a validação da compatibilidade dos pacotes via ```conda```, em alguns casos, apresenta alguma lentidão. Alternativamente uma outra aplicação de gerenciamento de pacotes desenvolvida pela comunidade tem apresentado maior velocidade na instalação e validação de pacotes. Essa aplicação chama-se ```Mamba```.

É possível instalar a aplicação ```Mamba```através da ```conda```. Clique no menu iniciar, na pasta Anaconda3, clique com o botão direito no **Anaconda prompt (anaconda3)**, clique em mais e escolha a opção **Executar como administrador**.

!!! Note Nota
    É sempre recomendado executar o **prompt** como administrador para instalar pacotes

![](figs/instala_pacote_01.jpg)

No **prompt**, digite:

``` conda install mamba -n base -c conda-forge ```

Aperte a tecla **enter** e siga as instruções de instalação e aguarde o final do processo.

![](figs/mamba_install.png)

