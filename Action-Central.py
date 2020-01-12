from application import app, db
from application.models import User

@app.shell_context_processor
def make_shell_processor():
    return {'db': db, 'User': User}