from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     

# 1) http://localhost:5000 - should display 8 by 8 checkerboard    
@app.route('/')                           
def index():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', row = 8, column = 8, color_one = "red", color_two = "black" )  

# 2) http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/4')                           
def eight_four():
    return render_template('index.html', row = 4, column = 8, color_one = "red", color_two = "black")  

# 3) http://localhost:5000/(x)/(y)
@app.route('/<int:x>/<int:y>')                           
def x_y(x,y):
    return render_template('index.html', row = x, column = y, color_one = "red", color_two = "black")  

#4) ninja bonus "/<x>/<y>/<color1>/<color2>") 
@app.route('/<int:x>/<int:y>/<string:color_one>/<string:color_two>')                           
def x_z(x,y, color_one, color_two):
    return render_template('index.html', row = x, column = y, color_one = color_one, color_two = color_two)


if __name__=="__main__":
    app.run(debug=True)                   



