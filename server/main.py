from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(openapi_url="/openapi.json", docs_url="/docs")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    # res = requests.get("http://localhost:7000")
    # return {"Python": "success", "healthCheck": json.loads(res.content)}
    return "OK"


@app.get("/health-check")
def health_check():
    return "OK"
