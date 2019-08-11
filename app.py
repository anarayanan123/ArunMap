from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_static(name=None):
    return render_template('ArunMap.html', name=name)

if __name__ == '__main__':
    app.run()
