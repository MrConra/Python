from flask import Flask, render_template, request, redirect, url_for # type: ignore

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta de ejemplo
@app.route('/about')
def about():
    return "Página sobre nosotros"

if __name__ == '__main__':
    app.run(debug=True)
