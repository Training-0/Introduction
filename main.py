import requests

print("hello world")
# r = requests.get("https://google.com")
# print(r.status_code) #akan keluar angka 200 = sudah sesuai
# if r.status_code == 200:
#     print(r.text) # mencetak isi halaman dari request diatas

# digunakan untuk mengatasi apabila ada error yang terjadi
try:
    r = requests.get("https://goo gle.com")
    print(r.status_code)  # akan keluar angka 200 = sudah sesuai
    if r.status_code == 200:
        print(r.text)  # mencetak isi halaman dari request diatas
except Exception as e:
    print('Have a problem',e)