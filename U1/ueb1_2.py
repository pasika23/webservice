import uvicorn
from fastapi import FastAPI
from pyproj import Transformer
import pyproj

app = FastAPI()

lv95 = "EPSG:2056"
wgs84 = "EPSG:4326"

t1 = Transformer.from_crs(wgs84,lv95)

start_lng = 7.6419551137223078
start_lat = 47.53487677458141

end_lng = -122.47864020149932
end_lat = 37.81951340907846

@app.get("/wgs84lv95")
async def transform(lng: str, lat: str):
    return { "type": "Point",
            "coordinates": t1.transform(lat,lng)
}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

