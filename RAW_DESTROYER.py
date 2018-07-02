import os
import os.path
cwd = os.getcwd()

print("""
 ██▀███   ▄▄▄       █     █░   ▓█████▄ ▓█████   ██████ ▄▄▄█████▓ ██▀███   ▒█████ ▓██   ██▓▓█████  ██▀███  
▓██ ▒ ██▒▒████▄    ▓█░ █ ░█░   ▒██▀ ██▌▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒▒██  ██▒▓█   ▀ ▓██ ▒ ██▒
▓██ ░▄█ ▒▒██  ▀█▄  ▒█░ █ ░█    ░██   █▌▒███   ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒ ▒██ ██░▒███   ▓██ ░▄█ ▒
▒██▀▀█▄  ░██▄▄▄▄██ ░█░ █ ░█    ░▓█▄   ▌▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░ ░ ▐██▓░▒▓█  ▄ ▒██▀▀█▄  
░██▓ ▒██▒ ▓█   ▓██▒░░██▒██▓    ░▒████▓ ░▒████▒▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░ ░ ██▒▓░░▒████▒░██▓ ▒██▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▓░▒ ▒      ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░   ██▒▒▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░▒ ░ ▒░  ▒   ▒▒ ░  ▒ ░ ░      ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ ▓██ ░▒░  ░ ░  ░  ░▒ ░ ▒░
  ░░   ░   ░   ▒     ░   ░      ░ ░  ░    ░   ░  ░  ░    ░        ░░   ░ ░ ░ ░ ▒  ▒ ▒ ░░     ░     ░░   ░ 
   ░           ░  ░    ░          ░       ░  ░      ░              ░         ░ ░  ░ ░        ░  ░   ░     
                                ░                                                 ░ ░                     

USE JPG FILES TO PREVIEW AND DELETE USELESS PICTURES, I WILL DELETE ALL RAW FILES THAT DID NOT HAVE A JPG COUPLE.

Do you want to perform action in the current directory? (Y/N)
Currently: %s
""" % cwd)

def destroy(dir):
    files = os.listdir(dir)
    cont = 0
    for temp in files:
        if (temp.lower().endswith(('.rw2'))):
            newdir = dir+'/'+temp.replace(".RW2", ".jpg")
            if (os.path.exists(newdir)):
                print(temp.replace(".RW2", ".JPG") + ' exists, skipping file ('+ str(cont) +'/'+ str(len(files))+')')
            else:
                print(temp.replace(".RW2", ".JPG") + ' doesn\'t exist, deleting file ('+ str(cont) +'/'+ str(len(files))+')')
                os.remove(dir+'/'+temp)
        cont += 1

    print('\n \nProcess Ended! Files were deleted! }:-)')
        

res  = input().upper()

if res == "Y":
    destroy(os.getcwd())
else:
    destroy(input("\nWhere do you want to DESTROY? "))

