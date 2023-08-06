from doreah import database
from doreah.packageutils import datafolder
from doreah.regular import hourly
import yaml

import os


db = database.Database(file=datafolder("database.ddb"))

typenames = {
	"str":str,
	"int":int,
	"bool":bool,
	"float":float
}
reverse_typenames = {typenames[t]:t for t in typenames}

#class Endpoint(db.DBObject):
#	__primary__ = "name",
#	name: str
#	data: dict = {}


@hourly
def load_endpoints():
	for fi in os.listdir(datafolder("endpoints")):
		try:
			with open(datafolder("endpoints",fi),"r") as f:
				info = yaml.safe_load(f)
				# create new endpoint or update existing
				#ep = Endpoint(name=data["name"],data=data["data"]) #data

				types = {}
				defaults = {}
				for var in info["data"]:

					val = info["data"][var]
					if type(val) in [dict,list]: continue
					if val in typenames:
						types[var] = typenames[val]
					else:
						types[var] = type(val)
						defaults[var] = val


				# this dynamically creates a subclass of DBObject with the default values and the types as annotations
				type(info["name"],(db.DBObject,),{**defaults,"__annotations__":types})

		except:
			print("Could not load endpoint information from",fi)

	db.save()
