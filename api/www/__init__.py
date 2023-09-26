import re

import pyramid.interfaces
import pyramid.view


def includeme(config):
    config.add_route("root", pattern="/")
    config.add_route("error-500", pattern="/500")

@pyramid.view.view_config(
    route_name="root",
    renderer="json",
    request_method="GET",
)
def root(request):
    return { 'message': 'Hello World!' }
