import pandas as pd
import numpy as np


from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error


def build_model():
    print("Creating the model .... ")

    #Read the dataset
    df = pd.read_csv("./model/graduate_admission.csv")



    #Preparing the data
    X = df.drop('Chance of Admit ',axis=1)
    X = X.drop('Serial No.',axis=1)
    y = np.array(df['Chance of Admit ']).reshape(-1,1)


    #Split train and test data
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=7)

    #Linear Regression Model
    reg = LinearRegression()
    reg.fit(X_train,y_train)

    #Evaluate Model
    yp_test = reg.predict(X_test)
    rmse = (np.sqrt(mean_squared_error(y_test,yp_test))).round(2)
    r2 = round(reg.score(X_test,y_test),2)

    

    print("Model performance on Test set")
    print("----------------------------------")
    print("RMSE is {} ".format(rmse))
    print("R^2 score is {}".format(r2))
    print("\n")



    #Save the model
    import pickle

    with open("./model/model.bin","wb") as f_out:
        pickle.dump(reg,f_out)
        f_out.close()



    print("Saved Model to model.bin")
    print("Exiting ... ")

    return 1





build_model()
