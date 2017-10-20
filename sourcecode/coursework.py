from flask import Flask, render_template, redirect, json, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html'), 200

@app.route('/albums/<album_name>/')
def root(album_name):
  jsonfile=open('album.json').read() #Reads JSON File
  album=json.loads(jsonfile) #Loads JSON File
  return render_template("album.html", albums=album)

@app.route('/info/')
def info():
  return render_template('info.html'), 200

@app.route('/albums/')
def album():
  return render_template('albums.html'), 200

@app.route("/contact/", methods=['POST', 'GET'])
def contact():
  if request.method == 'POST':
    print request.form
    names= request.form['name']
    email= request.form['email']
    message= request.form['message']
    text_file = open("static/contact_us_messages/%s.txt" %names, "w")
    text_file.write("Name: " + names + "\nEmail:  " + email + "\nMessage: " + message)
    text_file.close()
    return render_template('response.html', name=names), 200
  else:
    return render_template('contact.html'),200

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html'), 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
