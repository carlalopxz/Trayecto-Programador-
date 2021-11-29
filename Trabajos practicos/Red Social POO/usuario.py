import base64

class Usuario():
    def __init__(self,nombre, apellido,email, password, sexo, imagenPerfil,
    imagenPortada,biografia,celular,fechaCreacionCuenta,ciudad,sentimental):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.set_password(password)
        self.__sexo = sexo
        self.__imagenPerfil = imagenPerfil
        self.__imagenPortada = imagenPortada
        self.__biografia = biografia
        self.__celular = celular
        self.__fechaCreacionCuenta = fechaCreacionCuenta
        self.__ciudad = ciudad
        self.__sentimental = sentimental
    
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password 
    def get_sexo(self):
        return self.__sexo
    def get_imagenPerfil(self):
        return self.__imagenPerfil
    def get_imagenPortada(self):
        return self.__imagenPortada
    def get_biografia(self):
        return self.__biografia
    def get_celular(self):
        return self.__celular
    def get_fechaCreacionCuenta(self):
        return self.__fechaCreacionCuenta
    def get_ciudad(self):
        return self.__ciudad
    def get_sentimental(self):
        return self.__sentimental
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_apellido(self,apellido):
        self.__apellido = apellido
    def set_email(self,email):
        self.__email = email
    def set_password(self,password):
        self.__password = self.__encriptarContrasenia(password)
    def set_sexo(self,sexo):
        self.__sexo = sexo
    def set_imagenPerfil(self,imagenPerfil):
        self.__imagenPerfil = imagenPerfil
    def set_imagenPortada(self,imagenPortada):
        self.__imagenPortada = imagenPortada
    def set_biografia(self,biografia):
        self.__biografia = biografia
    def set_celular(self,celular):
        self.__celular = celular
    def set_fechaCreacionCuenta(self,fechaNueva):
        self.__fechaCreacionCuenta = fechaNueva
    def set_ciudad(self,ciudad):
        self.__ciudad = ciudad
    def set_sentimental(self,sentimental):
        self.__sentimental = sentimental
    
    def __encriptarContrasenia(self,password):
        return base64.b64encode(password.encode("UTF-8")).decode("UTF-8")