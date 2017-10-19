from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html'), 200

@app.route('/info/')
def info():
  return render_template('info.html'), 200

@app.route('/albums/')
def album():
  return render_template('album.html'), 200

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html'), 404

@app.route('/albums/pablohoney/')
def pablo():
  return render_template('pablo_honey.html'), 200

#@app.route('/albums/inrainbows/')
#def pablo(name=None):
 # song_name = 'Pablo Honey'
  #return render_template('song.html', song_name=song_name)

#...
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
