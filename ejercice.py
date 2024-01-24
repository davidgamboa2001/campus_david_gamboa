nombre= input(' porfavor ingresa tu nombre ')
print('hola ', nombre)

edad=int(input('ingresa tu edad para saber si puedes votar'))


if edad > 18:
    print('puedes ingresar al voto')
else:
    print('lo siento no puedes votar ')


calificacion=int(input('ingrese su nota para saber su calificacion'))

if calificacion <=70 :
    print('su nota es de D')
elif calificacion <=80 :
    print(' su calificacion es de C')
elif calificacion <=90 :
    print(' su calificacion es de B')
elif calificacion <=100 :
    print(' su calificacion es de A')


comida=input(' que comida deseas comer ?')


if comida=='comida china' :
    print('te recomiendo pekin')
elif comida =='comida italiana' :
    print(' te recomiendo pizza en italys')
elif comida== 'comida tipica' :
    print(' te recomiendo don jediondo') 
else:
    print('busque en google')    



contraseña= int(input('ingresa tu contraseña'))
contraseñacorrecta=1098815533

if contraseña==contraseñacorrecta :
    print(' bienvenido a tu banco')
else:
    print(' contraseña incorrecta')



palabra= input('ingresa una palabra para verificar si es palindroma')

if str(palabra) == str(palabra)[::-1]:
    print(' la pabra es palindroma')
else:
    print( ' la palabra no es palindroma')    
