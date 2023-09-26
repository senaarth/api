import json

def includeme(config):
    def company_service(request):
        return CompanyService(request)
    
    config.add_request_method(company_service, property=True, reify=True)

class CompanyService(object):
    def __init__(self, request):
        self.request = request

    def get_all_companies(self, request):
        all_companies = request.company_repository.get_all()

        company_list = [
            {
                'id': company.id,
                'name': company.name
            }
            for company in all_companies
        ]

        return company_list