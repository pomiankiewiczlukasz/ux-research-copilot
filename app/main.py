from fastapi import FastAPI


app = FastAPI(
    title="UX Research Copilot",
    description="AI assistant for UX research analysis",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "UX Research Copilot is running 🚀"
    }