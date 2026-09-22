from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

EXPRESS_API_URL = os.environ.get('EXPRESS_API_URL', 'http://express-app:5000')

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        try:
            response = requests.post(
            f'{EXPRESS_API_URL}/api/users', 
                json={'name': name, 'email': email},
            timeout=5
            )
            if response.status_code == 201:
                message = "User created successfully!"
            else:
                message = "Failed to create user."

        except requests.RequestException as e:
            print(f"Error creating user: {e}")
            message = "Error creating user. Please try again later."


    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)