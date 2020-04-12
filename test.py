from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/temperatures', methods=['POST'])
def temperature():
    zipcode = request.form['zip']

    # API request from weather api
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?zip=' + zipcode + ', us&appid=ae1912cf80b5cfd20b0cca40f6237aa9')

    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    return render_template('temperature.html', temp=temp_f)


# function for index.html
@app.route('/')
def index():
    return render_template('index.html')


# running on main method
if __name__ == '__main__':
    app.run(debug=True)
