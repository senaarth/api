def includeme(config):
    config.add_tween(".db.db_tween_factory")

def db_tween_factory(handler, registry):
    def finish_db_session(request):

        response = handler(request)

        if getattr(request, "_db_session", None):
            request._db_session.close()

        return response
    return finish_db_session
