<<<<<<< HEAD
# 🎮 CIn Brawl

Jogo desenvolvido em **Python + Pygame** como projeto da disciplina de **Introdução à Programação** (1º período) do **Centro de Informática (CIn) - UFPE**.

CIn Brawl é um jogo de combate 1v1, local e por turnos de ação em tempo real, inspirado em *Brawl Stars*. Dois jogadores escolhem seus personagens e se enfrentam em um mapa com diversos obstáculos, arbustos para se esconder e itens que concedem vantagens, em uma disputa de melhor de 3 rodadas.

## 📖 Sobre o projeto

O jogo foi construído como forma de aplicar, na prática, os principais conceitos vistos ao longo do período: estruturas condicionais e de repetição, funções, listas, dicionários e orientação a objetos (classes e herança).

## ✨ Funcionalidades

- **Modo 2 jogadores (local utilizando o mesmo teclado)**, cada um com seu próprio conjunto de controles.
- **4 personagens jogáveis**: Shelly, Piper, Colt e Iyoda, cada um com sprites próprios de movimentação.
- **Tela inicial** e **tela de seleção de personagens** com animações e confirmação individual de cada jogador.
- **Sistema de tiro** com munição limitada (4 balas) e recarga automática por tempo.
- **Mapa interativo** carregado a partir de um arquivo `.tmx` (Tiled Map Editor), com:
  - **Paredes**, que bloqueiam o movimento e os projéteis;
  - **Água**, que impede a passagem dos jogadores;
  - **Arbustos**, que escondem o jogador (e o "camuflam" no HUD) quando ele está suficientemente coberto.
- **Itens coletáveis** que reaparecem aleatoriamente pelo mapa:
  - 💚 **Vida**: adiciona e/ou recupera 1 ponto de vida (até o máximo);
  - 💥 **Dano**: aumenta o dano dos projéteis (até 3 níveis);
  - ⚡ **Velocidade**: aumenta a velocidade de movimento (até 3 níveis).
- **HUD completo** com vida, munição, bônus de dano/velocidade e placar de rodadas.
- **Sistema de rodadas**: vence a partida quem ganhar **2 rodadas** primeiro; ao final de uma rodada os personagens são reposicionados e os itens redistribuídos.
- **Tela de fim de jogo** com opção de reiniciar o campeonato ou voltar à tela de seleção de personagens.

## 🕹️ Controles

| Ação                | Player 1 (Azul)      | Player 2 (Vermelho)      |
|----------------------|-----------------------|----------------------------|
| Mover cima/baixo/esq/dir | `W` `A` `S` `D`  | `↑` `↓` `←` `→`         |
| Atirar               | `ESPAÇO`              | `ENTER`                    |
| Selecionar personagem | `A` / `D`             | `←` / `→`                  |
| Confirmar personagem  | `ESPAÇO`              | `ENTER`                    |
| Sair do jogo          | `ESC`                 | `ESC`                      |

Na tela de fim de jogo:
- `R` — reinicia o campeonato (placar zerado, mesmos personagens);
- `T` — volta para a tela de seleção de personagens.

## 🗂️ Estrutura do projeto

```
projeto-ip-brawl/
├── main.py            # Ponto de entrada do jogo
├── game.py             # Loop principal, regras de partida e HUD
├── players.py          # Classe Player e subclasses Player1/Player2
├── personagens.py      # Dicionário com os personagens disponíveis
├── itens.py             # Classes Item (coletáveis) e Projectile (balas)
├── mapa.py              # Carregamento do mapa .tmx e áreas de colisão
├── tela_inicial.py     # Tela inicial do jogo
├── tela_selecao.py     # Tela de seleção de personagens
├── settings.py          # Configurações gerais (resolução da tela)
├── utils.py              # Funções utilitárias
└── assets/                # Sprites, mapa, fontes e imagens de UI
```

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Pygame](https://www.pygame.org/) — engine do jogo
- [PyTMX](https://github.com/bitcraft/PyTMX) — leitura de mapas criados no [Tiled Map Editor](https://www.mapeditor.org/)

## 🚀 Como rodar o projeto

### Pré-requisitos
- Python 3 instalado
- Git (opcional, para clonar o repositório)

### Passo a passo (Windows)

1. Clone o repositório:
   ```bash
   git clone https://github.com/carolinaacalderaro/projeto-ip-brawl.git
   cd projeto-ip-brawl
   ```

2. Crie um ambiente virtual:
   ```powershell
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   > Se ocorrer erro de permissão no PowerShell, rode antes:
   > ```powershell
   > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   > ```

4. Instale as dependências:
   ```bash
   pip install pygame pytmx
   ```

5. Execute o jogo:
   ```bash
   python main.py
   ```

## 📌 Como jogar

1. Na tela inicial, pressione a tecla indicada para começar.
2. Cada jogador escolhe seu personagem (setas/`A`-`D`) e confirma (`ESPAÇO`/`ENTER`).
3. Movam-se pelo mapa, colidam com itens para ganhar vantagens e usem os arbustos para se esconder do adversário.
4. Atirem no oponente para reduzir sua vida — quem chegar a 0 de vida perde a rodada.
5. Vence o jogo quem ganhar **2 rodadas**.

## 👥 Autoria

Projeto desenvolvido para a disciplina de Introdução à Programação — CIn/UFPE.

## 📄 Licença

Projeto acadêmico, desenvolvido para fins educacionais.
=======
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

# 🔄 Melhorias Futuras

Atualmente planejado:

* [ ] Corrigir velocidade diagonal
* [ ] Melhorar HUD
* [ ] Reformular placar
* [ ] Melhorar tela de vitória
* [ ] Melhorar seleção de personagens
* [ ] Ícones no HUD para buffs
* [ ] Balanceamento de vida dos personagens
* [ ] Melhorar feedback visual dos rounds
* [ ] Efeitos sonoros
* [ ] Música de fundo
* [ ] Animações de tiro
* [ ] Diferenciar atributos por personagem

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
>>>>>>> 1477cec0e8afd8503e8b6494fa25546efeba9cdc
