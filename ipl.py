import requests
import time
import os
os.system('cls')
api_address="https://www.cricbuzz.com/match-api/livematches.json"
url = api_address
while True:
    time.sleep(2)
    json_data = requests.get(url).json()
    format_add = json_data
    keys=[]
    for k, v in format_add['matches'].items():
        keys.append(k)

    for key in keys:

        name = format_add['matches'][key]['series']['name']
        print ('name : {}'.format(name))
        short_name=format_add['matches'][key]['series']['short_name']
        print ('short_name :{}'.format(short_name))
        stadium = format_add['matches'][key]['venue']['name']
        print ('Stadium : {}'.format(stadium))
        place = format_add['matches'][key]['venue']['city']
        print ('place : {}'.format(place))
        match_no=format_add['matches'][key]['match_desc']
        print('match number : {}'.format(match_no))
        short_namee=format_add['matches'][key]['team1']['name']
        short_nameee=format_add['matches'][key]['team2']['name']
        print('match between :{}'.format( short_namee  +' vs '+  short_nameee))
        toss=format_add['matches'][key]['toss']['winner']
        print('toss : {}'.format(toss))
        decision=format_add['matches'][key]['toss']['decision']
        print('decision : {}'.format(decision))
        score=format_add['matches'][key]['score']['bowling']['score']
        print ('first innings score :{}'.format(score))
        score=format_add['matches'][key]['score']['batting']['score']
        print ('second innings score :{}'.format(score))
        status=format_add['matches'][key]['status']
        print('status of match : {}'.format(status))
        print ('')
