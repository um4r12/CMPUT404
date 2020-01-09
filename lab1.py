import requests;


print(requests.__version__)

get_request = requests.get("https://raw.githubusercontent.com/um4r12/CMPUT404/master/lab1.py")
print(get_request.content)
