from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Higgspiels clone backend running ✅"}

@app.post("/ai")
def ai_generate(prompt: str):
    # Sementara pakai dummy response
    response = f"AI output untuk prompt: {prompt}"
    return {"result": response}
