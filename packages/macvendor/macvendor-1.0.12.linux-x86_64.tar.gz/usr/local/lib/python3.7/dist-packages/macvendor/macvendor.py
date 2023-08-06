import argparse
import sys
import re
import os

PATH = os.path.dirname(os.path.realpath(__file__))
VERSION = "1.0.12"

#check if the MAC address is in a correct form return True if it is correct, else returns False
def checkMacAddr(addr):
    regexList = {   
                re.compile(r"^([0-9a-f][0-9a-f]:){3}(ff:fe:)?([0-9a-f][0-9a-f]:){2}([0-9a-f][0-9a-f])$", re.IGNORECASE),
                re.compile(r"^([0-9a-f][0-9a-f]-){3}(ff-fe-)?([0-9a-f][0-9a-f]-){2}([0-9a-f][0-9a-f])$", re.IGNORECASE),
                re.compile(r"^([0-9a-f][0-9a-f]\.){3}(ff\.fe\.)?([0-9a-f][0-9a-f]\.){2}([0-9a-f][0-9a-f])$", re.IGNORECASE),
                re.compile(r"^([0-9a-f][0-9a-f]){3}(fffe)?([0-9a-f][0-9a-f]){2}([0-9a-f][0-9a-f])$", re.IGNORECASE),
                re.compile(r"^([0-9a-f][0-9a-f][0-9a-f]:){3}([0-9a-f][0-9a-f][0-9a-f])$", re.IGNORECASE),
                re.compile(r"^([0-9a-f][0-9a-f][0-9a-f]\.){3}([0-9a-f][0-9a-f][0-9a-f])$", re.IGNORECASE),
                re.compile(r"^([0-9a-f][0-9a-f][0-9a-f]-){3}([0-9a-f][0-9a-f][0-9a-f])$",re.IGNORECASE),
                re.compile(r"^([0-9a-f][0-9a-f][0-9a-f][0-9a-f]:)([0-9a-f][0-9a-f]ff:)(fe[0-9a-f][0-9a-f]:)([0-9a-f][0-9a-f][0-9a-f][0-9a-f])$", re.IGNORECASE),
                re.compile(r"^([0-9a-f][0-9a-f][0-9a-f][0-9a-f]\.)([0-9a-f][0-9a-f]ff\.)(fe[0-9a-f][0-9a-f]\.)([0-9a-f][0-9a-f][0-9a-f][0-9a-f])$", re.IGNORECASE),
                re.compile(r"^([0-9a-f][0-9a-f][0-9a-f][0-9a-f]-)([0-9a-f][0-9a-f]ff-)(fe[0-9a-f][0-9a-f]-)([0-9a-f][0-9a-f][0-9a-f][0-9a-f])$", re.IGNORECASE)
                }
    for regex in regexList:
        if re.match(regex, addr) is not None:
            return True
    return False

#Like checkMacAddr but for OUI
def checkOUI(oui):
    regexList = {
        re.compile(r"^([0-9a-f][0-9a-f]:){2}([0-9a-f][0-9a-f])$", re.IGNORECASE),
        re.compile(r"^([0-9a-f][0-9a-f]\.){2}([0-9a-f][0-9a-f])$", re.IGNORECASE),
        re.compile(r"^([0-9a-f][0-9a-f]-){2}([0-9a-f][0-9a-f])$", re.IGNORECASE),
        re.compile(r"^([0-9a-f]){6}$", re.IGNORECASE),
    }
    for regex in regexList:
        if re.match(regex, oui) is not None:
            return True
    return False

#remove ":", "-", "." from the address
def cleanAddr(addr):
    for ch in {":", "-", "."}:
        if ch in addr:
            addr = addr.replace(ch, "")
    return addr.upper()

#Take a MAC address and returns the OUI, it can return longer value depending on the prefix
def macToOui(addr,prefix):
    return cleanAddr(addr)[0:prefix]

#Parse a line from a list and get the vendor name only
def getVendorFromFile(line):
    return line.split("\t")[1].replace("\n", "")

#Search for the address in the lists and print the vendor
def lookup(addr, file, prefix = 6):
    oui = macToOui(addr,prefix)
    test = [addr, ""]
    with open(file, "r") as db:
        for line in db:
            if oui in line:
                if "IEEE Registration Authority" in line: #if the line includes "IEEE Registration Authority" there is a chance the vendor is in prefix28 or prefix36 files
                    test[1] += getVendorFromFile(line)
                    if (cleanAddr(addr)[6:10] == "FFFE") and (len(cleanAddr(addr)) == 16):
                        addr = cleanAddr(addr)[0:6] + cleanAddr(addr)[10:] #Fix Problem with EUI-64 in the next two lines
                    prefix24 = lookup(addr, "{}/data/prefix28".format(PATH),7) or ""
                    prefix28 = lookup(addr, "{}/data/prefix36".format(PATH), 9) or ""
                    test[1] += " - {} {}".format(prefix24[1], prefix28[1])
                else:
                    test[1] += getVendorFromFile(line)
    return test

#Takes a list/tuple of MAC address/OUI and returns
def getVendorList(plist):
    result = {}
    if (type(plist) is list) or (type(plist) is tuple):
        for addr in plist:
            if checkMacAddr(addr) or checkOUI(addr):
                lookupData = lookup(addr, "{}/data/prefix24".format(PATH))
                result[lookupData[0]] = lookupData[1]
            else:
                result[addr] = "Invalide MAC or OUI format"
    else:
        raise Exception("argument for getvendorList() should be a list or a tuple")
    return result

def getVendor(p):
    if checkMacAddr(p) or checkOUI(p):
        return lookup(p, "./data/prefix24")
    else:
        return [p, "Invalide Mac or OUI format"]

def formatTable(d):
    from tabulate import tabulate
    headers = ['Mac', 'Vendor']
    data = [(k,v) for k,v in d.items()]
    return tabulate(data, headers=headers, tablefmt="github")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="Displays version information.", action="store_true")
    parser.add_argument("address", metavar="address", type=str, nargs="*", help="one or multiple valide MAC address or OUI to lookup")
    args = parser.parse_args()
    if args.address:    
        print(formatTable(getVendorList(args.address)))
    if args.version:
        print("verion {}".format(VERSION))

if  __name__ == "__main__":
    main()