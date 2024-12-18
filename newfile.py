import requests

headers = {
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzQ1MzcwMTAsImp0aSI6IjhlMTAxNjllLTBlNmQtNDZhYy1hNTczLWFkOTY0MDM4M2JlNiIsInN1YiI6IjI0Ymd6cGh4cHo5bnJoYnciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjI0Ymd6cGh4cHo5bnJoYnciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoiRWxlbWlzX2luc3RhbnQifX0.oUlEn7oVSxVWDhkWcyGsV6Bor4jYu-TrKnbiXSB8__m4FpWJbYKnRxOUuofdwts-dmI0dYjjEZB0dVFoUeoivQ',
    'Braintree-Version': '2018-05-10',
    'Content-Type': 'application/json',
    'Referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua-platform': '"Android"',
}

json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'dropin2',
        'sessionId': 'f0673453-8f42-4235-aaf0-075ae38b00e0',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': '4347692052399787',
                'expirationMonth': '03',
                'expirationYear': '2034',
                'cvv': '456',
                'billingAddress': {
                    'postalCode': '10080',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"clientSdkMetadata":{"source":"client","integration":"dropin2","sessionId":"f0673453-8f42-4235-aaf0-075ae38b00e0"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4347692052399787","expirationMonth":"03","expirationYear":"2034","billingAddress":{"postalCode":"10080"}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)




import requests

headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-TN,ar-EG;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://us.elemis.com',
    'referer': 'https://us.elemis.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'amount': 135.01,
    'additionalInfo': {
        'acsWindowSize': '03',
        'billingLine1': ' ',
        'billingCity': '',
        'billingPostalCode': '',
        'billingCountryCode': 'UK',
        'billingPhoneNumber': '',
        'billingGivenName': '',
        'billingSurname': '',
        'email': 'n.sakeer.j222211@gmail.com',
    },
    'challengeRequested': True,
    'bin': '432626',
    'dfReferenceId': '0_8c92d3d1-6195-4b00-a7fb-b1030669ee74',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.58.0',
        'cardinalDeviceDataCollectionTimeElapsed': 1215,
        'issuerDeviceDataCollectionTimeElapsed': 15018,
        'issuerDeviceDataCollectionResult': False,
    },
    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzQ1MzcwMTAsImp0aSI6IjhlMTAxNjllLTBlNmQtNDZhYy1hNTczLWFkOTY0MDM4M2JlNiIsInN1YiI6IjI0Ymd6cGh4cHo5bnJoYnciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjI0Ymd6cGh4cHo5bnJoYnciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoiRWxlbWlzX2luc3RhbnQifX0.oUlEn7oVSxVWDhkWcyGsV6Bor4jYu-TrKnbiXSB8__m4FpWJbYKnRxOUuofdwts-dmI0dYjjEZB0dVFoUeoivQ',
    'braintreeLibraryVersion': 'braintree/web/3.58.0',
    '_meta': {
        'merchantAppId': 'us.elemis.com',
        'platform': 'web',
        'sdkVersion': '3.58.0',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': 'f0673453-8f42-4235-aaf0-075ae38b00e0',
    },
}

response = requests.post(
    'https://api.braintreegateway.com/merchants/24bgzphxpz9nrhbw/client_api/v1/payment_methods/tokencc_bd_4zntfv_dw9gdf_hxm6gj_yrjycv_zr4/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"amount":135.01,"additionalInfo":{"acsWindowSize":"03","billingLine1":" ","billingCity":"","billingPostalCode":"","billingCountryCode":"UK","billingPhoneNumber":"","billingGivenName":"","billingSurname":"","email":"n.sakeer.j222211@gmail.com"},"challengeRequested":true,"bin":"432626","dfReferenceId":"0_8c92d3d1-6195-4b00-a7fb-b1030669ee74","clientMetadata":{"requestedThreeDSecureVersion":"2","sdkVersion":"web/3.58.0","cardinalDeviceDataCollectionTimeElapsed":1215,"issuerDeviceDataCollectionTimeElapsed":15018,"issuerDeviceDataCollectionResult":false},"authorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzQ1MzcwMTAsImp0aSI6IjhlMTAxNjllLTBlNmQtNDZhYy1hNTczLWFkOTY0MDM4M2JlNiIsInN1YiI6IjI0Ymd6cGh4cHo5bnJoYnciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjI0Ymd6cGh4cHo5bnJoYnciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoiRWxlbWlzX2luc3RhbnQifX0.oUlEn7oVSxVWDhkWcyGsV6Bor4jYu-TrKnbiXSB8__m4FpWJbYKnRxOUuofdwts-dmI0dYjjEZB0dVFoUeoivQ","braintreeLibraryVersion":"braintree/web/3.58.0","_meta":{"merchantAppId":"us.elemis.com","platform":"web","sdkVersion":"3.58.0","source":"client","integration":"custom","integrationType":"custom","sessionId":"f0673453-8f42-4235-aaf0-075ae38b00e0"}}'
#response = requests.post(
#    'https://api.braintreegateway.com/merchants/24bgzphxpz9nrhbw/client_api/v1/payment_methods/tokencc_bd_4zntfv_dw9gdf_hxm6gj_yrjycv_zr4/three_d_secure/lookup',
#    headers=headers,
#    data=data,
#)