from .. import models

def includeme(config):
    def company_repository(request):
        return CompanyRepository(
            session=request.db_session,
        )
    
    config.add_request_method(company_repository, property=True, reify=True)

class CompanyRepository(object):

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(models.Company)
