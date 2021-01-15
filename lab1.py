import requests

#question2
print(requests.__version__)

#question3


r = requests.get('http://www.google.com/')
print("the status code for google home page is ",r.status_code)

r = requests.get('https://www.google.com/teapot')
print("the status code for google teapot page is ",r.status_code)