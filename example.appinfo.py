from affilitest import api as affapi


def main():
    # Create a new instance of the API
    # Pass your API Key if you have one
    api = affapi.AffiliTest() 
    # Use login the acquire session and relevant permissions
    # Not needed if the API Key was supplied
    api.login('example@mail.com',  'password')

  # Using Google Play Store URL
  response = api.app_info(url = 'https://play.google.com/store/apps/details?id=com.whatsapp&hl=en')
  print(response)

  # Using iTunes app store URL
  response = api.app_info(url = 'https://itunes.apple.com/us/app/whatsapp-messenger/id310633997?mt=8')
  print(response)

  # Using Google Play Store package name
  response = api.app_info(package = 'com.whatsapp')
  print(response)

  # Calling the app info with an iTunes app store package
  # This requires specifying the country too.
  # The country is a two letter string as described by ISO 3166-alpha-2.
  # e.g - us for the United States, il for Israel, de for Germany and so on
  response = api.app_info(package = '310633997', country = 'us')
  print(response)

if __name__ == '__main__':
  main()