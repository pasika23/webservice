from pyproj import Transformer
import pyproj

lv95 = "EPSG:2056"
wgs84 = "EPSG:4326"

t1 = Transformer.from_crs(wgs84,lv95)
t2 = Transformer.from_crs(lv95,wgs84)

r1 = t1.transform(47.53487677458141, 7.6419551137223078)
print(r1)


start_lng = 7.6419551137223078
start_lat = 47.53487677458141

end_lng = -122.47864020149932
end_lat = 37.81951340907846

g = pyproj.Geod(ellps='WGS84')

r = g.npts(start_lng,start_lat,end_lng,end_lat,10)
print(r)

r2 = []
for x in r:
    r2.append([x[0],x[1]])
alles = list([start_lng,start_lat] + r + [end_lng,end_lat])


geojson = f"""
{{
    'type': 'Feature',
    'geometry': {{
        'type': 'MultiPoint',
        'coordinates': {alles}
    }}

}}"""