from flask_script import Manager,commands
from flask_migrate import Migrate, MigrateCommand
from todoapp import app
from models import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def init_db():
    with app.test_request_context():
        from models import db
        db.engine.echo = True
        db.metadata.bind = db.engine
        db.metadata.create_all(checkfirst=True)
        #db.create_all(checkfirst=True)

if __name__ == "__main__":
    manager.run()
