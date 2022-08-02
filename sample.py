import datetime
import time
from pyzabbix import ZabbixAPI
import pandas as pd

# Network, Account
zabbix_server = 'http://zabbix-host/zabbix'
zabbix_user = "*****"
zabbix_password = "*****"

# Local time
timefrom = "YYYY-MM-DD hh:mm:ss" # time from
timetill = "YYYY-MM-DD hh:mm:ss" # time till

# Local time -> Unix time
timefrom_unix = int(time.mktime(datetime.datetime.strptime(timefrom, "%Y-%m-%d %H:%M:%S").timetuple()))
timetill_unix = int(time.mktime(datetime.datetime.strptime(timetill, "%Y-%m-%d %H:%M:%S").timetuple()))

# Get token
z = ZabbixAPI(zabbix_server, user=zabbix_user, password=zabbix_password)

# Get resource trend on server
trend = z.trend.get(
    itemids="xxxxx",
    sortfield="clock",
    sortorder="ASC",
    time_from=timefrom_unix,
    time_till=timetill_unix,
    output=["clock", "value_avg"]
    )

# Store the trend data in pandas dataframe
trend_data = pd.DataFrame(trend)
trend_data['clock'] = pd.to_datetime(trend_data['clock'], unit='s') # Unixtime -> Datetime
trend_data['value_avg'] = trend_data['value_avg'].astype(int)

# Print CSV data
trend_csv = pd.DataFrame.to_csv(trend_data, columns=["clock", "value_avg"], index=True)
print(trend_csv)