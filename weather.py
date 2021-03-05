import geocoder
import requests

#You would put your API Key below
API_KEY = 'XXXXXXXXXXX'
API_BASE_URL = f'https://api.openweathermap.org/data/2.5/weather?units=imperial&appid='  #<---- You would put your API Key in this string right next to "appid=" .

def main():
  destinations = destinations = [geocoder.arcgis('Atlanta,Georgia'), geocoder.arcgis('Sandy Springs, Georgia'),  geocoder.arcgis('Birmingham, AL'), geocoder.arcgis('Yosemite National Park'), geocoder.arcgis('Las Vegas, Nevada'), geocoder.arcgis('Grand Canyon National Park'), geocoder.arcgis('Aspen, Colorado'), geocoder.arcgis('Mount Rushmore'), geocoder.arcgis('Yellowstone National Park'), geocoder.arcgis('Sandpoint, Idaho'), geocoder.arcgis('Banff National Park'), geocoder.arcgis('Capilano Suspension Bridge')]

  # Loop through each destination
  for destination in destinations:
    latitude = destination.lat
    longitude = destination.lng
    degree_sign= u'\N{DEGREE SIGN}'
    
    full_api_url = API_BASE_URL + '&lat=' + str(latitude) + '&lon=' + str(longitude)
    result = requests.get(full_api_url).json()
   
    print(f'{destination.address} is located at ({latitude:.4f}, {longitude:.4f})')
    print(f"At {destination.address} now, it's {result['weather'][0]['description']} with a temperature of {result['main']['temp']:.1f}{degree_sign}\n ")
    
    

main()
