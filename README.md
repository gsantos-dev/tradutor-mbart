# 🧠 Tradutor Corporativo Offline com mBART

Este projeto é uma solução **inteligente e 100% offline** para **tradução automática de apresentações corporativas em PowerPoint**, utilizando o modelo mBART da Hugging Face e um dicionário técnico personalizado.

---

## 🚀 Visão Geral

O pipeline é capaz de:
- Ler arquivos `.pptx` (PowerPoint) com textos em português
- Traduzir de forma **inteligente** e **contextualizada** para o inglês
- Manter termos específicos usando um **vocabulário técnico**
- Funcionar **totalmente offline**, garantindo **segurança de dados**

Ideal para empresas que lidam com apresentações sensíveis e precisam de padronização linguística para clientes internacionais.

---

## 🧩 Funcionalidades

✔️ Extração de textos (horizontal e vertical) de slides PPTX  
✔️ Suporte a **tabelas e caixas de texto simultâneas**  
✔️ Tradução via modelo **mBART fine-tuned** com termos específicos  
✔️ Aplicação local com suporte a **GPU (opcional)**  
✔️ Pipeline completo: pré-processamento → tradução → reconstrução do arquivo traduzido  

---

## 🛠️ Tecnologias e Bibliotecas

- Python 3.10+
- [Transformers](https://huggingface.co/docs/transformers/index) (Hugging Face)
- `torch` (PyTorch)
- `pptx` (manipulação de slides)
- `sentencepiece`
- `openpyxl`
- `os`, `re`, `json`, `unicodedata`

---

## 📁 Estrutura dos Arquivos

| Arquivo | Descrição |
|--------|-----------|
| `Instalando_Modelo.py` | Baixa e configura o modelo mBART e o tokenizador |
| `Treinamento_Modelo.py` | Realiza o fine-tuning com dicionário técnico e corpus paralelo |
| `Transformando_EM_texto.py` | Extrai textos dos slides originais |
| `Chamando_Modelo_Treinado.py` | Traduz os textos e gera a apresentação traduzida |

---

## 📦 Requisitos

Crie um ambiente virtual e instale os pacotes:

```bash`
pip install -r requirements.txt`




## 🔒 Segurança e Privacidade
Este projeto não utiliza APIs externas e não transmite nenhum dado pela internet, tornando-o ideal para ambientes corporativos com regras de compliance e confidencialidade.

## 📄 Licença
Este projeto está licenciado sob a Apache License 2.0.
Você pode utilizá-lo comercialmente, modificar e redistribuir, desde que mantenha os avisos de direitos autorais.


# 👨‍💻 Autor
Guilherme Santos Pereira
