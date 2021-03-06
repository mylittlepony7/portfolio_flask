from flask import Flask,flash,render_template,request,redirect,url_for

app= Flask(__name__                                                                                     , template_folder='Templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config

@app.route('/favicon.ico')
def favicon():
    return "Yes"

@app.route('/')
@app.route('/home')
def Home():
    return render_template('./Home.html')

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/projects')
def projedcts():
    return render_template('projects.html')

@app.route('/contactme')
def contactme():
    return render_template('./contactme.html')

@app.route('/mobilebrowser')
def mobilebrowser():
    return "<h1>Mobile Browsers are currently not supported</h1>"

@app.route('/Experience')
def experience():
    return render_template('experience.html')


if __name__ == "__main__":
   app.run(debug=True)