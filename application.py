from flask import Flask , render_template, request
import pandas as pd
import pickle

model = pickle.load(open("/Users/prakhar/Desktop/FINAL-YEAR-PROJECT/predictor/randomforestmodel.pkl", 'rb'))

app=Flask(__name__)
crop = pd.read_excel("/Users/prakhar/Desktop/FINAL-YEAR-PROJECT/predictor/01.xlsx")



@app.route('/')
def index():
    state = sorted(crop['State_Name'].unique())
    district = sorted(crop['District_Name'].unique())

    return render_template('pred.html' , state = state , district = district)

@app.route('/predict',methods=['POST'])
def predict():
        state=request.form.get('state')
        district=request.form.get('district')
        Area=float(request.form.get('Area'))
        production=float(request.form.get('production'))
        prod_area=request.form.get('prod_area')
        Rainfall=float(request.form.get('Rainfall'))
        Temperature=float(request.form.get('Temperature'))
        PH=float(request.form.get('PH'))

    

        prediction = model.predict(pd.DataFrame([[state,district,Area,production,prod_area,Rainfall,Temperature,PH]], columns=['State_Name' , 'District_Name' , 'Area' , 'Production' , 'prod/area' , 'rainfall' , 'temp' , 'Ph']) )



        return prediction[0]

if __name__ =="__main__" :

           app.run(debug=True)