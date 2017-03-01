import urllib, json, time

def beautify_json(jvalue):
    return json.dumps(jvalue, indent=4, sort_keys=True)

furl = urllib.urlopen(
    "http://api.openweathermap.org/data/2.5/forecast/daily?q=Hyderabad&units=metric&cnt=7&APPID=cbf65e03a91e42aebd4ebba2d136c270")
parsed = json.loads(furl.read())
print beautify_json(parsed['list'])
wlist = parsed['list']
for i in range(len(wlist)):
    print wlist[i]['weather'][0]['description'], wlist[i]['temp']['max'], wlist[i]['temp']['min'], time.strftime("%d/%m/%y", time.localtime(int(wlist[i]['dt'])))