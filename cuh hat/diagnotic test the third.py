from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    biodata = {
        'name': 'massimo matthew marelius',
        'class': '69 ips 420',
    }
    return render_template('home.html', biodata=biodata)

@app.route('/igs')
def igs():
    data1 = ["I", "G", "S"]
    return render_template('igs.html', data1=data1)

if __name__ == '__main__':
    app.run(debug=True)