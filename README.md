# ChatBot em PyQt5

Este é um projeto de chatbot construído usando **PyQt5** para criar uma interface gráfica de usuário (GUI) e **markdown2** para converter respostas em Markdown em HTML. O chatbot exibe as interações de maneira simples e intuitiva, com mensagens do usuário e do bot aparecendo em "balões" de chat estilizados.

## Funcionalidades

- **Interface de usuário**:
  - Caixa de entrada para o usuário digitar perguntas.
  - Área de chat onde as mensagens são exibidas em balões.
  - Botão "Enviar" para enviar perguntas, com mudança de estilo ao clicar ou pairar.
  - As mensagens do usuário aparecem à direita, e as do chatbot à esquerda.

- **Markdown para HTML**: As respostas do chatbot são estilizadas usando **Markdown**, convertendo-as para HTML.

- **Atalhos de teclado**: Suporte ao envio de mensagens ao pressionar a tecla **Enter** ou **Return**.

## Tecnologias Utilizadas

- **Python 3**
- **PyQt5**: Para criar a interface gráfica.
- **markdown2**: Para converter texto em Markdown para HTML.
  
## Estrutura do Projeto

- `main.py`: Contém a função `perg_resp` responsável por gerar as respostas do chatbot.
- `interface.py`: Implementa a interface gráfica e as interações do chatbot.

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/chatbot-pyqt5.git
