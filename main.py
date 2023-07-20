import getopt
import sys
import datetime as dt
import xml.etree.ElementTree as et
import requests

#2022-10-08 ===> 08/10/2022
def parseDate(date):
    try:
        pre_date = dt.datetime.strptime(date, '%Y-%m-%d')
        pre_date = pre_date.strftime('%d/%m/%Y')
        #print(pre_date)
        return pre_date
    except:
        return ("Date is not correct")


# https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002
#curency_rates --code=USD --date=2022-10-08


argv = sys.argv[1:]

code = ""
date = ""

try:
    options, args = getopt.getopt(argv, "", ["code=","date="])
except:
    print("Arguments error")

for name, value in options:
    if name in '--code':
        code = value
    elif name in ['-d', '--date']:
        date = value

if not code or not date:
    print("Not enouth args (--date or --code)")
    exit()

#print("code : " + str(code))
#print("date :" + str(date))



#PREPARE GET REQUEST
get_request_str = str('https://www.cbr.ru/scripts/XML_daily.asp?date_req=' + str(parseDate(date)))
#print(get_request_str)
data = requests.get(get_request_str)


#PARSE XML TEXT
doc = et.fromstring(data.text)

#FIND ELEMENT IN XML
for i in doc.iter('Valute'):
    if i.find('CharCode').text == str(code):
        print(i[1].text + str(" (") + i[3].text + "): " + i[4].text)