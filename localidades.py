#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Ingresar en un diccionario localidades (clave) y dos datos: cantidad de personas en edad laboral – 
cantidad de empleados. Los datos surgen de distintas planillas, por lo que una misma clave (localidad) se 
puede ingresar varias veces, debiendo sumarse los valores. Se pide: 
a) Calcular el total de personas en edad laboral y empleados para cada localidad e imprimirlo.
b) Imprimir un listado ordenado de mayor a menor por porcentaje de desocupación. Indicando: localidad - 
% de desocupación
'''
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def cargar_localidades(clave):
    localidad = {}
    r = clave
    while r != 'No':
        p = int(input('personas en edad laboral: '))
        e  =int(input('empleados: '))    
        if not r in localidad :
            localidad[r] = r
            localidad[r] = [p,e]
        else :
            localidad[r][0]+= p
            localidad[r][1]+= e
        r = input('localidad: ')   
    return localidad

def ordenar_tabla(l):
    dic = sorted(l,key=lambda item: item[0],reverse=True)
    return dic

def imprimir_empleados_en_edad_laboral():
    clave = input('agregar localidad: ')
    localidad = cargar_localidades(clave)
    total_edad_laboral=0
    total_empleados = 0
    print(localidad)
    for lo in localidad:
        total_edad_laboral+=localidad[lo][0]
        total_empleados+=localidad[lo][1]
        print('total de personas en edad laboral :',localidad[lo][0],'y empleados:',localidad[lo][1],'ubicados en ',lo)
    ordenado = ordenar_tabla(localidad)
    for l in ordenado:
        porc_desocupacion = (localidad[l][0]/total_edad_laboral)*100
        print('localidad - ',l,'su porcentaje de desocupacion es: ',porc_desocupacion)

#----------------------------------------------Bloque Principal---------------------------------------------
imprimir_empleados_en_edad_laboral()

    

    
        

        
    



            
            
                




    

