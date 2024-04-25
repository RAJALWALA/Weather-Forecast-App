import requests

API_key = "376110fc6ea64fd374017c5f72e00da3"

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content["list"]
    nr_values = 8 * forecast_days
    filtered_content = filtered_content[:nr_values]
    if kind == "Temperature":
        filtered_content = [dict["main"]["temp"]for dict in filtered_content]
    if kind == "Sky":
        filtered_content = [dict["weather"][0]["main"]for dict in filtered_content]
    return filtered_content

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))
