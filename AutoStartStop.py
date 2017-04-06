import boto3
import datetime
import sys

print 'ec2auto start'

from apiclient.discovery import build

API_KEY = 'AIzaSyC-T_K-SZKhRWiEwZUwKsHeSlo089w3hN8'
CALENDAR_ID = 'ja.japanese#holiday@group.v.calendar.google.com'

company_holiday_list = []

def lambda_handler(event, context):
    client = boto3.client('ec2')

    # AutoShutdown = AUTO -> Auto Start/Stop
    # AutoShutdown = AUTO -> Auto Stop only
    query_start = [
        {'Name': 'tag:AutoShutdown', "Values": ['AUTO']},
        {'Name': 'instance-state-name', "Values": ['stopped']}
    ]
    query_stop = [
        {'Name': 'tag:AutoShutdown', "Values": ['ON', 'AUTO']},
        {'Name': 'instance-state-name', "Values": ['running']}
    ]

    service = build(serviceName='calendar', version='v3', developerKey=API_KEY)
    events = service.events().list(calendarId=CALENDAR_ID).execute()
    holiday_list = []

    for item in events['items']:
        holiday_list.append(item['start']['date'])

    holiday_list.extend(company_holiday_list)

    try:
        # Weekday only
        if '[arn:aws:events:ap-northeast-1:633064615840:rule/ec2start]' in event['resources']:
            print 'ec2start'
            if not str(datetime.date.today()) in holiday_list:
                client.start_instances(InstanceIds=get_instanceid(query_start))

        elif '[arn:aws:events:ap-northeast-1:633064615840:rule/ec2stop]' in event['resources']:
            print 'ec2stop'
            client.stop_instances(InstanceIds=get_instanceid(query_stop))

        elif '[arn:aws:events:ap-northeast-1:633064615840:rule/ec2stop_call]' in event['resources'] \
                and (not str(datetime.date.today()) in holiday_list):
            print 'ec2stop_call'
            # To notify to Slack or so.

    except Exception as e:
        # Error Handling.

    print 'SUCCESS: task succeeded'
#    return


def get_instanceid(query):
    client = boto3.client('ec2')
    response = client.describe_instances(Filters=query)

    ec2_count = len(response['Reservations'])
    ec2_list = []

    if not ec2_count == 0:
        for i in range(0, ec2_count):
            ec2_list.append(response['Reservations'][i]['Instances'][0]['InstanceId'])
        return ec2_list
    else:
        print("SUCCESS: specified hosts is None")
        sys.exit()