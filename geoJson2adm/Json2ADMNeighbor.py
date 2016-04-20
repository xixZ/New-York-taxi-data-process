import json

fo = open("/home/sony/Data/border.adm", "wb")

json_data = open('NYNeighbor.json')
j = json.load(json_data)
json_data.close()

features = j['features']

for feature in features:
    new_record = '{'
    new_record += '"id": ' + str(feature['id']) + ', '
    new_record += '"neighbor_name": "' + feature['properties']['NTAName'] + '",'
    new_record += '"boro_code": ' + str(feature['properties']['BoroCode']) + ', '
    coors = feature['geometry']['coordinates'][0]
    if isinstance(coors[0][0], list):
        coors = coors[0]
    new_record += '"spatial_cell": polygon("'
    polygon = ""
    for coor in coors:
        polygon = str(coor[1]) + ',' + str(coor[0]) + ' ' + polygon
    new_record += polygon + '")}\n'
    fo.write(new_record)

fo.close()
