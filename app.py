from flask import Flask, render_template
app = Flask(__name__)
#Strona Główna
@app.route('/')
def home():
#Ta funkcja zwraca plik index.html kiedy ktoś wchodzi na stronę główną
    return render_template('index.html')
#Strona logowania
@app.route('/login')
def login():
    return render_template('Logowanie.html')  
#Strona z ciekawostką
@app.route('/page1')
def page1():
     return render_template('index2.html')
#Strona z animacją
@app.route('/adnotacja')
def adnotacja():
    return render_template('index3.html')
if __name__ == '__main__':
    app.run(debug=True)    