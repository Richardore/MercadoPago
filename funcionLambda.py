import json
import os
import mercadopago

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["TEST_TOKEN"])


    request_values = json.loads(event['body'])
    
    payment_data = {
    "transaction_amount": float(request_values["transaction_amount"]),
    "token": request_values["token"],
    "installments": int(request_values["installments"]),
    "payment_method_id": request_values["payment_method_id"],
    "issuer_id": request_values["issuer_id"],
    "payer": {
        "email": request_values["payer"]["email"],
        "identification": {
            "type": request_values["payer"]["identification"]["type"], 
            "number": request_values["payer"]["identification"]["number"]
            }
        }
    }


    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    
    return {
        "statusCode": 200,
        "headers":{
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS, DELETE"
        },
        
        "body": json.dumps({
            preference
        })
    }