from urllib import request

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
prev_response = request.urlopen(url + "44827")

for i in range(400):
    prev_num = prev_response.read().split()[-1]
    prev_str = "".join((chr(i) for i in prev_num))
    print(prev_str)
    prev_response = request.urlopen(url + prev_str)

