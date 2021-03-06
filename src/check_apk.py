/*
 * Copyright 2015 Dimitrios Mitropoulos
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 */

import simplejson
import urllib
import urllib2
import csv
import time
import sys

antiviruses = [
	'Bkav',
	'MicroWorld-eScan',
	'nProtect',
	'CMC',
	'CAT-QuickHeal',
	'McAfee',
	'Malwarebytes',
	'VIPRE',
	'AegisLab',
	'TheHacker',
	'K7GW',
	'K7AntiVirus',
	'NANO-Antivirus',
	'F-Prot',
	'Symantec',
	'Norman',
	'TotalDefense',
	'TrendMicro-HouseCall',
	'Avast',
	'ClamAV',
	'Kaspersky',
	'BitDefender',
	'Agnitum',
	'SUPERAntiSpyware',
	'ByteHero',
	'Rising',
	'Ad-Aware',
	'Emsisoft',
	'Comodo',
	'F-Secure',
	'DrWeb',
	'Zillya',
	'TrendMicro',
	'McAfee-GW-Edition',
	'Sophos',
	'Cyren',
	'Jiangmin',
	'Avira',
	'Antiy-AVL',
	'Kingsoft',
	'Microsoft',
	'ViRobot',
	'GData',
	'AhnLab-V3',
	'VBA32',
	'AVware',
	'Panda',
	'Zoner',
	'ESET-NOD32',
	'Tencent',
	'Ikarus',
	'Fortinet',
	'AVG',
	'Baidu-International',
	'Qihoo-360'
]

counter = 0
suspicious = False
url = "https://www.virustotal.com/vtapi/v2/file/report"

f = open('md5sums.csv')
try:
    reader = csv.reader(f)
    for row in reader:
    	if str(sys.argv[1]) == row[0]:
    		parameters = {"resource": row[1], "apikey": sys.argv[2]}
    		data = urllib.urlencode(parameters)
    		req = urllib2.Request(url, data)
    		response = urllib2.urlopen(req)
    		json = response.read()
    		response_dict = simplejson.loads(json)

    		for i in range(0, len(antiviruses)):
    			if response_dict.get("scans", {}).get(antiviruses[i], {}).get("detected") == True:
    				counter += 1
    				suspicious = True
    				print 'Antivirus:', antiviruses[i], '| Result:', response_dict.get("scans", {}).get(antiviruses[i], {}).get("result")
    		if suspicious == True:
    			print 'Total number of antiviruses: ', counter
    			break
finally:
    f.close()


