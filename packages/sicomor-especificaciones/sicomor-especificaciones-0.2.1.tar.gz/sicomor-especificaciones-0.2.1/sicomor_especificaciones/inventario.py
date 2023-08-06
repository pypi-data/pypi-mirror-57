from .hardware_inv import HARDWARE_INV
from .sistop_inv   import SISTOP_INV
from .software_inv import SOFTWARE_INV

INVENTARIO = HARDWARE_INV + SISTOP_INV + SOFTWARE_INV


def get_by_tipo():
	"""
		   tipo1    tipo2
		{
			"SW": { "SW": { "identificador": 11020001,
							  "descripcion": "Paquete Office Instalado", } ,
		}
	"""
	especificaciones = {}
	for recurso in INVENTARIO:
		if recurso["estado"]:
			tipo1_name = recurso["tipo1"]
			if tipo1_name not in especificaciones.keys():
				especificaciones[tipo1_name] = {}

			tipo2_keys = especificaciones[tipo1_name].keys()
			
			tipo2_name = recurso["tipo2"]
			if recurso["tipo2"] not in tipo2_keys:
				especificaciones[tipo1_name][tipo2_name] = {}

			especificaciones[tipo1_name][tipo2_name] = {
				"identificador": recurso["identificador"],
				"descripcion": recurso["descripcion"]
			}
	return especificaciones


def get_recursos():
	"""
		Retorna lista de inventarios validos.
	"""
	recursos = []
	for x in INVENTARIO:
		if x["estado"]:
			recursos.append(x)
	return recursos


def get_recurso(identificador):
	for x in INVENTARIO:
		if x["identificador"] == int(identificador):
			return x
	return {}
