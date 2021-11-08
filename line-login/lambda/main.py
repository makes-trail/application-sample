import json

def handler(event, context):
    print(event)
    
    try:
        claims = event['requestContext']['authorizer']['claims']
        user_info = {
            "userId": claims["cognito:username"],
            "name": claims["name"],
            "iconUrl": claims["picture"]
        }
        print(f'User logged in: {claims["name"]}')
        
        return {
            'statusCode': 200,
            'body': json.dumps(user_info)
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps("ERROR")
        }
