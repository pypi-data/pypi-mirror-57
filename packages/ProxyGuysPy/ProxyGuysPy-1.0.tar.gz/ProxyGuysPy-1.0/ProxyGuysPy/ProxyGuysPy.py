import requests
import json

class ProxyGuysAPI:
	def __init__(self, username, password):
		self.API_URL = 'https://portal.proxyguys.com/api/v2/proxies/'
		self.LOGIN_URL = 'https://portal.proxyguys.com/login'
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Sec-Fetch-User': '?1'
		}
		self.loggedIn = False
		self.username = username
		self.password = password
		self.sess = requests.Session()

	def login(self):
		data = f'username={self.username}&password={self.password}'
		resp = self.sess.post(self.LOGIN_URL, headers=self.headers, data=data, verify=False)
		if resp.status_code != 200:
			return False
		else:
			if resp.url == 'https://portal.proxyguys.com/login':
				return False
			self.loggedIn = True
			return True

	def get_available_proxies(self):
		resp = self.api_request('list')
		if resp == None:
			return json.dumps({'error': 'not logged in'})
		return resp['result']

	def get_proxy_site_availability(self):
		resp = self.api_request('availability')
		if resp == None:
			return json.dumps({'error': 'not logged in'})
		return resp['result']

	def connect_proxy(self, proxyUuid, location):
		resp = self.api_request('connect', f'{proxyUuid}/{location}')
		if resp == None:
			return json.dumps({'error': 'not logged in'})
		return resp['result']

	def disconnect_proxy(self, proxyUuid):
		resp = self.api_request('disconnect', proxyUuid)
		if resp == None:
			return json.dumps({'error': 'not logged in'})
		return resp['result']

	def hard_reset(self, proxyUuid):
		resp = self.api_request('hard_reset', proxyUuid)
		if resp == None:
			return json.dumps({'error': 'not logged in'})
		return resp['result']

	def fast_ip_change(self, proxyUuid):
		resp = self.api_request('reset', proxyUuid)
		if resp == None:
			return json.dumps({'error': 'not logged in'})
		return resp['result']

	def toggle_whitelist(self, proxyUuid, enable):
		param = 'enablewhitelist' if enable else 'disablewhitelist'
		resp = self.api_request(param, proxyUuid)
		if resp == None:
			return json.dumps({'error': 'not logged in'})
		return resp['result']

	def set_whitelist_ip(self, proxyUuid, cidr_ip):
		resp = self.api_request('ipwhitelist', f'{proxyUuid}/{cidr_ip}')
		if resp == None:
			return json.dumps({'error': 'not logged in'})
		return resp['result']

	def api_request(self, url, data=None):
		if not self.loggedIn:
			return None
		resp = None
		if data == None:
			resp = self.sess.get(self.API_URL + url, headers=self.headers, verify=False)
		else:
			resp = self.sess.get(self.API_URL + url + '/' + data, headers=self.headers, verify=False)
		if resp.status_code != 200:
			return None
		else:
			return resp.json()