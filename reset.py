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
answer = input("Anda ingin reset API keys data Anda ? Input ya or tidak: ") 
if answer == "ya": 
    file1 = open("config.json","w") 
    L = ["{\"id\": [""], \"pass\": [""], \"creditsused\": [""]}"]
    file1.writelines(L) 
    file1.close()
    print("  ")
    print("  ")
    print("API Keys sudah di reset mas/mbak bro!!")
    print("  ")
    print("  ")
    watxt = input("Sekalian gak mau hapus file daleman list URLs txt nya? Input ya or tidak: ")
    if watxt == "ya":
        file2 = open("urls.txt","w")
        btxt = []
        file2.writelines(btxt) 
        file2.close()
        print("  ")
        print("  ")
        print("List URLs udin di kosongin mas/mbak bro")
        print("  ")
        print("  ")
elif answer == "tidak": 
    print("oke gak jadi ye..")
else: 
    print("Inputnya ya atau tidak, jangan yang lain.")
    
#EOF reset.py PeweMoz V.1.1
