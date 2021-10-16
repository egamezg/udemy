# create variable nota that has 4.5
# create variable trabajo_realizado that has "si"
# calculate the value of "nota_final", if naota_final is greater or equal to 4
# and the value of "trabajo_realizado" is equal to "si", then the "nota_final" will
# be equal to "aprobado", in other case will be "suspenso"

nota = 4.5
trabajo_realizado = "si"

if nota >= 4 and trabajo_realizado == "si":
    nota_final = "aprobado"
    print(nota_final)
else:
    nota_final = "suspenso"
    print(nota_final)
