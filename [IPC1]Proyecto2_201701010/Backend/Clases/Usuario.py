#Se cra la clase
class Usuario:
    #Nuevo constructor
    #__init__ será método que se ejecuta al crear un objeto
    #self hace referencia al objeto actual

    def __init__(self, nombre, apellido, nombre_usuario, contrasenia, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.tipo = tipo

    #Se crea el metodo toDict convierte los objetos de una clase en diccionarios
    def toDict(self):
        return {
            'nombre':self.nombre,
            'apellido':self.apellido,
            'nombre_usuario': self.nombre_usuario,
            'contrasenia': self.contrasenia,
            'tipo': self.tipo
        }
    