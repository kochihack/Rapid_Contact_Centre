import json
import boto3


def LocationIntent(event, context, varCustomerPhoneNumber):
    varDisLoc = event["currentIntent"]["slots"]["disaster_Loc"]

    string = "PhoneNumber : " + varCustomerPhoneNumber + " Slots : " + varDisLoc
    encoded_string = string.encode("utf-8")

    bucket_name = "dmgmt"
    file_name = "hello1.txt"
    s3_path = "100001/20180223/" + file_name

    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)

    ret = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": "We have registered your Location we are sending you help, they are on the way, stay safe!"
            }
        }
    }

    return ret


def HelpIntent(event, context):
    ret = {
        "dialogAction": {
            "type": "ElicitSlot",
            "message": {
                "contentType": "PlainText",
                "content": "Please relax, we are here to help you. Please let me know your current location?"
            },
            "intentName": "Disaster_Location",
            "slots": {
                "disaster_Loc": ""
            },
            "slotToElicit": "disaster_Loc"

        }
    }
    return ret


def ElseIntent(event, context):
    ret = {
        "dialogAction": {
            "type": "ElicitIntent",
            "message": {
                "contentType": "PlainText",
                "content": "We are assisting some one, We will be with you soon to help you!"
            }
        }
    }

    return ret


def lambda_handler(event, context):
    varCustomerPhoneNumber = ""

    try:
        varCustomerPhoneNumber = event['sessionAttributes']['CustomerPhoneNumber']
    except:
        varCustomerPhoneNumber = ""

    CurrentIntent = event['currentIntent']['name']

    if (CurrentIntent == "Disaster_Call"):
        ret = HelpIntent(event, context)
    elif (CurrentIntent == "Disaster_Location"):
        ret = LocationIntent(event, context, varCustomerPhoneNumber)
    else:
        ret = ElseIntent(event, context)

    return ret
