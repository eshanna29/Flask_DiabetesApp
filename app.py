from flask import Flask, render_template, request
import joblib
#initialize app
app=Flask(__name__)

#load the model
model=joblib.load('diabetes_78.pkl')

@app.route('/')
def hello():
    return render_template('form.html')


@app.route('/submit',methods=['POST'])
def form_data():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    
    output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if output[0]==1:
        out='diabetic'
    else:
        out='not diabetic'

    return render_template('predict.html', data=f'person is {out}')

if __name__ == '__main__':
    app.run(debug=True)
