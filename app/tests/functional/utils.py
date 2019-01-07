import json

def get_access_token(client):
    email = "root@flask.com"
    password = "flaskiscool"

    query = json.dumps(
        {'query':
         '''mutation M {
                loginUser(email: "'''+email+'''", password: "'''+password+'''") {
                    accessToken
                    refreshToken
              }
            }
       '''
    })
    response = client.post(
        '/graphql',
        data=query,
        content_type='application/json'
    )

    content = json.loads(response.data)

    return content['data']['loginUser']['accessToken']
