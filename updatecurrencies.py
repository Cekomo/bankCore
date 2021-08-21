# output can be copy paste below "#-- THE VALUES MAY NOT BE UP-TO-DATE! --#" time to time
# this is not optimal for public use but effective for updating offline mode

import json
import requests

apiURL = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=698d889676879382f142cb906f52f58b&format=1")
apiURL = json.loads(apiURL.text)

tltousd = (1 / (apiURL["rates"]['TRY'])) * (apiURL["rates"]['USD'])
usdtotl = (apiURL["rates"]['TRY']) * (1 / (apiURL["rates"]['USD']))
tltoeur = 1 / (apiURL["rates"]['TRY'])
eurtotl = apiURL["rates"]['TRY']
tltogold = (apiURL["rates"]['XAU'] * 31.1034807) * (1 / (apiURL["rates"]['TRY']))
goldtotl = (1 / (apiURL["rates"]['XAU'] * 31.1034807)) * apiURL["rates"]['TRY']
usdtoeur = 1 / (apiURL["rates"]['USD'])
eurtousd = apiURL["rates"]['USD']
goldtousd = (apiURL["rates"]['USD']) * (1 / (apiURL["rates"]['XAU'] * 31.1034807))
usdtogold = (apiURL["rates"]['XAU'] * 31.1034807) * (1 / (apiURL["rates"]['USD']))
goldtoeur = 1 / (apiURL["rates"]['XAU'] * 31.1034807)
eurtogold = apiURL["rates"]['XAU'] * 31.1034807

print("self.tltousd =", '%.5f'%tltousd)
print("self.usdtotl =", '%.5f'%usdtotl) 
print("self.tltoeur =", '%.5f'%tltoeur) 
print("self.eurtotl =", '%.5f'%eurtotl) 
print("self.tltogold =", '%.5f'%tltogold) 
print("self.goldtotl =", '%.5f'%goldtotl) 
print("self.usdtoeur =", '%.5f'%usdtoeur) 
print("self.eurtousd =", '%.5f'%eurtousd) 
print("self.goldtousd =", '%.5f'%goldtousd) 
print("self.usdtogold =", '%.5f'%usdtogold) 
print("self.goldtoeur =", '%.5f'%goldtoeur) 
print("self.eurtogold =", '%.5f'%eurtogold)


