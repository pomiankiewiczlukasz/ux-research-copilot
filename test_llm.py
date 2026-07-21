from app.services.llm.ollama_service import ask_llm


answer = ask_llm(
    "Explain Retrieval Augmented Generation in two sentences."
)

print(answer)