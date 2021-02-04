from flask import Flask, flash, request, redirect, render_template
# from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import PlaylistForm, SongForm, NewSongForPlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    return render_template("home.html")


##############################################################################
# Playlist routes

@app.route("/playlists")
def list_playlists():
    """Shows Lists of all playlists" in db"""
    multipleplaylists = Playlist.query.all()
    return render_template('playlists.html', playlists=multipleplaylists)


@app.route('/playlists/<int:playlist_id>')
def show_playlist(playlist_id):
    """ Show details about artist """
    foundplaylist = Playlist.query.get(playlist_id)
    print(foundplaylist)
    return render_template("playlist.html", playlist=foundplaylist)
    # print(Playlist.description)


# @app.route("/playlists/add", methods=["GET", "POST"])
@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    print(request.form)
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        flash(
            f"Created new playlist: name is {name}, description is {description}")
        ps = Playlist(name=name, description=description)

        db.session.add(ps)
        # ps = Playlist(name=name, description=description)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_playlist.html', form=form)
    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@ app.route('/')
# ##############################################################################
# # Song routes
@ app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""
    song = Song.query.filter_by(id=song_id).first()
    playlistsongin = PlaylistSong.query.filter_by(song_id=song_id).all()

    # # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    # print(foundsonglist)
    # return f"<h1>{song.title}</h1>"
    # return render_template("songs.html", songs=foundsonglist)
    return render_template('song.html', song=song, playlistsongin=playlistsongin)
# ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    print(request.form)
    #    """Handle add-song form:

    #    - if form not filled out or invalid: show form
    #    - if valid: add playlist to SQLA and redirect to list-of-songs
    #    """
# ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    form = SongForm()
    if form.validate_on_submit():
        song = Song(title=form.title.data, artist=form.artist.data)
        # flash(
        #     f"Artist new song: artist is {artist}, story is {story}")
        # sg = Song(artist=artist, story=story)

        db.session.add(song)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_song.html', form=form)


# @app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
# def add_song_to_playlist(playlist_id):
"""Add a playlist and redirect to list."""

#     # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

#     # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

# playlist = Playlist.query.get_or_404(playlist_id)
# form = NewSongForPlaylistForm()

#     # Restrict form to songs not already on this playlist

#     curr_on_playlist = ...
#     form.song.choices = ...

# curr_on_playlist = [s.id for s in playlist.songs]
# form.song.choices = (db.session.query(Song.id, Song.title)
#                      .filter(Song.id.notin_(curr_on_playlist))
#                      .all())


#     if form.validate_on_submit():

# if form.validate_on_submit():

#     # This is one way you could do this ...
#     playlist_song = PlaylistSong(song_id=form.song.data,
#                                  playlist_id=playlist_id)
#     db.session.add(playlist_song)


#         # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

#         return redirect(f"/playlists/{playlist_id}")

#     return render_template("add_song_to_playlist.html",
#                            playlist=playlist,
#                            form=form)

# db.session.commit()

# return redirect(f"/playlists/{playlist_id}")

# return render_template("add_song_to_playlist.html",
#                        playlist=playlist,
#                        form=form)
