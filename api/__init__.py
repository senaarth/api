from pyramid.config import Configurator
import sqlalchemy
from sqlalchemy.orm import sessionmaker

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        _register_endpoints(config)
        _inject_db_session(config)
        _inject_repositories(config)
        _inject_services(config)

        config.include('.www')
        config.scan()

    return config.make_wsgi_app()

def _inject_db_session(config):
    config.include(".www.db")

    settings = config.get_settings()
    engine = sqlalchemy.create_engine(settings["postgres.uri"])
    _session_factory = sessionmaker(bind=engine)

    # Lazily create a db session and re-use it throughout the request
    def db_session(request):
        if not getattr(request, "_db_session", None):
            request._db_session = request.session_factory()

        return request._db_session

    def session_factory(request):
        return _session_factory

    config.add_request_method(db_session, property=True, reify=True)
    config.add_request_method(session_factory, property=True, reify=True)

def _register_endpoints(config):
    config.include(".www.company")

def _inject_repositories(config):
    config.include(".repositories.company")

def _inject_services(config):
    config.include(".services.company_service")