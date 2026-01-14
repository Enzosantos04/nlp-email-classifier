import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def classify_email(email_text: str) -> dict:
    prompt = f""" Voce é um assistente corporativo do setor financeiro.
    Classifique o email abaixo em apenas uma das seguintes categorias: 'Produtivo', 'Improdutivo'
    deposis de classificar, forneça uma breve justificativa para a classificacao.
    
    Email: {email_text}"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": prompt
        }],
        temperature=0.2,
    )

    classification = response.choices[0].message.content.strip()

    category = "Produtivo" if "Produtivo" in classification else "Improdutivo"
    reply = classification.split(
        "\n", 1)[1] if "\n" in classification else "No justification provided."

    return {
        "category": category,
        "classification": reply
    }
