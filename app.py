from flask import Flask, render_template, jsonify
from flask import send_from_directory
app = Flask(__name__, static_folder='static')
app = Flask(__name__)

# Replace this with your actual data retrieval logic
aspirants_data = [
    {"name": "Sai Abhivardhan Arcot", "imageUrl": "images/kungfu.png"},
    {"name": "Kandhakatla Sai Krishna", "imageUrl": "images/au1.jpg"},
    {"name": "Rohith Vengala", "imageUrl": "images/au2.jpg"},
    {"name": "Sai Abhivardhan Arcot", "imageUrl": "images/kungfu.png"},
    {"name": "Kandhakatla Sai Krishna", "imageUrl": "images/au1.jpg"},
    {"name": "Rohith Vengala", "imageUrl": "images/au2.jpg"}
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/aspirants')
def get_aspirants():
    return jsonify(aspirants_data)

if __name__ == '__main__':
    app.run(debug=True)
