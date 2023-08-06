from doreah.control import mainfunction
from .database import db, load_endpoints
from collections import Counter

@mainfunction({})
def report(endpoint):
	load_endpoints()
	try:
		cls = db._getclassbyname(endpoint)
	except:
		raise
		print("Endpoint not found")
		return

	reports = db.getall(cls)
	for var in cls.__annotations__:
		val_list = [r.__getattribute__(var) for r in reports]
		print(var,Counter(val_list))
