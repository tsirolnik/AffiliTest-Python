from affilitest import api as affapi
from affilitest import devices
import queue
from threading import Thread

DEMO_TEST_COUNTRY = 'us'
DEMO_TEST_DEVICE = devices.ANDROID

NUM_THREADS = 4

def main():
    # Create a new instance of the API
    api = affapi.AffiliTest('example@mail.com',  'password')
    # Use login the acquire session and relevant permissions
    api.login()
    print('Logged in')

    # Create a new queue
    q = queue.Queue()

    # Setup NUM_THREADS
    for i in range(NUM_THREADS):
      thread = Thread(target=worker, args=(q, api.clone(),))
      thread.setDaemon(True)
      thread.start()
      print('Started thread', i)


    test_items = [
      { 'url':'http://google.com', 'country':DEMO_TEST_COUNTRY, 'device':DEMO_TEST_DEVICE },
      { 'url':'http://cnn.com', 'country':DEMO_TEST_COUNTRY, 'device':DEMO_TEST_DEVICE },
      { 'url':'http://yahoo.com', 'country':DEMO_TEST_COUNTRY, 'device':DEMO_TEST_DEVICE },
      { 'url':'http://facebook.com', 'country':DEMO_TEST_COUNTRY, 'device':DEMO_TEST_DEVICE }
    ]

    for item in test_items:
      q.put(item)

    # Wait for the tasks to be done
    q.join()


def worker(q, api):
    while True:
      print('Done!', test(q.get(), api))
      # This queue item is off the list
      q.task_done()


def test(test_item, api):
    # Call the regular test endpoint
    return api.test(
        test_item['url'],
        test_item['country'],
        test_item['device']
    )

if __name__ == '__main__':
    main()
