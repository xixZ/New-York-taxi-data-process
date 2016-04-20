import json

fo = open("border.adm", "wb")

json_data = open('borough.json')
j = json.load(json_data)
json_data.close()
features = j['features']


for feature in features:
    newCell = "{"
    prop = feature['properties']
    boro_code = prop["BoroCode"]
    boro_name = prop['BoroName']
    coors = feature['geometry']['coordinates'][0]
    newCell += "\"boro_code\": " + str(boro_code) + ', '
    newCell += "\"boro_name\": string(\"" + boro_name + '\"), '
    newCell += "\"cell\": polygon(\""
    for coor in coors:
        newCell += str(coor[0]) + ',' + str(coor[1]) + ' '
    newCell += "\")}\n"
    fo.write(newCell)
fo.close()
