class NombreClase:
    def __init__(self):
        print("Constructor")
        
    def metodoUno(self):
        print("Metodo Uno")

    def metodo(self, variable_uno:int, variable_dos:float)->int:
        """
        Este metodo recibe 2 variables enteras, las suma y regresa 
        el resultado de la suma

        Args:

        params

        variable_uno:int - Primer numero entero
        variable_dos:int - segundo numero entero

        :return

        suma:int - suma de los dos numeros enteros
        """
        suma = variable_uno + variable_dos
        return int(suma)
    
    def metodoTres(self, variable_tres:str)->None:
        print(f"numero de caracteres: (len(variable_tres))")


nombre_objeto=HolaMundo()
nombre_objeto.metodoUno()

