import nfc

def get_id():

    while True:
        try:
            reader = nfc.Reader()
            data = reader.get_uid()
            if data:
                return(data)
        except:
            pass

for i in range(3):
    print(get_id())