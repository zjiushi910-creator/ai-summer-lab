import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url, timeout=5)

number = 10

try :
    print(number / 0)
except ZeroDivisionError as e:
    print(f"除数出错：{e}")
