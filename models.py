"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# DO NOT MODIFY THIS FUNCTION  


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"
   
    # ADD THE NECESSARY CODE HERE
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).all()



    def __repr__(self):
        p = self
        return f"<Playlist id={p.id} name={p.name} description={p.description}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(30), nullable=True)

    def greet(self):
        return f"Artist name {self.name} Story {self.description}"

# class Song(db.Model):
#     """Song."""

#     # ADD THE NECESSARY CODE HERE


# class PlaylistSong(db.Model):
#     """Mapping of a playlist to a song."""

#     # ADD THE NECESSARY CODE HERE
