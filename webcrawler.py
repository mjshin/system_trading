

import ystockquote
import operator

from datetime import date, timedelta


yesterday = date.today() - timedelta(1)

yesterday = '2016-' + yesterday.strftime('%m-%d')
print(yesterday)

price_history = ystockquote.get_historical_prices('006400.KS', '2015-01-01', yesterday)

#sorted_price_history = sorted(price_history.items(), key=operator.itemgetter(1))


#print(price_history)


#for key in price_history:
#    print "key : %s , value : %s " % (key, price_history[key])

sorted_keys = sorted(price_history.keys())

for key in sorted_keys:
    print "Date : " + key
    print price_history[key]

#print("Volume : " + price_history[0][''])
#print("Volume : " + price_history[0]['Volume'])