from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    color = request.args['integer']
    #stores information sent to the server
    #args is a dactionary able to carry multiple values
    #args is visible in the url of the website
        reply = "integer * 0.9144"
    return render_template('page1.html', response = reply)

if __name__=="__main__":
    app.run(debug=False, port=54321)
