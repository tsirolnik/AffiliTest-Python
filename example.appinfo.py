from affilitest import api as affapi


def main():
  # Create a new instance of the API
  api = affapi.AffiliTest('example@mail.com',  'password')
  # Use login the acquire session and relevant permissions
  api.login()

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
  response = api.app_info(package = '310633997', country = 'us')
  print(response)

if __name__ == '__main__':
  main()