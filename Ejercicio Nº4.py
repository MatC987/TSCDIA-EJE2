def igualdad_numerica(a,b):
    if a == b:
        return print('Los numeros ingresados son iguales. Resultado:', a==b)
    else:
        return print('Los numeros ingresados no son iguales. Resultado:', a==b)

num1 = float(input('ingrese el primer numero'))
num2 = float(input('ingrese el segundo numero'))

igualdad_numerica(num1,num2)