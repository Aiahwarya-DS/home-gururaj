import json
import requests
import time

def lambda_handler(event, context):
    # TODO implement
    
    loop_for = 3
    turn_on = True
    
    for i in range(loop_for * 2):
        for j in range(13, 16):
            r = requests.get(url="http://188.166.206.43:80/DN4OM5C7yt07W5KJ_5JE9h8bvUwLa7Hc/update/D{}?value={}".format(j, "1" if turn_on else "0"))
            time.sleep(0.2)
        turn_on = not turn_on
            
        time.sleep(0.)
        
    
    print(r.content)
    # print(r.reason)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }



