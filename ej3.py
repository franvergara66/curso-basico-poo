import datetime


class Empleado:
    cantidad_empleados = 0
    tasa_incremento = 1.03

    def __init__(self, nombre, apellido, email, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.sueldo = sueldo
        Empleado.cantidad_empleados += 1

    def get_full_name(self):
        return '{} {}'.format(self.nombre, self.apellido)

    def get_new_salary(self):
        self.sueldo = int(self.sueldo * self.tasa_incremento)

    @classmethod
    def asignar_incremento(cls, cantidad):
        cls.tasa_incremento = cantidad

    @classmethod
    def convertir_desde_string(cls, empString):
        nombre, apellido, email, sueldo = empString.split("-")
        return cls(nombre, apellido, email, sueldo)

    @staticmethod
    def es_laborable(day):
        if day.weekday() in (5, 6):
            return False
        return True


emp1 = Empleado('Jane', 'Willis', 'jwillis@test.com', 2500)
emp2 = Empleado('Jack', 'Ryan', 'jryan@test.com', 5500)

Empleado.asignar_incremento(1.2)

print(emp1.tasa_incremento)
print(emp2.tasa_incremento)
print(Empleado.tasa_incremento)

nuevo_empleado = Empleado.convertir_desde_string("Luis-Campos-lcampos@test.com-10000")
print(nuevo_empleado.__dict__)

dia = datetime.date(2019, 12, 18)
print(Empleado.es_laborable(dia))
