project_id = 'bigquery-266522'
compute_region = 'us-central1'
model_display_name = 'Turnover_20200209074919'
inputs = {'Effective_Date': '2018-04-18 16:48:37', 
            'Work_City':'Rockton','Age':25.1, 
            'Job_Title':'Prodctn/Maint, Prodctn Worker', 
            'Length_of_Service':1.2, 
            'Job_Function': 'Operations', 
            'Work_State':'Illinois', 
            'Job_Family':'Prodctn Worker', 
            'Category': 'Production Maintenance', 
            'Major_Bus_Node_Name':'Building Solutions & Services', 
            'Ethnicity':'White (Not Hispanic or Latino)', 
            'Grade':'PM', 'Gender':'Male', 
            'Record_Source': 'WORKDAY', 
            'Work_Country':'United States'}

feature_importance = None

from google.cloud import automl_v1beta1 as automl

client = automl.TablesClient(project=project_id, region=compute_region)

if feature_importance:
    response = client.predict(
        model_display_name=model_display_name,
        inputs=inputs,
        feature_importance=True,
    )
else:
    response = client.predict(
        model_display_name=model_display_name, inputs=inputs
    )

data = {}

for result in response.payload:
    data[str(result.tables.value.string_value)] = result.tables.score

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify(Predictions=data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
