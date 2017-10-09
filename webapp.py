from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    color = request.args['color']
    #stores information sent to the server
    #args is a dactionary able to carry multiple values
    #args is visible in the url of the website
    if color == 'pink'
        reply = "You must be a girl!!"
    else:
        reply = "you are a chump"
    return render_template('responde.html', response = reply)

if __name__=="__main__":
    app.run(debug=False, port=54321)
