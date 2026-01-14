import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def classify(email_content: str) -> dict:
    if not email_content.strip():
        return {
            "category": "Erro",
            "classification": "Email vazio."
        }

    prompt = f"""
Você é um assistente corporativo do setor financeiro.

Classifique o email abaixo em APENAS uma das categorias:
- Produtivo
- Improdutivo

Responda EXATAMENTE neste formato (sem texto extra):

Categoria: <Produtivo ou Improdutivo>
Justificativa: <breve explicação>

Email:
{email_content}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=150
    )

    content = response.choices[0].message.content.strip()
    lines = content.splitlines()

    category = lines[0].split(":", 1)[1].strip()
    justification = lines[1].split(":", 1)[1].strip()

    return {
        "category": category,
        "classification": justification
    }
