import boto3

def handler(event, context):
    print("Value of the event object = ", event)

    if event.get('vesselId'):
        dynamo_db = boto3.resource('dynamodb')
        vessel_table = dynamo_db.Table("Vessel")
        try:
            vessel_table.put_item(
                Item={
                    'vesselId': event.get('vesselId'),
                    'vesselName': event.get('vesselName'),
                    'speed': event.get('speed'),
                    'latitude': event.get('latitude'),
                    'longitude': event.get('longitude')
                })
            print("Successfully inserted item")
        except Exception as ex:
            print("Exception Error = {}".format(ex))
            raise ex
    else:
        print("vesselId Can not be empty in the event = {}".format(event))

    return {
        'body': "Successfully inserted vessel with id = {}".format(event.get('vesselId'))
    }
