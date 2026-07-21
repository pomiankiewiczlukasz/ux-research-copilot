import ollama


MODEL_NAME = "qwen2.5:7b"


def ask_llm(prompt: str):

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]