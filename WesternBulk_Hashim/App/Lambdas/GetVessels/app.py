import boto3
from botocore.exceptions import ClientError


def handler(event, context):
    print("Value of the event object = ", event)

    if event.get("id"):
        dynamo_db = boto3.resource('dynamodb')
        vessel_table = dynamo_db.Table("Vessel")
        try:
            response = vessel_table.get_item(Key=
            {
                'vesselId': event.get('id')
            })
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            vessel = response.get('Item')
            if vessel:
                print("Vessel info = ", vessel)
                return vessel
            else:
                print("No vessel found with id = {}".format(event.get('id')))
                return {'msg': "No vessel found with id = {}".format(event.get('id'))}
    else:
        print("id Can not be empty in the event = {}".format(event))
