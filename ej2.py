class Empleado:
    cantidad_empleados = 0
    tasa_incremento = 1.03

    def __init__(self, nombre, apellido, email, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.sueldo = sueldo

    def get_full_name(self):
        return '{} {}'.format(self.nombre, self.apellido)

    def get_new_salary(self):
        self.sueldo = int(self.sueldo * self.tasa_incremento)


emp1 = Empleado('Jane', 'Willis', 'jwillis@test.com', 2500)
emp2 = Empleado('Jack', 'Ryan', 'jryan@test.com', 5500)

print(emp1.get_full_name())
print(emp2.get_full_name())
print(Empleado.get_full_name(emp1))

print(emp1.__dict__)

print(emp1.sueldo)
emp1.get_new_salary()
print(emp1.sueldo)
print(Empleado.tasa_incremento)
print(emp1.tasa_incremento)
print(emp2.tasa_incremento)

emp2.tasa_incremento = 2.1
print(emp2.__dict__)
print(Empleado.__dict__)

Empleado.tasa_incremento = 1.5
print(Empleado.tasa_incremento)
print(emp1.tasa_incremento)
print(emp2.tasa_incremento)
emp1.tasa_incremento = 1.5
print(emp1.__dict__)
emp2.foo = 3
print(emp2.__dict__)
