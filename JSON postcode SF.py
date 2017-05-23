import json
import http.client
import urllib.request
import argparse
import platform
import sys
import time

#import usb.core
#import usb.util

FEED_PAST_CUTTER = b'\n' * 5
USB_BUSY = 66

PIPSTA_USB_VENDOR_ID = 0x0483
PIPSTA_USB_PRODUCT_ID = 0xA053


def printmain(txtprt):
    """The main loop of the application.  Wrapping the code in a function
    prevents it being executed when various tools import the code.
    """
    if platform.system() != 'Linux':
        sys.exit('This script has only been written for Linux')

    # Find the Pipsta's specific Vendor ID and Product ID
    dev = usb.core.find(idVendor=PIPSTA_USB_VENDOR_ID,
                        idProduct=PIPSTA_USB_PRODUCT_ID)
    if dev is None:  # if no such device is connected...
        raise IOError('Printer  not found')  # ...report error

    try:
        # Linux requires USB devices to be reset before configuring, may not be
        # required on other operating systems.
        dev.reset()

        # Initialisation. Passing no arguments sets the configuration to the
        # currently active configuration.
        dev.set_configuration()
    except usb.core.USBError as ex:
        raise IOError('Failed to configure the printer', ex)

    # The following steps get an 'Endpoint instance'. It uses
    # PyUSB's versatile find_descriptor functionality to claim
    # the interface and get a handle to the endpoint
    # An introduction to this (forming the basis of the code below)
    # can be found at:

    cfg = dev.get_active_configuration()  # Get a handle to the active interface

    interface_number = cfg[(0, 0)].bInterfaceNumber
    # added to silence Linux complaint about unclaimed interface, it should be
    # release automatically
    usb.util.claim_interface(dev, interface_number)
    alternate_setting = usb.control.get_interface(dev, interface_number)
    interface = usb.util.find_descriptor(
        cfg, bInterfaceNumber=interface_number,
        bAlternateSetting=alternate_setting)

    usb_endpoint = usb.util.find_descriptor(
        interface,
        custom_match=lambda e:
        usb.util.endpoint_direction(e.bEndpointAddress) ==
        usb.util.ENDPOINT_OUT
    )

    if usb_endpoint is None:  # check we have a real endpoint handle
        raise IOError("Could not find an endpoint to print to")

    # Now that the USB endpoint is open, we can start to send data to the
    # printer.
    # The following opens the text_file, by using the 'with' statemnent there is
    # no need to close the text_file manually.  This method ensures that the
    # close is called in all situation (including unhandled exceptions).
    
    txt = txtprt#"hello from the pipsta printer" #parse_arguments()
    usb_endpoint.write(b'\x1b!\x00')

    # Print a char at a time and check the printers buffer isn't full
    for x in txt:
        usb_endpoint.write(x)    # write all the data to the USB OUT endpoint
        
        res = dev.ctrl_transfer(0xC0, 0x0E, 0x020E, 0, 2)
        while res[0] == USB_BUSY:
            time.sleep(0.01)
            res = dev.ctrl_transfer(0xC0, 0x0E, 0x020E, 0, 2)
            
    usb_endpoint.write(FEED_PAST_CUTTER)
    usb.util.dispose_resources(dev)
    
def postcode(postcode):
    urlData = ''
    pcode = ''
    if len(postcode) ==0:
        urlData = 'http://api.postcodes.io/random/postcodes/'
    else:
        urlData = 'http://api.postcodes.io/postcodes/'+postcode
    
    try:
        urlrequest = urllib.request.urlopen(urlData)
        data = urlrequest.read()
        print('data:\n',data)
        js = json.loads(data.decode("utf-8"))
        print('js is type of',type(js))
        if len(postcode) ==0:
            pcode = str(js['result']['postcode'])
        else:
            pcode = postcode
        
        print('Postcode',pcode.upper(),' has')
        Long_and_Lat(str(js['result']['longitude']),str(js['result']['latitude']),pcode)
        print('is in the country of:',str(js['result']['country']))
        
    except urllib.request.HTTPError as httpE:
        print(httpE.code)
        print('#'*30+'\nERROR')
        print('Could not find postcode '+postcode.upper()+' \ncheck it is a valid postcode\n')
    

def TFL():
    urlData = 'https://api.tfl.gov.uk/Line/victoria/Disruption?app_id=&app_key='
    urlrequest = urllib.request.urlopen(urlData)
    data = urlrequest.read()
    print(data)

def Long_and_Lat(Lg, Lt,pcode=''):
    Long=Lg
    Lat=Lt
    urlData = 'http://api.sunrise-sunset.org/json?lat='+Lat+'&lng='+Long

    try:
        urlrequest = urllib.request.urlopen(urlData)
        data = urlrequest.read()
        js = json.loads(data.decode("utf-8"))
        msg= '#'*30+'\n'
        if len(pcode) > 0:
            msg += 'Postcode: '+ pcode.upper() +'\n'
        msg += 'Longitude:'+ Long + '\nand latitude:' + Lat +'\n'
        msg += 'Has sunrise:'+js['results']['sunrise']+' \nand sunset:'+js['results']['sunset'] +'\n'
        msg += '\n'*5
        msg += '#'*30

        print('Postcode:',pcode,'\n')
        print('Longitude:', Long,'and latitude', Lat)
        print('Has sunrise:',js['results']['sunrise'],' and sunset:',js['results']['sunset'])
        printmain(msg)
        
    except  urllib.request.HTTPError:
            print('Could not find sunrise & sunset times for longitude'+Long+' and latitude'+Lat)
    

def menu():
    print('*'*29)
    print('*'*10+' Welcome '+'*'*10)
    print('*'*29)

    print('You can enter a postcode or longitude & latitude')
    print('and the program will return the sunrise & sunset \ntimes for that location')
    print('')
    print('The program uses a web service to \'calculate\' the \nlongitude & latitude from a postcode')
    print('Once the longitude & latitude are know \nit uses another webservice to find the sunrise & sunsets time')
    print()
    print('Make your choice below')
    print('Postcodes enter P')
    print('Longitude & Latitude enter L')
    print('random postcode R')

'''
while True:
    menu()
    choice = input('\nPlease enter your choice L or P or R: ')
    if choice.upper() == 'R':
        pcode= ''
        print('checking web service.....')
        postcode(pcode)
    elif choice.upper() == 'P':
        pcode= input(str("Please enter your postcode: "))
        print('checking web service.....')
        postcode(pcode)
    elif choice.upper() == 'L':
        lg =input('Please enter the longitude: ')
        lt =input('Please enter the latitude: ')
        Long_and_Lat(lg,lt)
'''
TFL()

