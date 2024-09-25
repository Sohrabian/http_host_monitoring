# example of pinging the status of a set of websites asynchronously
from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from http import HTTPStatus
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from colorama import Fore, Back, Style
import time
from tkinter import *
from tkinter import messagebox

# get the status of a website
def get_website_status(url):
    # handle connection errors
    try:
        # open a connection to the server with a timeout
        with urlopen(url,timeout=3) as connection:
            # get the response code, e.g. 200
            code = connection.getcode()
            return code
    except HTTPError as e:
        return e.code
    except URLError as e:
        return e.reason
    finally:
        time.sleep(10)
   
# interpret an HTTP response code into a status
def get_status(code):
    if code == HTTPStatus.OK:
        return 'OK'
    return 'ERROR'
 
# check status of a list of websites
def check_status_urls(urls):
    # create the thread pool
    with ThreadPoolExecutor(len(urls)) as executor:
        # submit each task, create a mapping of futures to urls
        future_to_url = {executor.submit(get_website_status, url):url for url in urls}
        # get results as they are available
        for future in as_completed(future_to_url):
            # get the url for the future
            url = future_to_url[future]
            # get the status for the website
            code = future.result()
            # interpret the status
            status = get_status(code)
            # report status
            if status =='ERROR':
                urlMain= ['https://flightpermission.cao.ir/','https://caa.gov.ir','https://medical.cao.ir','https://techcomit.cao.ir']
                if url in urlMain:
                    root = Tk()
                    root.withdraw()
                    messagebox.showinfo("ERROR Connection", f'{url:20s}\t{status:5s}\t{code}')                   
                print(Fore.RED+f'{url:20s}\t{status:5s}\t{code}')
            if status == 'OK':
                print(Fore.GREEN+f'{url:20s}\t{status:5s}\t{code}')
            #print(f'{url:20s}\t{status:5s}\t{code}')
            time.sleep(25)

 
# list of urls to check
URLS = ['https://pel.cao.ir',
'https://farasa.cao.ir',
'https://techcomit.cao.ir',
'https://aviation.cao.ir',
'https://uas.cao.ir',
'https://regulation.caa.gov.ir',
'https://complaint.cao.ir',
'https://tariff.cao.ir',
'https://bpms.cao.ir',
'https://billing.cao.ir',
'https://e-agency.cao.ir',
'https://aig.cao.ir',
'https://agencylist.cao.ir',
'https://voluntary.cao.ir',
'https://fleet.cao.ir',
'https://accert.cao.ir',
'https://dpequip.cao.ir',
'https://sim.cao.ir',
'https://acreg.cao.ir',
'https://acpermit.cao.ir',
'https://flightopr.cao.ir',
'https://e-agencylist.cao.ir',
'https://customs.cao.ir',
'https://caa.gov.ir',
'https://flightpermission.cao.ir',
'https://medical.cao.ir']

# check all urls

while True:
    check_status_urls(URLS) 
