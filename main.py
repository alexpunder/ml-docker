from fastapi import FastAPI


app = FastAPI(
    title="Простой сервис для работы с Docker.",
    docs_url="/",
)

@app.get("/healthcheck")
def healthcheck():
    return {"success": True}
