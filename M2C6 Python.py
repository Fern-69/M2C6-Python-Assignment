class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        
cliente = Usuario('Juan', '1234')

print(cliente.__dict__)
