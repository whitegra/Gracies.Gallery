from flask import Flask, render_template, abort
from artworks_data import ARTWORKS  # Import the ARTWORKS dictionary

app = Flask(__name__)

@app.route('/')
def index():
    """Home page that lists all artworks."""
    return render_template('index.html', artworks=ARTWORKS)

@app.route('/artwork/<artwork_id>')
def artwork(artwork_id):
    """Detail page for a single artwork."""
    if artwork_id not in ARTWORKS:
        abort(404)  # Return 404 if artwork_id is invalid
    artwork = ARTWORKS[artwork_id]
    return render_template('artwork.html', artwork=artwork)

if __name__ == '__main__':
    app.run()
