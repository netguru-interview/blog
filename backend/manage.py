from flask.cli import FlaskGroup
from flaskblog import create_app, db
from flaskblog.models import User

app = create_app()

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    sample_user = User(
        username='admin',
        email='ponomarov.aleksandr@gmail.com',
        password='$2b$12$xwnQU6n3vKIjOzm2pnpKl.VgheEnU5aGwmaVSZRIbAIQCQxoA2pzS')
    db.session.add(sample_user)
    db.session.commit()


if __name__ == "__main__":
    cli()
