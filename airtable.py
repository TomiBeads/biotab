from pyairtable.orm import Model
from pyairtable.orm import fields

class Usuario (Model):
    clave = fields.TextField("clave")
    contra = fields.TextField("contra")
    nombre = fields.TextField("nombre")
    admin = fields.CheckboxField("admin")
    class Meta:
        api_key = "patn1DWLGpKowibsv.39bdd2ccad950be7954beb56934cc11958fe8d38c9972501c9d53818cf43b8d0"
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
        api_key = "patn1DWLGpKowibsv.39bdd2ccad950be7954beb56934cc11958fe8d38c9972501c9d53818cf43b8d0"
        base_id = "appNDA3zjKznZwEsr"
        table_name = "bioenergia"