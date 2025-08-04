import peewee as pw 
from pyairtable.orm import Model
from pyairtable.orm import fields

#Base de datos local 
base_datos = pw.SqliteDatabase("base_datos.db")

class usuario(pw.Model):
    clave = pw.TextField(primary_key = True)
    contra = pw.TextField()
    nombre = pw.TextField()
    admin = pw.IntegerField()
    class Meta:
        database = base_datos

base_datos.connect()
base_datos.create_tables([usuario], safe=True)  # safe=True evita errores si ya existe la tabla
base_datos.close()

#usuarios = usuario.select()
#for u in usuario:
#    print(u.clave, u.contra, u.nombre, u.admin))
