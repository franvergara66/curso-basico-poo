class Estudiante:

    def __init__(self, id, nombre, apellido, email, edad, universidad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.universidad = universidad

    def get_full_name(self):
        return '{} {}'.format(self.nombre, self.apellido)


estudiante1 = Estudiante(17389551, 'Francisco', 'Vergara', 'javiervergara2004@gmail.com', 33, 'UCV')
estudiante2 = Estudiante(13493706, 'Andrea', 'Garcia', 'agarcia@gmail.com', 29, 'UCAB')

print(estudiante1.get_full_name())
print(estudiante2.get_full_name())
print(Estudiante.get_full_name(estudiante2))
