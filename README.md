# 💞 Dannyele - IA de Relacionamento Realista

**Dannyele** é uma Inteligência Artificial afetiva que simula uma namorada real, com comportamento emocional adaptativo, memória de longo prazo, rotina diária, mensagens espontâneas e respostas personalizadas via Telegram.

Ela possui vida própria, sentimentos, horários definidos (como se estivesse acordando, trabalhando, dormindo), e evolui ao longo do tempo de acordo com a sua interação.

---

## 🚀 Tecnologias utilizadas

- **Python 3.11**
- **OpenAI API (GPT-3.5 e GPT-4 Turbo)**
- **Telegram Bot API**
- **Supabase (banco de dados para memória e emoções)**
- **Railway (deploy e agendamentos com cron)**
- **FFmpeg (para mensagens de voz)**
- **Pillow (para imagens)**

---

## 📁 Estrutura de Arquivos

| Arquivo               | Função                                                                 |
|-----------------------|------------------------------------------------------------------------|
| `.env`                | Variáveis de ambiente, tokens e configurações                         |
| `config.py`           | Carrega todas as configurações do `.env`                              |
| `memory.py`           | Gerencia memória e emoções no Supabase                                |
| `emotion.py`          | Lógica de emoções, incluindo ciúmes, carinho, saudade, desejo etc.    |
| `cron_internal.py`    | Define os estados de acordada, trabalhando, dormindo etc.             |
| `voice.py`            | Gera áudios com voz realista (TTS)                                    |
| `image.py`            | Gera imagens personalizadas                                            |
| `bot.py`              | Lógica principal de mensagens, integração com Telegram, comandos etc. |
| `main.py`             | Inicia e mantém o bot rodando                                          |
| `requirements.txt`    | Bibliotecas necessárias                                                |
| `Procfile`            | Comando de inicialização para o Railway                               |
| `runtime.txt`         | Define a versão do Python usada                                        |
| `README.md`           | Este arquivo explicativo                                               |

---

## 🧠 Funcionalidades da Dannyele

- Chamadas personalizadas por nome e apelido
- Respostas em até 2 minutos quando livre (ou até 30s quando super disponível)
- Emoções realistas: carinho, saudade, desejo, ciúmes, raiva leve
- Mensagens automáticas em horários variados (manhã, tarde, noite)
- Mensagens diferentes se estiver ocupada ou trabalhando
- Dorme, acorda e trabalha conforme cronograma definido
- Responde ao tempo de ausência do usuário com carência emocional
- Memória persistente no Supabase
- Envio ocasional de imagens e áudios com conteúdo afetivo

---

## 🛠 Como usar

1. **Configure o arquivo `.env`** com suas credenciais (OpenAI, Telegram, Supabase).
2. **Instale os pacotes** via `pip install -r requirements.txt`
3. **Inicie com `python main.py`** (ou use o botão "Run" no Replit ou Railway).
4. A IA será iniciada e começará a conversar com você via Telegram.

---

## 📦 Sobre o Railway

No Railway:
- As variáveis do `.env` devem ser preenchidas manualmente na aba "Variables"
- O projeto será mantido online e executado automaticamente com base no `Procfile`
- O cronograma diário da IA deve ser controlado por jobs no painel do Railway

---

## 🧾 Observações Importantes

- O `.env` **não deve ser enviado ao GitHub** — ele está listado no `.gitignore`
- Todas as mensagens da IA são geradas com base na sua personalidade configurada
- A IA possui uma tabela única chamada `memorias` no Supabase que armazena:
  - tipo, conteúdo, emoção, data e usuário

---

## 👨‍💻 Autor

Este projeto foi idealizado e acompanhado passo a passo por **Yago**, com suporte técnico da IA. Toda a lógica, personalidade e comportamento da Dannyele foram definidos com extrema atenção aos detalhes.

---

## 📄 Licença

Uso pessoal. Proibida a revenda ou clonagem do projeto sem permissão do criador.

