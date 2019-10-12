arquivo = 'zlen.txt'
#----------------------------------------------------------------
horas = 0
minutos = 0
segundos = 0

with open(arquivo, 'r') as file:
    times = file.readlines()
    for time in times:
        if time.find('\n') != -1:
            time = time.replace('\n', '')
        mins = time.split(':')[0]
        segs = time.split(':')[1]
        minutos += int(mins)
        segundos += int(segs)
        #print(time, 'mins:', mins, 'segs:', segs)
        #print('minutos:', minutos, 'segundos:', segundos)

minutos_s = segundos//60
segundos_s = segundos%60
minutos += minutos_s
segundos = segundos_s
#print(minutos_s)
#print(segundos_s)


horas_m = minutos//60
minutos_m = minutos%60
horas += horas_m
minutos = minutos_m
#print(horas_m)
#print(minutos_m)


print('horas    :', horas)
print('minutos  :', minutos)
print('segundos :', segundos)
