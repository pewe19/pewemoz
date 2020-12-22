import json
print("PeweMoz V.1.1")
print("Gunakan API MOZ Anda Sendiri!!")
print("  ")
print("    ____                   __  __")
print("   |  _ \ _____      _____|  \/  | ___ ____")
print("   | |_) / _ \ \ /\ / / _ \ |\/| |/ _ \_  /")
print("   |  __/  __/\ V  V /  __/ |  | | (_) / /")
print("   |_|   \___| \_/\_/ \___|_|  |_|\___/___|")
print("  ")
print("  ")
uid = input("API MOZ Anda: ")
passwd = input("API Secret MOZ Anda: ")
print("  ")
print("  ")
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
    print("Error mas/mbak bro! cek coba di folder ada file config.json ndak? ")


#EOF inputAPI.py PeweMoz V.1.1
