import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                    'cond, temp, feelslike, loc, scale')

def main():
    # print header
    print_the_header()
    code = input('What zipcode are you requesting the weather for?')
    html = get_html(code)

    report = get_weather_from_html(html)
    print("The temp in {} is {}, and feels like {}\n It's a {} day".format(report.loc, report.temp, report.feelslike, report.cond))

def print_the_header():
    print('*************************')
    print('      Weather App')
    print('*************************')
    print()

def get_html(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    #cityCss = '.region-content-header h1'
    #weatherScaleCss = '.wu-unit-temperature.wu-label'
    #weatherTempCss = '.wu-unit-temperature.wu-value'
    #weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    feels_like = soup.find(class_='feels-like').find(class_='temp').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()
    loc2 = cleanup_text(loc)
    condition2 = cleanup_text(condition)
    feels_like2 = cleanup_text(feels_like)
    temp2 = cleanup_text(temp)
    scale2 = cleanup_text(scale)
    #print(loc, condition, 'feels like:' + feels_like, temp, scale)
    report = WeatherReport(cond=condition2, temp = temp2, scale = scale2, feelslike = feels_like2, loc = loc2)
    return report
    #return loc2, condition2, feels_like2, temp2, scale2

def cleanup_text(text: str):
    if not text:
        return text
    text = text.strip()
    return text



if __name__ == '__main__':
    main()
