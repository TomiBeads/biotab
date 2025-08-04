#from pyairtable import Api

#api = Api("patf0NZCu1R0XOVDs.ac01eb0dc160ee42dacdafd5e70b6a06bab44fed6b3c7171befe7e80f4d29e39")
#tabla = api.table("appNDA3zjKznZwEsr", "usuario")

#registros = tabla.all()
#for r in registros:
    #print(r["fields"])

from pyairtable.orm import Model
from pyairtable.orm import fields

class Usuario (Model):
    clave = fields.TextField("clave")
    contra = fields.TextField("contra")
    nombre = fields.TextField("nombre")
    admin = fields.CheckboxField("admin")
    class Meta:
        api_key = "patf0NZCu1R0XOVDs.ac01eb0dc160ee42dacdafd5e70b6a06bab44fed6b3c7171befe7e80f4d29e39"
        base_id = "appNDA3zjKznZwEsr"
        table_name = "Usuario"

class bioenergia(Model):
    cultivo = fields.TextField("cultivo")
    parte = fields.TextField("parte")
    municipio = fields.SelectField("municipio")
    cantidad = fields.FloatField("cantidad")
    area = fields.FloatField("area")
    energia = fields.FloatField("energia")
    latitud = fields.FloatField("latitud")
    longitud = fields.FloatField("longitud")
    class Meta:
        api_key = "patf0NZCu1R0XOVDs.ac01eb0dc160ee42dacdafd5e70b6a06bab44fed6b3c7171befe7e80f4d29e39"
        base_id = "appNDA3zjKznZwEsr"
        table_name = "bioenergia"

#cacao = bioenergia(
    #cultivo = "Cacao",
    #parte = "Cascara",
    #municipio = "Cunduacan",
    #cantidad = 40.3,
    #area = 20.4,
    #energia = 18.2,
    #latitud = 18.076169,
    #longitud = 10.076169
#)

#cacao.save()
#nuevo = Usuario(
    #clave = "222H16010",
    #contra = "Magaña",
    #nombre = "Señor Magaña",
    #admin = 0
#)
#nuevo.save()