fo = open("taxi_part.adm", "wb")

with open('taxi.adm', 'rb') as f:
    count = 0
    for row in f:
        count += 1
        fo.write(row)
        if count >= 6000000:
            break
        if count % 1000000 == 0:
            print count
    print count
f.close()
fo.close()
