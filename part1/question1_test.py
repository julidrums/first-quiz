from question1 import get_city_weather
from question1 import get_city_temperature

def test_get_city_weather():

  assert get_city_weather("Quito") == '22 degrees and None'

  assert get_city_weather("New York") == "None degrees and rainy"


