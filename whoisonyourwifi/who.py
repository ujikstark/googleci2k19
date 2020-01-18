## Created By Ujikstark

#!/usr/bin/env python3
import scapy.all as sc
import socket
from termcolor import colored

ip = input("IP : ")
strip = '-'*73
count_line = 0 

def scan():
    global count_line
    ip_packet = sc.ARP(pdst=ip+'/24')
    mac = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = mac/ip_packet
    result = sc.srp(packet, timeout=1, verbose=False)[0]
    result_scrape = []
    
    for i in result[0]:
        data = {"ip": i[1].psrc,
                "mac": i[1].hwsrc}
                
        result_scrape.append(data)
                
    for x in result:
        data = {"ip": x[1].psrc,
                "mac":x[1].hwsrc}
                      
        result_scrape.append(data)
                     
    print(colored(f'{strip}\nHost Name\t\tIP\t\t\t\tMAC\n{strip}', "green"))
    
    del(result_scrape[1])
    del(result_scrape[1])
    for x in result_scrape:
        count_line += 1 
        get_host = socket.getfqdn(x["ip"])            
        print(colored(f'{get_host}\t\t{x["ip"]}\t\t\t{x["mac"]}\n{strip}',"green"))    
    print(colored(f'{count_line} Device Connected',"blue"))     
        

if __name__ == "__main__":        
    scan()
        
        

