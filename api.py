import json
uid = input("API MOZ Anda: ")
passwd = input("API Secret MOZ Anda: ")
try:
    x = open("config.json").read()
    x = json.loads(x)
    x['id'].append(uid)
    x['pass'].append(passwd)
    x['creditsused'].append('0')
    with open("config.json", "w+") as f:
            x = str(x)
            x = x.replace("'", "\"")
            f.write(x)
            f.close()
    print("Berhasil menambahkan API keys ke dalam list." + "\n" + "\n" + uid + "\n" + "\n"+ passwd + "\n")
except FileNotFoundError:
    print("Error encountered! Please check if config.json file exists.")


