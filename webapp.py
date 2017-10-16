from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
@app.route("/h1")
def render_home1():
    return render_template('home1.html')
@app.route("/h2")
def render_home2():
    return render_template('home2.html')
@app.route("/h3")
def render_home3():
    return render_template('home3.html')



@app.route("/p1")
def render_response1():
    color = float(request.args['integer1'])
    #stores information sent to the server
    #args is a dactionary able to carry multiple values
    #args is visible in the url of the website
    reply = str(color * 0.9144)
    return render_template('page1.html', response = reply)
@app.route("/p2")
def render_response2():
    color = float(request.args['integer2'])
    reply = str(color * 2.54)
    return render_template('page2.html', response = reply)
@app.route("/p3")
def render_response3():
    color = float(request.args['integer3'])
    reply = str(color * 1.6)
    return render_template('page3.html', response = reply)

if __name__=="__main__":
    app.run(debug=False, port=54321)
