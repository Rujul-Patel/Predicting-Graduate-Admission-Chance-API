# Admission-Chance-API
An end to end Machine Learning Project demo, which provides API to predict the chance of admission for graduate course.

### 
 * Link to Ipython Notebook [Supervised Learning - Chance of Admission](https://github.com/Rujul-Patel/Data-Science-and-ML/blob/master/Supervised-Graduate-Admission.ipynb)
 
### API Usage
-----
 * Hosted on https://admission-chance.herokuapp.com/predict
 
 * Check Server Status
 ```
 curl https://admission-chance.herokuapp.com/test
 ```
 
 * Predict a data point
 ```
 curl \
--header "Content-Type: application/json" \
--request POST \
--data \
'{
	"GRE Score":312.00,
	"TOEFL Score":108.00,
	"University Rating":3.00,
	"SOP":3.50,
	"LOR":3.00,
	"CGPA":8.53,
	"Research":0.00
}' \
https://admission-chance.herokuapp.com/predict
```

* Can also test from here : https://apitester.com/shared/checks/6501686e99f04982a53286a459045b9f

### Project Structure
-----

```
.
├── app
│   ├── app.py
│   └── wsgi.py
├── docker-compose.yml
├── Dockerfile
├── model
│   ├── graduate_admission.csv
│   └── model.py
└── requirements.txt
```

<ul>
  <li>app
    <ul>
      <li> app.py  :- Flask application that reads model from binary and returns prediction for the given data-point.</li>
      <li> wsgi.py :- WSGI server Configuration</li>
    </ul>
  </li>
  <li>model
    <ul>
      <li>graduate_admission.csv :- Data to train model. Source : https://www.kaggle.com/mohansacharya/graduate-admissions</li>
      <li>model.py :- Trains the models and stores it in a binary file.</li>
    </ul>
  </li>
</ul>

###### Note : Refer [this Ipython Notebook](https://github.com/Rujul-Patel/Data-Science-and-ML/blob/master/Supervised-Graduate-Admission.ipynb) for EDA and use of other supervised models on this dataset

  
### Building the project using docker
----

Build Manually
```
docker build -t flask .
docker run -d -p 5000:5000 flask
```

Or use docker-compose
```
docker-compose up
```

-----
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)




