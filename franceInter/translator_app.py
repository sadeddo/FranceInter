import  uuid, json
import pip._vendor.requests as requests

def traduction(message):
    # Add your key and endpoint
    key = "3828ee9780c04a4bb4554897c8efc0d2"
    endpoint = "https://api.cognitive.microsofttranslator.com/"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "westeurope"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'fr',
        'to': ['en']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': 'fec2ec624eb9426db1cae4191cd0056f',
        'Ocp-Apim-Subscription-Region': 'westeurope',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': message
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response[0]['translations'][0]['text']

