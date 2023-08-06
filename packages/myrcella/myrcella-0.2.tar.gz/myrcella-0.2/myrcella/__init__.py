name = "myrcella"
version = 0,2
versionstr = ".".join(str(n) for n in version)
desc = "Simple API server to collect data according to dynamically loaded yaml specifications"
author = {
	"name": "Johannes Krattenmacher",
	"email": "python@krateng.dev",
	"github": "krateng"
}
requires = [
	"bottle>=0.12.16",
	"waitress>=1.3",
	"doreah>=1.3"
]
resources = [
	"data_files/*/*"
]







### DOREAH CONFIGURATION

from doreah import config
import pkg_resources

config(
	packageutils={
		"packagename": name,
		"populate": pkg_resources.resource_filename(__name__,"data_files")
	}
)
from doreah.packageutils import datafolder, init_datafolder
init_datafolder()
config(
	logging={
		"logfolder": datafolder("logs")
	},
	settings={
		"files":[
			datafolder("settings","default.ini"),
			datafolder("settings","settings.ini")
		]
	}
)
