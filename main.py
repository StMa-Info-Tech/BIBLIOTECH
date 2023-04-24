import nfc
from time import sleep

def get_id():

    while True:
        try:
            reader = nfc.Reader()
            data=reader.get_uid()
            if data:
                return(data)
        except:
            pass

for i in range(100):
    print(get_id())
    sleep(2)