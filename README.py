#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar ` configurar o GRUB` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar `configurar o GRUB` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to configure/install/usar `configure the GRUB` on `Linux Ubuntu`._

# ## Descrição
# 
# ### `GRUB (Grand Unified Bootloader)`
# 
# O GRUB (Grand Unified Bootloader) é um carregador de inicialização multissistema muito utilizado em sistemas operacionais baseados em Unix, como Linux e FreeBSD. Sua função principal é gerenciar o processo de boot do computador, permitindo que o usuário escolha entre diferentes sistemas operacionais instalados ou diferentes versões de um mesmo sistema. O GRUB se destaca por sua flexibilidade e capacidade de personalização, oferecendo suporte a diversos sistemas de arquivos e possuindo recursos como a detecção automática de outros sistemas operacionais e a capacidade de modificar parâmetros de inicialização em tempo real. Ele substituiu o LILO (Linux Loader) como o carregador de boot padrão em muitas distribuições Linux, devido à sua maior facilidade de configuração e robustez
# 

# ## 1. Configurar o GRUB do `Linux Ubuntu` [1]
# 
# **ATENÇÂO**: Tenha em mente que o `GRUB` deve ser instalado no primário da sequência de `boot`, logo, se ele for instalado em outro disco, este, por sua vez, deve ser alterado para ser o primeiro disco na inicialização do computador.
# 
# ### 1.1 Atualizar o Sistema Operacional (SO)
# 
# Para editar o arquivo de configuração do GRUB no Linux, você geralmente trabalhará com o arquivo /etc/default/grub. Este arquivo contém as configurações principais do GRUB, permitindo personalizar o processo de boot do sistema. Aqui está um guia passo a passo sobre como editá-lo:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# 3. Abra o arquivo com um editor de texto: Geralmente, usa-se um editor como o `nano` ou `vim`. Por exemplo, para usar o `nano`, você digitaria: `sudo nano /etc/default/grub`
# 
# Lembre-se de que você precisa de privilégios de superusuário para editar este arquivo, por isso usamos `sudo`.
# 
# 4. **Edite as configurações conforme necessário:** No arquivo, você encontrará várias opções, como `GRUB_TIMEOUT`, que define o tempo de espera antes do boot padrão, e `GRUB_CMDLINE_LINUX_DEFAULT`, onde você pode adicionar parâmetros do kernel. Abaixo, tem-se uma configuração padrão sugerida:
# 
#     ```
#     # If you change this file, run 'update-grub' afterwards to update
#     # /boot/grub/grub.cfg.
#     # For full documentation of the options in this file, see:
#     #   info -f grub -n 'Simple configuration'
# 
#     GRUB_DEFAULT="0"
#     GRUB_TIMEOUT_STYLE="menu"
#     GRUB_TIMEOUT="10"
#     GRUB_DISTRIBUTOR="`lsb_release -i -s 2> /dev/null || echo Debian`"
#     GRUB_CMDLINE_LINUX_DEFAULT="noquiet nosplash resume=UUID=<seu-uuid-de-swap>"
#     # GRUB_CMDLINE_LINUX=""
# 
#     # Uncomment to enable BadRAM filtering, modify to suit your needs
#     # This works with Linux (no patch required) and with any kernel that obtains
#     # the memory map information from GRUB (GNU Mach, kernel of FreeBSD ...)
#     # GRUB_BADRAM="0x01234567,0xfefefefe,0x89abcdef,0xefefefef"
# 
#     # Uncomment to disable graphical terminal (grub-pc only)
#     # GRUB_TERMINAL=console
# 
#     # The resolution used on graphical terminal
#     # note that you can use only modes which your graphic card supports via VBE
#     # you can see them in real GRUB with the command `vbeinfo'
#     # GRUB_GFXMODE=640x480
# 
#     # Uncomment if you don't want GRUB to pass "root=UUID=xxx" parameter to Linux
#     # GRUB_DISABLE_LINUX_UUID=true
# 
#     # Uncomment to disable generation of recovery mode menu entries
#     # GRUB_DISABLE_RECOVERY="true"
# 
#     # Uncomment to get a beep at grub start
#     # GRUB_INIT_TUNE="480 440 1"
# 
#     GRUB_DISABLE_OS_PROBER="false"
#     GRUB_COLOR_NORMAL="light-gray/black"
#     GRUB_COLOR_HIGHLIGHT="magenta/black"
#     ```

# 5. **Salve as alterações:** No `nano`, você faz isso pressionando `Ctrl+O` para salvar e depois `Ctrl+X` para sair. Se estiver usando `vim`, salve com `:w` e saia com `:q`.
# 
# 6. **Atualize o GRUB:** Após salvar suas alterações, você precisa atualizar a configuração do GRUB para que as alterações entrem em vigor. Isso é feito com o comando: `sudo update-grub`
# 
# 7. Reinicie o sistema: Para verificar as alterações, reinicie o sistema.
# 
# Lembre-se de ser cuidadoso ao editar as configurações do GRUB, pois erros podem afetar o processo de boot do seu sistema. Se você não tem certeza sobre uma configuração, é recomendável procurar mais informações ou consultar a documentação relevante.
# 

# ## 1.1 Código completo para configurar/instalar/usar 
# 
# Para configurar/instalar/usar o `GRUB Customizer` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***GRUB: Carregador de inicialização multifuncional.*** Disponível em: <https://chat.openai.com/c/4e8aa5fa-7954-4191-976a-7d81731aac10> (texto adaptado). ChatGPT. Acessado em: 09/11/2023 16:38.
