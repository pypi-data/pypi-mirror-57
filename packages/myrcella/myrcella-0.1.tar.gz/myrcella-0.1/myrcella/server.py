from bottle import Bottle, request
import waitress
from doreah import settings
from doreah.logging import log
from .database import db

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
		# instantiate a new object of this class
		cls(**data)
		db.save()
	except:
		log("Does not exist!")
		return 404



waitress.serve(server, host=HOST, port=PORT, threads=THREADS)
