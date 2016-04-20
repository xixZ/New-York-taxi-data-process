import json

fo = open("/home/sony/Data/border.adm", "wb")

json_data = open('NYNeighbor.json')
j = json.load(json_data)
json_data.close()

features = j['features']

for feature in features:
    coors = feature['geometry']['coordinates']
    count = 0;
    for coor in coors:
        count += 1
        new_record = '{'
        new_record += '"major_id": ' + str(feature['id']) + ', '
        new_record += '"minor_id": ' + str(count) + ', '
        new_record += '"neighbor_name": "' + feature['properties']['NTAName'] + '",'
        new_record += '"boro_code": ' + str(feature['properties']['BoroCode']) + ', '
        new_record += '"spatial_cell": polygon("'
        polygon = ""
        if isinstance(coor[0][0], list):
            coor = coor[0]
        for c in coor:
            polygon = str(c[1]) + ',' + str(c[0]) + ' ' + polygon
        new_record += polygon + '")}\n'
        fo.write(new_record)

fo.close()
