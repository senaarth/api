import json
import pyramid
import pyramid.httpexceptions
from pyramid.response import Response

from .. import models

def includeme(config):
    config.add_route("all companies", pattern="/companies")

@pyramid.view.view_config(
    route_name="all companies",
    renderer="json",
    request_method="GET",
)
def get_all_companies(request):
    all_companies = request.company_service.get_all_companies(request)
    response_data = json.dumps(all_companies)

    return Response(body=response_data, content_type='application/json', charset='UTF-8')
