import uvicorn
from fastapi import FastAPI

app = FastAPI()

d = {}
file = open("U1\PLZO_CSV_LV95.csv", encoding="utf-8")
next(file)

for line in file:
    data = line.strip().split(";")
    gde = data[3]
    plz = data[1]
    bfs = data[4]
    kanton = data[5]
    east = data[6]
    north = data[7]
    sprache = data[8]
    d[gde] = {"PLZ": plz,
              "Gemeinde": gde,
              "Kanton": kanton,
              "BFS": bfs,
              "E": east,
              "N": north,
              "Sprache": sprache}


file.close()

@app.get("/search")
async def search(gde: str):
    if gde in d:
        return d[gde]
    else:
        return {"error": "not found"}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)