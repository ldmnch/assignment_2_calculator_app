from flask import Flask, render_template, request
from helpers import calculator_helper, check_input_type
from geometry import Circle

app = Flask(__name__)  # create the instance of the flask class

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])  # associating the POST method with this route

def calculate():

    result = None

    category = request.form.get('category') 
    print(f"Category received: {category}")  # Debug: Print the category value


    if category == 'algebra':

        # using the request method from flask to request the values that were sent to the server through the POST method
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = str(request.form['algebra_operation'])

        try:
            value1, value2 = check_input_type(value1, value2)
        except ValueError:
            return render_template('index.html', printed_result="Invalid input, Please insert numeric values.")

        result = calculator_helper(value1, value2, operation)

    elif category == 'geometry':

        radius = request.form['radius']
        operation = str(request.form['geometry_operation'])
        print(operation)

        try:
            radius = float(radius)
        except ValueError:  
            return render_template('index.html', printed_result="Invalid input, Please insert numeric values.")
        
        circle_instance = Circle(radius)

        if operation == 'area':
            result = circle_instance.area()
        elif operation == 'circumference':
            result = circle_instance.perimeter()

    return render_template('index.html', printed_result=result)

if __name__ == "__main__":
    app.run(debug=True)