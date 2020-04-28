import requests



def Weather(name_city):
    s_city = name_city
    city_id = 0
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': "6b1a916104032c9990483fae25b6539e"})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        city_id = data['list'][0]['id']
    except Exception as e:
        print("Exception (find):", e)
        pass                       
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                            params={'id': city_id, 'units': 'metric', 'lang': 'Eng', 'APPID': "6b1a916104032c9990483fae25b6539e"})
        
        data = res.json()

        weth = str(data['weather'][0]['description']) +"@"+ str(data['main']['temp'])
        weth = weth + ("@"+str(data['wind']['speed']) +"@"+ str(data['main']['humidity']) +"@"+  str(data['main']['pressure'])+"@")
        return weth
    except Exception as e:
        msd ='Enter the right name(with ",")'
        return msd

