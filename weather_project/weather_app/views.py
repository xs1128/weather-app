import datetime as dt
import requests
from django.shortcuts import render
from zoneinfo import ZoneInfo

# Create your views here.
def home(request):
    # Weather API requests paramaeters
    BASE_URL = "http://api.weatherapi.com/v1"
    API_METHOD = "/current.json/forecast.json"
    API_KEY = "42cc03750a834b628fb55045240305" #This API key is expired, please create your own
    geo_location = ""
    # Requird only with forecast API method
    days = 7
    lang = None
    """
    Implement all other params when moving to another independent file
    """

    if request.method == "POST":
        geo_location = request.POST['city']
        fetch_url = f"{BASE_URL}{API_METHOD}?key={API_KEY}&q={geo_location}&days={days}&lang={lang}"
        data = fetch_weather(geo_location, API_KEY, fetch_url)

        return render(request, "home.html", data)
    else:
        return render(request, "home.html")


def fetch_weather(location, api, fetch_url):
    res = requests.get(fetch_url)

    data = res.json()
    data["hourly_forecast"] = []

    try:
        data['location']['date'] = data['location']['localtime'].split(" ")[0]

        for days in data['forecast']['forecastday']:
            date = days['date'].split("-")
            days['formatted_date'] = date[1] + "-" + date[2]

        for i, d in enumerate(data["forecast"]["forecastday"]):
            if d["date"] == str(dt.date.today()):
                for hours in d["hour"]:
                    if int(hours["time"].split(" ")[1].split(":")[0]) >= (dt.datetime.now(ZoneInfo(data["location"]["tz_id"])).hour):
                        data["hourly_forecast"].append({"hour": hours["time"].split(" ")[1], "chance": hours["chance_of_rain"]})

                for hours in data["forecast"]["forecastday"][i]["hour"]:
                    if int(hours["time"].split(" ")[1].split(":")[0]) <= (dt.datetime.now(ZoneInfo(data["location"]["tz_id"])).hour):
                        data["hourly_forecast"].append({"hour": hours["time"].split(" ")[1], "chance": hours["chance_of_rain"]})
    except KeyError:
        pass

    if res.status_code == requests.codes.ok:
        pass
    else:
        print("Error" + str(data["error"]["code"]) + ": " + str(data["error"]["message"]))

    return data
