#!/usr/bin/python3

import multiprocessing
import threading
import os

import dns_proxy.dns_proxy_dev as DNSProxyInit
import dns_relay.dns_relay as DNSRelayInit
import dhcp_server.dhcp_server as DHCPServerInit
  
def Run():
    DNSProxy = DNSProxyInit.DNSProxy()
    DNSRelay = DNSRelayInit.DNSRelay()
    DHCPServer = DHCPServerInit.DHCPServer()
     
    threading.Thread(target=DNSProxy.Start).start()
    threading.Thread(target=DNSRelay.Start).start()
    threading.Thread(target=DHCPServer.Start).start()

if __name__ == '__main__':
    try:
        priv = os.geteuid()
        if (priv == 0):
            print(' ______   __    _  __   __    _______  _     _  _______  ___      ___     ')
            print('|      | |  |  | ||  |_|  |  |       || | _ | ||   _   ||   |    |   |    ')
            print('|  _    ||   |_| ||       |  |    ___|| || || ||  |_|  ||   |    |   |    ')
            print('| | |   ||       ||       |  |   |___ |       ||       ||   |    |   |    ')
            print('| |_|   ||  _    | |     |   |    ___||       ||       ||   |___ |   |___ ')
            print('|       || | |   ||   _   |  |   |    |   _   ||   _   ||       ||       |')
            print('|______| |_|  |__||__| |__|  |___|    |__| |__||__| |__||_______||_______|')

            Run()
        else:
            print('DNX FWALL requires Root Priveledges. Exiting...')
            exit(1)
    except Exception as E:
        print(E)
    except KeyboardInterrupt:
        print('\n-----------------------------------------------------')
        print("User Interrupt. Exiting Some Random Thing")
        print('-----------------------------------------------------')
