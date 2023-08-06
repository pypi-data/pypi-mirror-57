# This is the class you derive to create a plugin
import logging

from airflow.plugins_manager import AirflowPlugin
from airflow.www.app import csrf

from shu.api import create_api, create_swagger
from shu.resources import dags

import flask

log = logging.getLogger(__name__)

blueprint = flask.Blueprint("test", __name__)


@csrf.exempt
@blueprint.route("/test", methods=["POST"])
def test():
    return "Hello world!"


def create_blueprints():
    api = create_api("/internal")
    api.add_namespace(dags)
    swagger = create_swagger()
    csrf.exempt(api.blueprint)
    csrf.exempt(swagger)
    return [api.blueprint, swagger, blueprint]


# Defining the plugin class
class Plugin(AirflowPlugin):
    name = "internal"
    operators = []
    sensors = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = create_blueprints()
    menu_links = []
    appbuilder_views = []
    appbuilder_menu_items = []
    global_operator_extra_links = []
