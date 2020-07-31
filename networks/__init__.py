# PROJECT/NETWORKS/__init__.py
from flask import Blueprint

networks_blueprint = Blueprint('networks', __name__,
                     template_folder='templates/networks')
from project.networks import views, models