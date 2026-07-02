# 🎮 Xama no Brawl

<p align="center">
  <img width="650" alt="banner" src="assets/telainicial/logo_brawl.png">
</p>

<p align="center">
  <strong>Um jogo PvP 1v1 inspirado em Brawl Stars, desenvolvido em Python utilizando Pygame.</strong>
</p>

<p align="center">
  Projeto desenvolvido com foco em arquitetura modular, animações, gerenciamento de estados, colisão, mapas interativos e gameplay competitivo local.
</p>

---

# 📌 Sobre o Projeto

**Xama no Brawl** é um jogo inspirado em <img alt="Brawl Stars"/> Brawl Stars, desenvolvido inteiramente em **Python** com a biblioteca Pygame.

O jogo possui uma experiência completa com fluxo de navegação entre telas, seleção de personagens e sistema de combate competitivo local entre dois jogadores.

A proposta foi recriar parte da identidade do Brawl Stars adaptando a experiência para um jogo desktop 2D com mecânicas próprias.

---

# ✨ Principais Funcionalidades

## 🎬 Tela Inicial Animada

Sistema de abertura com múltiplas etapas de animação:

* Fade In inicial
* Efeito de queda e ricochete da logo
* Sistema de respiração (scaling animation)
* Botão de iniciar piscando
* Possibilidade de pular animações

---

## 👥 Seleção de Personagens

Tela dedicada para escolha dos personagens antes da partida.

Atualmente disponíveis:

* Shelly
* Piper
* Colt
* Iyoda

Recursos presentes:

* Navegação independente para cada jogador
* Confirmação individual
* Feedback visual de confirmação
* Sprites carregados dinamicamente
* Interface animada

---

## ⚔️ Sistema de Combate

Partida local **1v1** com sistema competitivo.

Mecânicas:

* Melhor de 3 rounds
* Sistema de vida
* Sistema de munição
* Tempo de recarga automática
* Sistema de projéteis
* Colisão com paredes
* Alcance máximo das balas
* Sistema de respawn entre rounds

---

## 🗺️ Sistema de Mapa

Mapa criado utilizando:

* Editor Tiled
* Arquivo `.tmx`
* Sistema de leitura via PyTMX

Camadas implementadas:

* Walls → colisão sólida
* Water → área bloqueada
* Bush → sistema de invisibilidade parcial

---

## 🎁 Sistema de Itens Coletáveis

Itens spawnam dinamicamente no mapa.

Atualmente disponíveis:

❤️ Life Orb
Aumenta vida do jogador

💥 Damage Orb
Aumenta dano do disparo

⚡ Speed Orb
Aumenta velocidade de movimentação

Sistema implementado:

* Spawn seguro
* Verificação contra colisão em paredes
* Verificação contra água
* Verificação contra arbustos
* Reposição automática após coleta

---

# 🧠 Mecânicas Implementadas

✔ Sistema de colisão
✔ Movimento em 8 direções
✔ Sistema de projéteis
✔ Sistema de dano
✔ Sistema de rounds
✔ Sistema de vitória
✔ HUD individual dos jogadores
✔ Sistema de buffs temporários por rodada
✔ Ocultação em arbustos
✔ Reinício da partida
✔ Retorno para seleção de personagens

---

# 🏗 Arquitetura do Projeto

```bash
Projeto/
│
├── assets/
│   │
│   ├── coletaveis/
│   │   ├── orb_vida.png
│   │   ├── orb_dano.png
│   │   └── orb_velocidade.png
│   │
│   ├── colt/
│   ├── iyoda/
│   ├── piper/
│   ├── shelly/
│   │
│   ├── telainicial/
│   │
│   ├── telaselecao/
│   │
│   ├── mapa_brawl.tmx
│   └── Map (10).png
│
├── game.py
├── itens.py
├── main.py
├── mapa.py
├── personagens.py
├── players.py
├── settings.py
├── tela_inicial.py
├── tela_selecao.py
├── utils.py
└── instructions.md
```

---

# 🛠 Tecnologias Utilizadas

Linguagem:

* Python 3

Bibliotecas:

* Pygame
* PyTMX

Ferramentas:

* Visual Studio Code
* Tiled Map Editor

---

# 🎮 Controles

## Player 1

| Ação           | Tecla |
| -------------- | ----- |
| Mover esquerda | A     |
| Mover direita  | D     |
| Mover cima     | W     |
| Mover baixo    | S     |
| Atirar         | SPACE |

---

## Player 2

| Ação           | Tecla |
| -------------- | ----- |
| Mover esquerda | ←     |
| Mover direita  | →     |
| Mover cima     | ↑     |
| Mover baixo    | ↓     |
| Atirar         | ENTER |

---

# 🚀 Como Executar

## 1. Criar ambiente virtual

```bash
python -m venv venv
```

## 2. Ativar ambiente virtual

```bash
.\venv\Scripts\Activate.ps1
```

Caso ocorra erro no PowerShell:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

## 3. Instalar dependências

```bash
pip install pygame pytmx
```

## 4. Executar o projeto

```bash
python main.py
```

---

# 📷 Fluxo do Jogo

```text
Tela Inicial Animada
        ↓
Seleção de Personagens
        ↓
Partida 1v1
        ↓
Sistema Melhor de 3
        ↓
Tela de Vitória
        ↓
Reiniciar OU Voltar à Seleção
```

---

# 💡 Conceitos Trabalhados

Durante o desenvolvimento foram aplicados conceitos importantes de programação:

* Programação Orientada a Objetos
* Modularização
* Game Loop
* Gerenciamento de Estados
* Sistema de Colisão
* Manipulação de Sprites
* Eventos em tempo real
* Física básica de projéteis
* Arquitetura escalável
* Clean Code
* Separação de responsabilidades

---

# 👨‍💻 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de aprofundar conhecimentos em:

* Desenvolvimento de jogos
* Programação em Python
* Estruturação de projetos grandes
* Organização de código modular
* Design de gameplay competitivo

---

<p align="center">
  Feito com Python, Pygame e muito café ☕
</p>