import requests
from tkinter import messagebox
import time

urls = ['https://url_01','url_02']
errorCount = [0, 0, 0, 0]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

while True:
    for index,url in enumerate(urls):
        time.sleep(10)
        try:
            response = requests.get(url, headers = headers)
            response.raise_for_status()
            errorCount[index] = 0
            print(f"Request successful!, http status: {response.status_code} , url: {url}")
            time.sleep(1)
        except requests.exceptions.HTTPError as errh:
            errorCount[index] += 1
            time.sleep(1)
            if errorCount[index]== 6:
                print(f"HTTP Error: {errh}.")
                messagebox.showerror('HttpError',f'Http error: {errh}\nUrl: {url}')
        except requests.exceptions.ConnectionError as errc:
            errorCount[index] += 1
            time.sleep(1)
            if errorCount[index]== 6:
                print(f"Connection Error: {errc} .")
                messagebox.showerror('ConnectionError',f'Connection Error: {errc}\nUrl: {url}')
        except requests.exceptions.Timeout as errt:
            errorCount[index] += 1
            time.sleep(1)
            if errorCount[index]== 6:
                print(f"Timeout Error: {errt} .")
                messagebox.showerror('Timeout',f'Time Out: {errt}\nUrl: {url}')
        except requests.exceptions.RequestException as err:
            errorCount[index] += 1
            time.sleep(1)
            if errorCount[index]== 6:
                print(f"An error occurred: {err} .")
                messagebox.showerror('RequestException',f'Request Exception: {err}\nUrl: {url}')


