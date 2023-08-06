from bottle import Bottle, request
import waitress
from doreah import settings
from doreah.logging import log
from .database import db, reverse_typenames

PORT = settings.get_settings("PORT")
HOST = settings.get_settings("HOST")
THREADS = 12


server = Bottle()

@server.post("/<endpoint>")
def post_endpoint(endpoint):

	data = request.json
	log("Received request to endpoint " + endpoint)
	try:
		cls = db._getclassbyname(endpoint)
		log("Mapped to class " + str(cls))
	except:
		log("Does not exist!")
		return 404
		
	# instantiate a new object of this class
	cls(**data)
	db.save()


@server.get("/<endpoint>")
def get_endpoint(endpoint):
	try:
		cls = db._getclassbyname(endpoint)
		# return information
		return {
			"types": {t:reverse_typenames[cls.__annotations__[t]] for t in cls.__annotations__},
			"defaults": {key:value for key, value in cls.__dict__.items() if not key.startswith('__') and not callable(value)}
		}
	except:
		return 404

waitress.serve(server, host=HOST, port=PORT, threads=THREADS)
