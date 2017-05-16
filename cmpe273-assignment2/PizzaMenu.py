from __future__ import print_function

import boto3
import json

print('Loading function')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    # '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    # access to the request and response payload, including headers and
    # status code.

    # To scan a DynamoDB table, make a GET request with the TableName as a
    # query string parameter. To put, update, or delete an item, make a POST,
    # PUT, or DELETE request respectively, passing in the payload to the
    # DynamoDB API as a JSON body.
    # '''
    
    dynamodb = boto3.resource('dynamodb', region_name='us-west-1', endpoint_url="https://dynamodb.us-west-1.amazonaws.com")


    table = dynamodb.Table('PizzaMenus')
    
    httpMethod = event.get('httpMethod')
    data = event.get('data')

    if httpMethod == "POST":    
        try:
            response = table.put_item(
               Item={
                    "menu_id":data["menu_id"],
                    "store_name" : data["store_name"],
                    "selection" : data["selection"],
                    "size" : data["size"],
                    "price" : data["price"],
                    "store_hours" : data["store_hours"]
                }
            )
        except:
            return "Invalid POST Request 400"
        else:
            return "200 OK"
    elif httpMethod == "GET":
        try:
            response = table.get_item(
                Key={"menu_id":event.get('param').get("menu_id")}
            )
        except:
            return "Invalid GET Request 400"
        else:
            return response['Item']
    elif httpMethod == "PUT":
        get_resp = table.get_item(
                Key={"menu_id":event.get('param').get("menu_id")}
            )
        existing_data = get_resp['Item']
        
        if event.get("store_name") == "":
            new_store_name = existing_data["store_name"]
        else:
            new_store_name = event.get("store_name")
        if len(event.get("size")) > 0:
            new_size = event.get("size")
        else:
            new_size = existing_data["size"]
        if len(event.get("selection")) > 0:
            new_selection = event.get("selection")
        else:
            new_selection = existing_data["selection"]
        if len(event.get("price")) > 0:
            new_price = event.get("price")
        else:
            new_price = existing_data["price"]
        if event.get("store_hours") == "":
            new_store_hours = existing_data["store_hours"]
        else:
            new_store_hours = event.get("store_hours")

        response = table.update_item(
            Key={
                "menu_id":event.get('param').get("menu_id")
            },
            UpdateExpression="set store_name = :sn, selection=:s, size=:sz, price=:p, store_hours=:sh",
            ExpressionAttributeValues={
                ':sn': new_store_name,
                ':s': new_selection,
                ':sz': new_size,
                ':p': new_price,
                ':sh': new_store_hours
            },
            ReturnValues="UPDATED_NEW"
        )
        print("size :")
        print(event.get("size"))
        print(type(event.get("size")))
        return "200 OK"
    
    elif httpMethod == "DELETE":
        try:
            table.delete_item(Key={'menu_id': event.get('param').get("menu_id")})
        except:
            return "Invalid DELETE Request 400"
        else:
            return "200 OK"
            

    #print("Received event: " + json.dumps(event, indent=2))

    # operations = {
    #     'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
    #     'GET': lambda dynamo, x: dynamo.scan(**x),
    #     'POST': lambda dynamo, x: dynamo.put_item(**x),
    #     'PUT': lambda dynamo, x: dynamo.update_item(**x),
    # }

    # operation = event['httpMethod']
    # if operation in operations:
    #     payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
    #     dynamo = boto3.resource('dynamodb').Table(payload['TableName'])
    #     return respond(None, operations[operation](dynamo, payload))
    # else:
    #     return respond(ValueError('Unsupported method "{}"'.format(operation)))
