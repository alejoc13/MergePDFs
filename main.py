import helper.options as op


if __name__ == '__main__':
    option  = input("""
                    Ingrese el número de la opción a utilizar:
                    1. Automatica - EL orden de lso PDF será el orden ene el qeu se enceuntren en la carpeta Documents
                    2. Manual - Ingrese manualmente lso docuemntos en el orden que desea que se agrupen
                    Presione enter sin ingresar ninguan opción pada terminar la ejecución
                    Ingrese la opción: """)

    if option == '1':
        op.automaticOption()
    elif option == '2':
        op.manualOption()
