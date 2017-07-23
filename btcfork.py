import os
import time
import requests
import urllib2
from datetime import datetime
from bs4 import BeautifulSoup
url='http://www.btcforkmonitor.info/'
fetchInterval=5 #Fetches btcrforkmointor site interval
def fetch():
        try:
                        print str(datetime.now())
                        page=requests.get(url)
                        soup=BeautifulSoup(page.content,'html.parser')
                        mydivs = soup.findAll("div", { "class" : "alert alert-success mt-4 mx-2" })
                        if not 'NO CHAIN SPLIT DETECTED' in str(mydivs):
                                beep = lambda x: os.system("echo -n '\a';sleep 0.5;" * x)
                                print mydivs
                                print "Chain split. Confirm on http://www.btcforkmonitor.info/"
				while(True):
					beep(1)
					time.sleep(2)
                        else:
                                print 'No Chain splitted'

        except Exception, e:
                print e             
while(1==1):
        fetch()
        time.sleep(fetchInterval)
