"""
Proyecto 1: QUIZ

Fácil=1-12
Intermedio=13-24
Díficil=25-36
Muy díficil=37-50
"""
import random

#Abriendo archivo del QUIZ
archivo=open("quiz.txt","r",encoding="utf8")
lista=archivo.readlines()
archivo.close()

#Generando arreglo
quiz=[]

#Importar archivo .txt
for i in lista:
        var=i.replace("\n","").split(';')
        var2={"pregunta":var[0],"respuestas":var[1],"resp_c":var[2]}
        quiz.append(var2)

#Cargando valores iniciales
n_pregunta=0
aciertos=0
num_pre=[]   #Arreglo para almacenar preguntas hechas y evitar que se repitan
nivel=0     #Variable para control de nivel de preguntas
a=0
b=0
while n_pregunta<10:
    #Comprobando nivel
    if nivel>7:
         a=37
         b=50
         
    elif nivel>5:
         a=25
         b=36
         
    elif nivel>3:
        a=13
        b=24
    else:
         a=0
         b=12
         x=random.randint(a,b)
         
    
    while x in num_pre:
        x=random.randint(a,b)
        
    num_pre.append(x)
    
    #Imprimiendo en patalla
    print(f"Pregunta {n_pregunta+1}:")
    print()
    print(quiz[x]['pregunta'])
    print()
    print(quiz[x]['respuestas'])
    print()
        
    resp=input("Ingrese su respuesta: ")

    if resp==quiz[x]['resp_c']:
        print("Respuesta correcta")
        print()
        aciertos+=1
        nivel+=1

    else:
        print("Respuesta incorrecta")
        print()
        if nivel==0:
            nivel=0
        else:
            nivel-=1
        

    n_pregunta+=1

print(f"Número de aciertos es: {aciertos}")

#return b,c
#nivel1,nivel2=fun()
