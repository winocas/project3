# from flask import Flask, url_for, redirect

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return redirect(url_for('main'))

# @app.route('/service')
# def main():
#     return '서비스'

# if __name__=='__main__':
#     app.run(debug=True)

from flask import Flask, render_template, redirect, request, url_for
import corona_data

app = Flask(__name__)
 
@app.route('/')
def index():
    data1 = corona_data.get_tot_coro()
    data2 = corona_data.get_city_coro()
    return render_template('index.html', data1=data1, data2=data2)

@app.route('/city')
def region():
    data = corona_data.get_city_coro()
    return render_template('region.html', data=data)

@app.route('/coro/')
@app.route('/coro/<city>')
def inputTest(city=None):
    data = corona_data.get_city_coro()  
    return render_template('main.html', city=city, data=data)
    
@app.route('/cityinfo',methods=['POST'])
def calculate(city=None):
    data = corona_data.get_city_coro()
    if request.method == 'POST':
        temp = request.form['city']
    else:
        temp = None
    return redirect(url_for('inputTest',city=temp))
 
if __name__ == '__main__':
    app.run()