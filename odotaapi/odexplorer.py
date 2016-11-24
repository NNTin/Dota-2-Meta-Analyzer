import requests
import time
from converter import urlconverter
#from reddit.botinfo import message
message = False

def ODExplorer(SQLQuery, q=None):

    try:
        response = {}
        attempt = 0

        while response == {}:

            if message: print('[odexplorer] sending SQL query to OD explorer')

            URL = 'http://api.opendota.com/api/explorer?sql=' + urlconverter.URLConverter(SQLQuery)
            response = requests.get(URL)
            response.connection.close()
            response = response.json()

            # careful Steam API sometimes returns empty JSONs!
            # handle this error!

            if response == {}:
                attempt += 1
                if (attempt == 10):
                    print('Tried %s times, cancelling API request. (Skipped counter increases)')
                    if q == None:
                        return response
                    else:
                        q.put(response)
                    break
                print('Failed API request, retrying in %s seconds' %(attempt * 2))
                print(URL)
                time.sleep(attempt * 2)
                continue
            else:
                if q == None:
                    return response
                else:
                    q.put(response)


    except:
        print('[odexplorer] there was an error, couldn\'t query on OD explorer: %s' %SQLQuery)

        response = {}
        if q == None:
            return response
        else:
            q.put(response)

        # future, retry until it works!
