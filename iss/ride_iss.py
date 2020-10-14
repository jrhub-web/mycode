#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

import urllib.request
import json

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
        
    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)
    
    ## put fileobject into helmet
    helmet = groundctrl.read()
    
    ## decode JSON to Python data structure
    helmetson = json.loads(helmet.decode('utf-8'))
    j2 = helmetson['people']
    #n = j2['name']
    #c = j2['craft']
    for key  in helmetson['people']:
    ## display our Pythonic data
       # value = j2[key]
        print(key['name'], " on the ", key['craft'])
    #print(helmetson)
    
    #print('\n\nPeople in Space: ', helmetson['number'])
    #people = helmetson['people']
    #print(people)
main() 
    
 


