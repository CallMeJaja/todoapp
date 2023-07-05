from tabulate import tabulate
import os, time

# Color Code
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
NORMAL = "\033[0m"

os.system("cls||clear")
print(f"""\
 _______         _    __  __      
|__   __|       | |  |  \/  |     
    | | __ _ ___| | _| \  / | ___ 
    | |/ _` / __| |/ / |\/| |/ _ \\
    | | (_| \__ \   <| |  | |  __/
    |_|\__,_|___/_|\_\_|  |_|\___|
{RED}----------------------------------
{GREEN}        Buat Daftar Tugas Mu
{RED}----------------------------------

""")
data = []

def showMenu():
    time.sleep(.3)
    # Membuat data
    print(f"{ITALIC}{LIGHT_WHITE}           Menu")
    data = [
        ['1','Daftat Tugas'],
        ['2','Tambah Tugas Baru'],
        ['3','Hapus Tugas'],
        ['4','Exit']
        ]
 
    header = ['No.', 'Daftar Menu']

    print(NORMAL + tabulate(data, headers=header, tablefmt="rounded_grid", numalign="left"))
    menu = int(input("Pilihan: [1/2/3/4]: "))
    match menu:
        case 1:
            taskList()
        case 2:
            addTask()
        case 3:
            delTask()
        case 4:
            exit()    
def taskList():
    header = ['No','Tugas']
    print(NORMAL + "\n" + tabulate(data,headers=header, tablefmt="rounded_grid", numalign="left"))
    showMenu()

def addTask():
    os.system("cls||clear")
    task = input("Masukkan Nama Tugas : ")
    data.append([str(len(data) + 1), task])
    time.sleep(.3)
    print("Tugas berhasil ditambahkan!")
    time.sleep(1)
    print("")
    taskList()

def delTask():
    header = ['No','Tugas']
    print(NORMAL + "\n" + tabulate(data,headers=header, tablefmt="rounded_grid", numalign="left"))
    print("")
    task = int(input("Mau hapus tugas yang mana ? [ex:1] : "))
    if task <= len(data):
        deleted = data.pop(task - 1)
        print(f"Tugas {deleted} berhasil dihapus!")
    else:
        print("Tugas tidak ditemukan")
    time.sleep(.5)
    print("")
    taskList()
showMenu()

