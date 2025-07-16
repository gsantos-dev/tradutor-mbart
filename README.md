markdown# 🧠 Tradutor de Apresentações Empresariais com mBART

Este projeto implementa um **tradutor de apresentações PowerPoint (PPTX)** baseado no modelo **mBART** da Hugging Face, adaptado para funcionar **offline** e com foco em traduções empresariais de **português para inglês**.

## ✨ Principais Funcionalidades

- 🔄 **Tradução Automática de PPTs**: Caixas de texto horizontais e verticais, tabelas e elementos empresariais com layout e formatação preservados
- 🎯 **Treinamento Personalizado**: Usa seus próprios arquivos como base, mantendo termos técnicos e dicionários internos
- 🔒 **Execução Local & Offline**: Segurança de dados sensíveis garantida, ideal para ambientes corporativos restritos
- 🤖 **Modelo Customizável**: Treina com seus próprios PPTs traduzidos para melhor precisão

---

### 📋 Descrição das Pastas

| 📁 Pasta/Arquivo | 📝 Descrição |
|------------------|--------------|
| `Input_PPTS/` | Apresentações originais em português |
| `Output_PPTS/` | Arquivos PPTX traduzidos automaticamente |
| `PPTs_pt/` | Caixas de texto extraídas dos slides (PT) |
| `PPTs_en/` | Traduções dos textos em inglês |
| `Texto_pt/` | Texto puro extraído dos slides em português |
| `Texto_en/` | Traduções finais em texto puro (EN) |
| `save_data/` | Modelos treinados, checkpoints e tokenizer |
| `Modelo_Mbart_Treinado/` | Versão final do modelo ajustado (mBART) |

### 🐍 Scripts Principais

| 📄 Script | ⚙️ Função |
|-----------|----------|
| `Intalando_Modelo.py` | Instalação e download do mBART |
| `Transformando_EM_texto.py` | Extração de texto dos slides |
| `Treinamento_Modelo.py` | Fine-tuning com seus próprios dados |
| `Chamando_Modelo_Treinado.py` | Tradução de novos conteúdos |

---

## 📦 Instalação

> **Requisitos**: Python 3.10+, pip, Git, PowerPoint instalado (para manipulação de arquivos .pptx)

### 1. Clone o repositório:
```bash``
git clone https://github.com/gsantos-dev/tradutor-mbart.git``
cd tradutor-mbart

### 2. Crie o ambiente virtual:
bash python -m venv venv
venv\Scripts\activate

### 3. Instale as dependências:
pip install -r requirements.txt

### 🚀 Como Usar
## 1. Instalar modelo base do mBART
bash python Intalando_Modelo.py
## 2. Extrair textos dos arquivos PPTX
##bash python Transformando_EM_texto.py
## 3. Treinar o modelo com seus pares de tradução
bash python Treinamento_Modelo.py
## 4. Traduzir novos arquivos
bash python Chamando_Modelo_Treinado.py

## 🗃️ Estrutura de Pastas

### 📥 Pastas de Entrada
- **`Input_PPTS/`** - Arquivos .pptx em português (originais)

### 📤 Pastas de Saída  
- **`Output_PPTS/`** - Traduções finais em .pptx (automático)

### 🔄 Processamento de Texto
- **`Texto_pt/`** - Texto extraído dos slides em PT
- **`Texto_en/`** - Traduções correspondentes para treinamento/teste

### 🤖 Modelo e Dados
- **`save_data/`** - Armazena tokenizer, modelo e checkpoints treinados

---

## 🔒 Segurança e Privacidade

## ✅ Nenhum dado é enviado para servidores externos ou terceiros
## ✅ Ideal para empresas com políticas restritas de rede
## ✅ Treinamento e inferência são 100% locais


### 📄 Licença
Distribuído sob a Apache License 2.0.
Você pode usá-lo comercialmente, modificá-lo e redistribuí-lo, desde que mantenha os créditos.

👨‍💻 Autor
Guilherme Santos Pereira


### ⚡ Este projeto é um exemplo de como aplicar IA generativa e modelos de linguagem em um contexto corporativo real, com foco em segurança, automação e escalabilidade.
