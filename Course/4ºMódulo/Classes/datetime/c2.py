'''
datetime.now()
datetime.fromtimestamp (Unix Timestamp)
Timezone diferente (pytz)
'''
from datetime import datetime
from pytz import timezone

data = datetime.now()
print(
    data.timestamp(),                   # Isso está na base de dados
    datetime.fromtimestamp(1670849077), sep=' | '
    )

# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))