from flask import Flask, render_template, request

app = Flask(__name__)

#list arrays
generalP = []
tvP = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/general', methods=["POST", "GET"])
def general():
    if request.method == "POST":
        content = request.json
        generalP.append(content)

    return render_template('general.html', posts = generalP)
    

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/tv', methods=["POST", "GET"])
def tv():
    if request.method == "POST":
        content = request.json
        tvP.append(content)
    return render_template('tv.html', posts = tvP)

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
