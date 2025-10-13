import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    PaO2 = req.params.get('PaO2')
    if not PaO2:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = None   
        if req_body:
            PaO2 = req_body.get('PaO2')

    if PaO2 is None:  
        return func.HttpResponse(
            json.dumps({"error": "Please provide the patient's PaO2 lab value in mmHg!"}),
            status_code=400,
            mimetype="application/json"
        )

    try:
        PaO2 = float(PaO2)
    except (TypeError, ValueError): 
        return func.HttpResponse(
            json.dumps({"error": "PaO2 must be valid numbers."}),
            status_code=400,
            mimetype="application/json"
        )

    if 80 <= PaO2 <= 100:
        PaO2_Results = "normal"
    elif 60 <= PaO2 < 80:
        PaO2_Results = "abnormal: mild hypoxemia"
    elif 40 <= PaO2 < 60:
        PaO2_Results = "abnormal: moderate hypoxemia"
    elif 0 < PaO2 < 40:
        PaO2_Results = "abnormal: severe hypoxemia"
    elif PaO2 > 100:
        PaO2_Results = "abnormal: hyperoxemia"
    else:
        PaO2_Results = "abnormal: undetermined"

    return func.HttpResponse(
        json.dumps({
            "PaO2": PaO2,
            "PaO2_Results": PaO2_Results
        }),
        mimetype="application/json"
    )




## post request code
import requests

url = f"https://pao2-lab-values-drd6gcgeapbufxeb.canadacentral-01.azurewebsites.net/api/http_trigger1?code=YS2RIO2lVYt0bdf61fYAH2QlfbccAYxEmj2T7ZqF6U0cAzFuSqM20g=="
KEY = "YS2RIO2lVYt0bdf61fYAH2QlfbccAYxEmj2T7ZqF6U0cAzFuSqM20g=="

rq = requests.post(url, json={"PaO2": 65}, params={"code": KEY}, timeout=10)
print("POST:","Status Code:", rq.status_code, rq.json())


## get request code
import requests

url = f"https://pao2-lab-values-drd6gcgeapbufxeb.canadacentral-01.azurewebsites.net/api/http_trigger1?code=YS2RIO2lVYt0bdf61fYAH2QlfbccAYxEmj2T7ZqF6U0cAzFuSqM20g=="
KEY = "YS2RIO2lVYt0bdf61fYAH2QlfbccAYxEmj2T7ZqF6U0cAzFuSqM20g=="

params = {
    "PaO2": 33,
    "code": KEY}

req = requests.get(url, params=params, timeout=10)
print("GET:","Status Code:", req.status_code, req.json())