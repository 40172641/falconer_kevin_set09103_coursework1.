from flask import Flask, render_template
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
  return render_template('error2.html'), 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
