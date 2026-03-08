# 📈 Quant ETL Pipeline: Monitorização HFT com Gemini AI

Este projeto é um pipeline de dados (ETL) focado na análise de ativos financeiros de alta volatilidade, desenhado para simular a ingestão de dados num sistema de *High-Frequency Trading* (HFT) e *MLOps*.

## 🧠 Arquitetura do Pipeline

1. **Extract (Extração):** Consome dados em tempo real da API RESTful do CoinGecko, recolhendo preço e volume (24h) de ativos chave (BTC, ETH, SOL, LINK).
2. **Transform (Transformação):** Integra a API do **Google Gemini (LLM)** para analisar os dados instantaneamente e gerar um *insight* técnico ou alerta de risco para robôs de trading.
3. **Load (Carregamento):** Exporta o DataFrame final, já com a análise de sentimento/risco da IA, para um ficheiro `.csv` estruturado, pronto para ser consumido por algoritmos de execução.

## 🛠️ Tecnologias e Práticas Utilizadas
- **Python:** Lógica principal e orquestração.
- **Pandas:** Manipulação e estruturação de *DataFrames*.
- **Google Generative AI (Gemini):** Motor de inferência para análise quantitativa.
- **Dotenv:** Proteção de credenciais e variáveis de ambiente (Segurança MLOps).

## 🚀 Como Executar

1. Clona este repositório.
2. Instala as dependências: `pip install pandas requests google-generativeai python-dotenv`.
3. Cria um ficheiro `.env` na raiz do projeto com a tua chave: `GEMINI_API_KEY="tua_chave"`.
4. Executa o ficheiro principal: `python etl_hft_gemini.py`.

---
*Desenvolvido por [Geilson Costa Freitas Cabral](https://github.com/Pingoliro) - Focado em Infraestrutura de IA e HFT.*
# quant-etl-gemini
