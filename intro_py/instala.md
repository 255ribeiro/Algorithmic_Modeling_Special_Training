# Instalação do Python

A distribuição oficial do CPython pode ser encontrada na página da Python Foundation, [Python.org](https://www.python.org/). Embora este seja um material rico sobre a linguagem, neste curso vamos utilizar a distribuição **Anaconda**.

## Instalação da distribuição Anaconda

**Anaconda** é uma distribuição do Python orientada para programação científica e análise de dados. A página oficial da distribuição é [anaconda.com](https://www.anaconda.com)

![anaconda inc](figs/anaconda_inc.png)

 O instalador da versão individual (gratuita) pode ser baixada no link: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual). Ou pelo menu **Products**, opção **Individual Edition**.

![anaconda individual](figs/InkedanacondaIndividual_LI.jpg)

Clique no link de download para baixar o instalador. Certifique-se de baixar o executável compatível com seu sistema operacional.

![anaconda individual](figs/Inkedanaconda_download_LI.jpg)

## Instalação no Windows

Siga as instruções:

1. Execute o instalador
    ![instala](figs/Inkedinstalador_01.jpg)
1. Concorde com os termos do serviço. clique em **I Agree**.
    ![instala](figs/Inkedinstalador_02.jpg)
2. Instalar para o usuário atual do computador ou para todos os usuários. O padrão é apenas para o usuário atual **(just me)**. Escolha sua opção e clique em **Next**.
    ![instala](figs/Inkedinstalador_03.jpg)
3. Escolha a pasta da instalação e clique em **Next**.
    ![instala](figs/Inkedinstalador_04.jpg)
4. Opções de instalação. Não é recomendado marcar a primeira opção.Pode-se marcar a segunda opção. clique em instalar e aguarde o final do processo. 
    ![instala](figs/Inkedinstalador_05.jpg)

## Preparando o ambiente no Windows

!!! note Nota
    As instruções abaixo são baseadas no Windows 10.

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



#### FIM
