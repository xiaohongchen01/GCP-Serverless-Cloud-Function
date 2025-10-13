import json
import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Expects JSON or query param with 'PaO2' (arterial oxygen tension, mmHg).
    Returns a JSON classification of oxygenation status.
    """
   
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    pao2_val = data.get("PaO2", args.get("PaO2"))

    if pao2_val is None:
        return (
            json.dumps({"error": "Please provide the patient's PaO2 lab value in mmHg!"}),
            400,
            {"Content-Type": "application/json"},
        )


    try:
        pao2 = float(pao2_val)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "PaO2 must be a valid number."}),
            400,
            {"Content-Type": "application/json"},
        )

  
    if 80 <= pao2 <= 100:
        result = "normal"
    elif 60 <= pao2 < 80:
        result = "abnormal: mild hypoxemia"
    elif 40 <= pao2 < 60:
        result = "abnormal: moderate hypoxemia"
    elif 0 < pao2 < 40:
        result = "abnormal: severe hypoxemia"
    elif pao2 > 100:
        result = "abnormal: hyperoxemia"
    else:
        result = "undetermined"

    payload = {
        "PaO2": pao2,
        "result": result,
    }

    return json.dumps(payload), 200, {"Content-Type": "application/json"}
