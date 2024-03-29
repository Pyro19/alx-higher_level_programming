#!/usr/bin/python3
"""
 Takes in a URL, sends a request to the URL and displays the body of the response.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    status = requests.get(argv[1]).status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(requests.get(argv[1]).text)
