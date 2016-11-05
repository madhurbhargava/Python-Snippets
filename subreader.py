import os
import urllib2

print("Reading File")
open('workingurls.txt', 'w').close()
with open("output.txt") as f:
    for url in f:
        url = url.strip()
        print("Checking: http://"+url)
        try:
            code = urllib2.urlopen("http://"+url, timeout=5).getcode()
            if code >= 200 & code < 400:
                print(code)
                with open("workingurls.txt", "a") as myfile:
                    myfile.write(url+"\n")
        except Exception as e:
            print(url+" not working")
