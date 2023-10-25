from flask import Flask,render_template,request,redirect,url_for,jsonify

# Creating a simple flask application...
app = Flask(__name__)

# Flask app routing
# Creating routes...
@app.route("/",methods=["GET"])
# The first parameter is default url, second is methods.

def welcome():
    return "<h1>Welcome to my webpage</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h2>Welcome to the index page</h2>"

# Variable Rule...
@app.route("/success/<int:score>")
def success(score):
    return f"The person has passed & the score is : {str(score)}"

@app.route("/failure/<int:score>")
def failure(score):
    return f"The person has failed & the score is : {str(score)}"

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        Maths=float(request.form["Maths"])
        Science=float(request.form["Science"])
        History=float(request.form["History"])

        avg_marks = (Maths+Science+History)/3
        res=""
        if(avg_marks>=50):
            res="success"
        else:
            res="failure"
        return redirect(url_for(res,score=avg_marks))
        # return render_template("form.html",score=avg_marks)

@app.route('/api',methods=["POST"])
def calc_sum():
    data = request.get_json()
    val_a = float(dict(data)['a'])
    val_b = float(dict(data)['b'])
    return jsonify(val_a+val_b)

if __name__ == "__main__":
    app.run(debug=True)

# If we do not specify "debug=true" then whenever we will do any change in our then always we have to stop the server of our flask app... It also takes 2 more params one is "URL" & the other is "Port". If there is no url given means that it will take a localhost & take port as 5000 by default.

