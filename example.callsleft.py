from affilitest import api as affapi


def main():
    # Create a new instance of the API
    # Pass your API Key if you have one
    api = affapi.AffiliTest() 
    # Use login the acquire session and relevant permissions
    # Not needed if the API Key was supplied
    api.login('example@mail.com',  'password')

    # Using Google Play Store URL
    response = api.calls_left()
    print(response)

if __name__ == '__main__':
  main()