import os
import pandas as pd
import requests
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
CHAVE_API = os.getenv("GEMINI_API_KEY")

if not CHAVE_API:
    raise ValueError("Chave de API não encontrada! Verifique o arquivo .env.")

genai.configure(api_key=CHAVE_API)
modelo = genai.GenerativeModel('gemini-1.5-flash')

# ==========================================
# 1. EXTRACT (Extração)
# ==========================================
print("Iniciando Extração de Dados via CoinGecko...")
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,chainlink&vs_currencies=usd&include_24hr_vol=true"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data).T
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'ativo', 'usd': 'preco_usd', 'usd_24h_vol': 'volume_24h'}, inplace=True)
    print("Extração concluída!\n")
else:
    raise Exception(f"Erro na extração: {response.status_code}")

# ==========================================
# 2. TRANSFORM (Transformação com IA)
# ==========================================
print("Iniciando Transformação Quantitativa com Gemini...")

def gerar_insight_quant(ativo, preco, volume):
    prompt = f"""
    Você é um algoritmo de análise de HFT (High-Frequency Trading).
    O ativo {ativo.upper()} está cotado a ${preco} com um volume de 24h de ${volume}.
    Gere apenas UMA frase curta e técnica de recomendação (ex: alerta de liquidez, tendência ou risco) para alimentar um robô de operações financeiras.
    """
    try:
        resposta = modelo.generate_content(prompt)
        # Retorna o texto gerado limpando espaços extras
        return resposta.text.strip()
    except Exception as e:
        return f"Erro na IA: {e}"

# Aplica a função para cada linha do DataFrame
df['insight_gemini'] = df.apply(lambda row: gerar_insight_quant(row['ativo'], row['preco_usd'], row['volume_24h']), axis=1)
print("Transformação concluída!\n")
print(df)

# ==========================================
# 3. LOAD (Carregamento)
# ==========================================
print("\nIniciando Carregamento (Salvando na Infraestrutura)...")
nome_arquivo = "insights_mercado_hft.csv"
df.to_csv(nome_arquivo, index=False)
print(f"Pipeline finalizado! Dados prontos para o robô no arquivo: {nome_arquivo} 🚀")
