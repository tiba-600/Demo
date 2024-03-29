from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        voornaam = request.form['voornaam']
        achternaam = request.form['achternaam']
        email = request.form['email']
        password = request.form['password']
        print(f'email: {email}, Wachtwoord: {password}, voornaam: {voornaam}, achternaam: {achternaam}')
        return render_template('confirmation.html') 

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
