def evaluacion(a):
    switcher = {1: "empezar", 2: "salir",}
    selected = switcher.get(a, {"001": 'OPCIÓN INVÁLIDA'})
    if isinstance(selected, dict):
        print("{}, vuelva a seleccionar una opción".format(list(selected.values())[0]))
        main()
    elif selected == "salir":
        pass
    else:
        beign()

def beign():
    a = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    b = a.split(',')
    size = range(1, len(b))
    print("Ingrese un número")
    num_prueba = int(input())
    factor = 1
    resultado = ''
    if num_prueba > len(b):
        temp = num_prueba
        while(temp > len(b)):
            temp -= len(b)
            factor += 1
        pos_factor = factor-2
        resultado = b[pos_factor] + b[temp-1]
    elif num_prueba <= len(b):
        resultado = b[num_prueba-1]
    print("RESULTADO ============> La(s) letra(s) correspontiente(s) al resultado es/son: {}".format(resultado))
    main()
        

def main():
    print("Programa de transformación de números a letras, seleccione opción")
    print("1. Ingresar un número")
    print("2. salir")
    opcion = int(input())
    evaluacion(opcion)


main()
