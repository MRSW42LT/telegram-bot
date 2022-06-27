from requests_html import HTMLSession

def get_climate(city):
    url = f'https://www.google.com/search?q=weather+{city}'

    r = HTMLSession().get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'})

    temp = 'Temperature: ' + r.html.find('span#wob_ttm', first=True).text
    description = r.html.find('span#wob_dc', first=True).text
    humidity = 'Humidity: ' + r.html.find('span#wob_hm', first=True).text
    wind = 'Wind: ' + r.html.find('span#wob_tws', first=True).text
    rain = 'Rain : ' + r.html.find('span#wob_pp', first=True).text
    location = r.html.find('#wob_loc', first=True).text

    data = f"\n\n {location} \n {temp} \n {humidity} \n {rain} \n {description} \n {wind}"

    return data
