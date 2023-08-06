Python API for ProxyGuys


How to import:
from ProxyGuysPy import ProxyGuysAPI

How to use:

#initalize the class
api = ProxyGuysAPI('USERNAME', 'PASSWORD')

#login
api.login() #returns True or False

#functions
api.get_available_proxies()
api.get_proxy_site_availability()
api.connect_proxy(proxyUuid, location)
api.disconnect_proxy(proxyUuid)
api.hard_reset(proxyUuid)
api.fast_ip_change(proxyUuid)
api.toggle_whitelist(proxyUuid, True/False)
api.set_whitelist_ip(proxyUuid, 'IP_ADDRESS')

#all functions return a json object