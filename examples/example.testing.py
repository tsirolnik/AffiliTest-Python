from affilitest import api as affapi
from affilitest import devices

def main():
    # Create a new instance of the API
    # Pass your API Key if you have one
    api = affapi.AffiliTest() 
    # Use login the acquire session and relevant permissions
    # Not needed if the API Key was supplied
    api.login('example@mail.com',  'password')
    print('Successfuly logged in, testing')

    # Call the regular test endpoint
    response = api.test(
        'http://google.com',
        'us', # us for the United States, il for Israel, de for Germany and etc
        devices.ANDROID,
        True # Placing True would return the raw data with its meta data
    )
    print(response)

    # Compare the results to preview URL
    response = api.compare_to_preview(
        'https://itunes.apple.com/us/app/whatsapp-messenger/id310633997?mt=8',
        'https://itunes.apple.com/us/app/whatsapp-messenger/id310633997?mt=8',
        'us', # us for the United States, il for Israel, de for Germany and etc
        devices.IPHONE,
    )
    print(response)


if __name__ == '__main__':
    main()
