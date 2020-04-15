#!/usr/bin/python


import requests
import json
import os
import datetime
import random


#### declaring  empty lists:

list = []
st = []

# ICINGA API to pull downtime list:

reports = os.system('curl -u root:asdfasdfasdf -s -k "https://icingaexample.com:5665/v1/objects/downtimes?joins=host.name" | python -m json.tool | more > /tmp/downtime.json')

# Function to grab the host list which was scheduled only before 15 mins from Icinga:
# Note - Icinga downtime list returns timing in EPOCH time format , you have to convert this time into human readable time

def time1():
    time1.start_time_before_5_mins = datetime.datetime.now() - datetime.timedelta(minutes=15)
    ''' below varaible to convert (start_time_before_5_mins) into EPOCH time'''
    time1.start_time_before_5_mins_epoch = time1.start_time_before_5_mins.strftime('%s')
    return time1.start_time_before_5_mins_epoch


#Function to convert the JSON output and to grab two values which is Entity ID and Display ID
# Note -  Dynatrace would have mapped ENTITYID in place of Hostname, so you have to find out the actual ENTITYID against the HostName which comes from the ICINGA downtime list
#requests.get ==> is to have load the Json results to a file  in later part "hello.txt and equivalent BASH command is curl with GET call . so to see results of JSON output, you have to open hello.txt to see results
#The second WITH statement is to read the JSON output which was dumped earlier in the FIRST WITH statement results.

def dyna():
    token="asdxasdW1JWLxX09a"
    headers = { 'Authorization': "Api-Token asdxasdW1JWLxX09a" }
    r = requests.get{'https://dynatracetest1.sample.com/e/44ae-477c-09asdc/api/v1/entity/infrastructure/hosts', headers=headers, verify=False)
    j = json.loads(r.text)
    ''' Invoking the service_name variable from the main function below and splitting it to get a string value'''
    s = service_name.split('!')[0]
    ss = str(s)
    with open("hello.txt","w") as f:
        json.dump(j,f,indent=4)

    with open("hello.txt","r") as file:
        data = json.load(file)
        for p in data:
            name = str(p['displayName'])
            ent = str(p['entityId'])
            for i in ss:
                if ss in name:
                    list.append(ent)
    return list


# Assigning the time1 function to a Object variable:
# Main Function which will pull host list from ICINGA API:
# ICINGA API sample
# Schedule this in CRON or in same script itself - 
# reports = os.system('curl -u root:asdfasdfdsf -s -k "https://icingatest:5665/v1/objects/downtimes?join=host.name" | python -m json.tool | more > /tmp/list_downtime.json')

a = time1()
with open('/tmp/list_downtime.json') as json_file:
    data = json.load(json_file)
    for p in data['results']:
        service_name = p['attrs']['__name']
        end_time = str(p['attrs']['end_time']
        start_time = str(p['attrs']['start_time'])
  
# Below steps to generate a random variable to have different USER ID, Just at last it will have random number after the USER ID, the idea being DYNATRACE overwrites / REMOVE the existing donwtime if the HOST is already in downtime and that would create problem later , so we came with RANDOM user id concept.

        ids = str(p['attrs']['author'])
        ids_ic = "icinga"
        id_random = random.choice([1,2,3,4,5,6,7,8,9])
        id_randoms = str(p['attrs']['author'])

# Below lines to convert start and end time from EPOCH time to normal time , since ICINGA returns time in EPOCH and DYNATRACE accept datetime in human readable format and passing to Dynatrace API
        if a < start_time:
            # Below print just for testing and assigning DYNA function to a OBJECT variable:
            print service_name,start_time,end_time
            entity = dyna ()
            payload = { 'id' : id_randoms, 'type' :'Planned', 'description': 'Icinga over Dyna', 'suppressAlerts': 'False', 'suppressProblems' : 'False', 'scope' : { 'entities' : entity , 'matches': [] }, 'schedule': { 'type': 'Once', 'timezoneId': 'America/Phoenix', 'maintenanceStart': normal_start_time, 'maintenanceEnd' : normal_end_time } }
            headers = { 'Authorization': 'Api-Token asdxasdW1JWLxX09a', 'content-type': 'application/json' }
            r_last = requests.post('https://dynatracetest1.sample.com/e/44ae-477c-09asdc/api/v1/maintenance', data=json.dumps(payload),headers=headers, verify=False)

    
