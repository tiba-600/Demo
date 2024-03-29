from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Hier kun je de logica toevoegen om de gegevens van het formulier te verwerken,
        # bijvoorbeeld het verzamelen van inloggegevens en het opslaan in een database.
        # In dit voorbeeld zullen we eenvoudigweg de ingediende gegevens afdrukken.
        username = request.form['username']
        password = request.form['password']
        print(f'Gebruikersnaam: {username}, Wachtwoord: {password}')
        return 'Bedankt voor het indienen van uw gegevens.'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)