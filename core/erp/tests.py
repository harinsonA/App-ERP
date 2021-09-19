from django.test import TestCase

# Create your tests here.
'''
# listar
query = Type.objects.all()
print(query)

# Insertar
t = Type()
t.name = 'Accionista
t.save()


# Editar 
t = Type.objects.get(pk=1)
t.name = 'Presidente
t.save()

# Eliminar
t = Type.objects.get(pk=1)
t.delete()

# Filtrar
obj = Type.objects.filter(
    name__icontains='terry'
)

obj = Type.objects.filter(name__endswith='a').exclude(id=5)
for i in Type.objects.filter(name__endswith='a')[:2]:
    print(i.name)

# Filtrar por llave foranea
Empleado.objects.filter(type_id=1)
Empleado.objects.filter(type_id=1, date__)

'''