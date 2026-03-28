from flask import Flask, render_template, request, redirect , url_for
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 🔹 Get data from form
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # 🔹 Check password match
        if password != confirm_password:
            return render_template('register.html', msg="Passwords do not match!")
        return redirect(url_for('login'))


    # 🔹 Render registration form on GET request
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('home'))
        
        
    return render_template('login.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    msg =''
    output = ""    
    if request.method == 'POST':
        gender = int(request.form['gender'])
        age = int(request.form['age'])
        hypertension = int(request.form['hypertension'])
        heart_disease = int(request.form['heart_disease'])
        smoking_history = int(request.form['smoking'])
        bmi = float(request.form['bmi'])
        HbA1c_level = float(request.form['HbA1c_level'])
        blood_glucose_level = int(request.form['blood_glucose_level'])
        test_data = [gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level]
        print("Test data",test_data)
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn import tree
        from sklearn.metrics import accuracy_score

        df=pd.read_csv("static/diabetes_prediction_dataset.csv")

        df.head()

        df.tail()

        df.describe()

        df.info()



        df = pd.read_csv("static/diabetes_prediction_dataset.csv")

        df['gender'] = df['gender'].replace(['Female', 'Male', 'Other'], [0, 1, 2])
        df['smoking_history'] = df['smoking_history'].replace(
            ['never', 'No Info', 'current', 'former', 'ever', 'not current'],
            [0, 1, 2, 3, 4, 5]
        )

        x = df.drop('diabetes', axis=1)
        y = df['diabetes']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        model = LogisticRegression(random_state=0, max_iter=1000)  # 🔥 FIX: convergence error avoid

        model.fit(x_train, y_train)

        predicted_output = model.predict(x_test)
        print(predicted_output)
        print(y_test)

        accuracy = accuracy_score(y_test, predicted_output)
        print("Accuracy:", accuracy)

        
        Predictions = model.predict([test_data])
        print(Predictions)

        if Predictions[0] == 0:
            print("No diabetes Disease")
            output = "No diabetes Disease"
        else:
            print("Diabetes Disease")
            output = "Diabetes Disease"
        
    return render_template('Diabetes.html',output=output,Title ="Diabetes.html") 


@app.route('/prediction', methods=['GET','POST'])

def prediction():
    msg=''
    output=""
    if request.method=='POST':
        age=int(request.form['age'])
        sex=int(request.form['sex'])
        cp=int(request.form['cp'])
        trestbps=int(request.form['trestbps'])
        chol=int(request.form['chol'])
        fbs=int(request.form['fbs'])
        restecg=int(request.form['restecg'])
        thalach=int(request.form['thalach'])
        exang=int(request.form['exang'])
        oldpeak=float(request.form['oldpeak'])
        slope=int(request.form['slope'])
        ca=int(request.form['ca'])
        thal=int(request.form['thal'])

        test_data=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        print("Testdata",test_data)
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn import tree

        from sklearn.metrics import accuracy_score

        data = pd.read_csv("static/heart.csv")
        data.head()

        data.tail()

        data.describe()

        data.info()

        X= data.drop('target', axis=1)
        Y= data['target']

        X.shape

        Y.shape

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        X_train.shape
        
        X_test.shape

        #model = KNeighborsClassifier(n_neighbors=5)
        model = LogisticRegression(random_state=0)
        #model = tree.DecisionTreeClassifier()

        X_test.shape

        model.fit(X_train, Y_train)

        predicted_output = model.predict(X_test)
        print(predicted_output)
        print(Y_test)



        accuracy = accuracy_score(Y_test, predicted_output)
        accuracy

        #X_test=[54,1,0,122,286,0,0,116,1,3.2,1,2,2]
        Predictions = model.predict([test_data])
        print(Predictions)

        #age=int(input("Enter Age: "))
        #sex=int(input("Enter Gender: "))
        #cp=int(input("Enter Chest Pain: "))
        #trestbps=int(input("Enter Blood Pressure: "))
        #chol=int(input("Enter Cholestrol: "))
        #fbs=int(input("Fasting Blood Sugar: "))
        #restecg=int(input("Enter Restecg: "))
        #thalach=int(input("Enter Thalach: "))
        #Exang=int(input("Enter Exang: "))
        #Oldpeak=float(input("Enter Oldpeak: "))
        #slope=int(input("Enter Slope: "))
        #ca=int(input("Enter Ca: "))
        #Thal=int(input("Enter Thal: "))

        #list=[age, sex, cp, trestbps, chol, fbs, restecg, thalach, Exang, Oldpeak, slope, ca, Thal]
        #print(list)
        

        if(Predictions[0]==0):
            print("No Heart Disease")
            output="No Heart Disease"
        else:
            print("Heart Disease")
            output="Heart Disease"
    return render_template('heart.html',output=output ,Title="heart.html")


#lungs disease

@app.route('/lungs', methods=['GET','POST'])

def lungs():
    msg=''
    output=""
    if request.method=='POST':
        age = int(request.form['age'])
        smoking = int(request.form['smoking'])
        alcohol = int(request.form['alcohol'])
        airpollution = int(request.form['airpollution'])
        geneticrisk = int(request.form['geneticrisk'])
        chestpain = int(request.form['chestpain'])
        coughing = int(request.form['coughing'])
        fatigue = int(request.form['fatigue'])
        shortnessbreath = int(request.form['shortnessbreath'])
        
        

        test_data=[age,smoking, alcohol, airpollution, geneticrisk,chestpain,coughing,fatigue,shortnessbreath]
        print("Testdata",test_data)
        
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn import tree

        from sklearn.metrics import accuracy_score

        data = pd.read_csv("static/lungs.csv")

        data.head()

        data.tail()

        data.describe()

        data.info()

        data['LungCancer'] = data['LungCancer'].map({'YES':1, 'NO':0})

        data.info()

        x= data.drop('LungCancer', axis=1)
        y= data['LungCancer']

        x.shape
        y.shape

        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

        x_train.shape

        x_test.shape

        model = LogisticRegression()
        x_test.shape
        model.fit(x_train, y_train)

    

        predicted_output = model.predict(x_test)
        print(predicted_output)
        print(y_test)

        accuracy = accuracy_score(y_test, predicted_output)
        print(accuracy)

        Predictions= model.predict([test_data])

        print(Predictions)

        if(Predictions[0]==0):
            print("No Lungs Disease")
            output = "No lungs disease"

        else:
            print("lungs Disease")
            output="Lungs Disease Confirm"
    return render_template('lungs.html',output=output )

#liver

@app.route('/liver', methods=['GET','POST'])
def liver():
    output = ""

    if request.method == 'POST':
    
            # 🔹 Form values
            age = int(request.form['age'])
            gender = int(request.form['gender'])
            tb = float(request.form['tb'])
            db = float(request.form['db'])
            ap = float(request.form['ap'])
            aa = float(request.form['aa'])
            sa = float(request.form['sa'])
            tp = float(request.form['tp'])
            alb = float(request.form['alb'])
            agr = float(request.form['agr'])

            test_data = [age, gender, tb, db, ap, aa, sa, tp, alb, agr]

            import pandas as pd
            from sklearn.model_selection import train_test_split
            from sklearn.neighbors import KNeighborsClassifier
            from sklearn.linear_model import LogisticRegression
            from sklearn import tree

            from sklearn.metrics import accuracy_score
            
            # 🔹 Load dataset
            df = pd.read_csv("static/liver.csv")

            df.head()

            df.tail()

            df.describe()

            df.info()

            df['Gender'] = df['Gender'].map({'Male':1, 'Female':0})
            df['LiverDisease'] = df['LiverDisease'].map({'YES':1 ,"NO":0})

            # 🔹 Target column
            x = df.drop('LiverDisease', axis=1)
            y = df['LiverDisease']
           

            x.shape
            y.shape

            x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

            x_train.shape

            x_test.shape

            model = LogisticRegression()
            x_test.shape
            model.fit(x_train, y_train)

        

            predicted_output = model.predict(x_test)
            print(predicted_output)
            print(y_test)

            accuracy = accuracy_score(y_test, predicted_output)
            print(accuracy)

            Predictions= model.predict([test_data])

            print(Predictions)
            # 🔹 Prediction
            

            if Predictions[0] == 1:
                output = "Liver Disease Detected"
            else:
                output = "No Liver Disease"

    return render_template('liver.html', output=output)

#kidney

@app.route('/kidney',methods=['GET','POST'])
def kidney():
    output = ""

    if request.method == 'POST':
    
            # 🔹 Form values
            age = int(request.form['age'])
            bloodpressure = int(request.form['bloodpressure'])
            sg = float(request.form['sg'])
            al = int(request.form['al'])
            sugar = int(request.form['sugar'])
            bu = float(request.form['bu'])
            sc = float(request.form['sc'])
            sodium = float(request.form['sodium'])
            potassium = float(request.form['potassium'])
            hg = float(request.form['hg'])

            test_data = [age, bloodpressure, sg, al, sugar, bu, sc, sodium, potassium, hg]
            
            import pandas as pd
            from sklearn.model_selection import train_test_split
            from sklearn.neighbors import KNeighborsClassifier
            from sklearn.linear_model import LogisticRegression
            from sklearn import tree

            from sklearn.metrics import accuracy_score

            data = pd.read_csv("static/kidney.csv")

            data.head()

            data.tail()

            data.describe()

            data.info()

            data['KidneyDisease'].replace(['YES','NO'],[1,0], inplace=True)

            data.info()

            x= data.drop('KidneyDisease', axis=1)
            y= data['KidneyDisease']

            x.shape
            y.shape

            x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

            x_train.shape

            x_test.shape

            model = LogisticRegression(max_iter=1000)
            x_test.shape
            model.fit(x_train, y_train)

            model.fit(x_train, y_train)

            predicted_output = model.predict(x_test)
            print(predicted_output)
            print(y_test)

            accuracy = accuracy_score(y_test, predicted_output)
            print(accuracy)

            Predictions= model.predict([test_data])

            print(Predictions)

            if Predictions[0] == 1:
                output = "Kidney Disease Detected"
            elif Predictions[0] == 0:
                output = "No Kidney Disease"

    return render_template('kidney.html', output=output)


# Prediction route

if __name__ == "__main__":
    app.run(port=5000,debug=True)