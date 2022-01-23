from django.db import models
from datetime import datetime
from django.forms.models import model_to_dict

from core.erp.choices import gender_choices

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name
    
    def toJSON(self):
        item =model_to_dict(self, exclude=['id'])
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surname = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='DNI')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de Nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(decimal_places=2, default=0.00, max_digits=9)

    def __str__(self):
        return self.client.names
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    amount = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.product.name
    
    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']


# Ejemplo sobre modelos en Django
# class Type(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Nombre')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Tipo'
#         verbose_name_plural = 'Tipos'
#         ordering = ['id']


# class Employee(models.Model):
#     category = models.ManyToManyField(Category)
#     type = models.ForeignKey(Type, on_delete=models.CASCADE)
#     names = models.CharField(max_length=150, verbose_name='Nombres')
#     last_name = models.CharField(max_length=150, verbose_name='Apellidos')
#     dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
#     date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
#     date_creation = models.DateField(auto_now=True)
#     date_updated = models.DateField(auto_now_add=True)
#     age = models.PositiveIntegerField(default=0, verbose_name='Edad')
#     #gender = models.CharField(max_length=50, verbose_name='Sexo')
#     salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Salario')
#     state = models.BooleanField(default=True, verbose_name='Estado')
#     avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
#     cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

#     def __str__(self):
#         return self.names + ' ' + self.last_name

#     class Meta:
#         verbose_name = 'Empleado'
#         verbose_name_plural = 'Empleados'
#         db_table = 'empleado'
#         ordering = ['id']