from fastapi import FastAPI
from fastapi import responses
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))

@app.get("/addiere")
async def addiere(a: int = 0, b: int = 0):
    return {"resultat": a+b}

@app.get("/")
async def root():
    return {"Version": "1.0"}
 
@app.get("/hallo")
async def root():
    return {"Hallo": "World"}

@app.get("/bild")
async def bild():
    return responses.FileResponse("static/1539163272-01_IIM7682_byIngemarImboden.jpg-1400x726.jpeg")

@app.get("/web")
async def web():
    return responses.HTMLResponse("<h1>Titel</h1><img src='static/1539163272-01_IIM7682_byIngemarImboden.jpg-1400x726.jpeg' width='30%' />")


uvicorn.run(app, host="127.0.0.1", port=8000)