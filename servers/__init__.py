# application/servers/__init__.py

from flask import Blueprint

servers = Blueprint('servers', __name__,
                           template_folder='templates')


from application.servers import routes, models
from application.networks import models
