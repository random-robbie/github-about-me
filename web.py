from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        token = request.form['token']
        headers = {'Authorization': f'token {token}'}
        response = requests.get('https://api.github.com/user', headers=headers)
        if response.status_code == 200:
            user = response.json()
            return render_template('user.html', user=user)
        else:
            error = f'Error: {response.status_code} {response.reason}'
            return render_template('index.html', error=error)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
