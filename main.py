import getpass
import random
import time

from art import text2art, tprint
from tqdm import tqdm

from logger import logging, log, err
from CommandHeandler import CommandHandler
from LocalStorageService.Models import create_all
from LocalStorageService.StorageInteraction import StorageInteraction

current_user: str = "root"


def init():
    head = text2art("ServiceHUB", font="starwars")
    print(head)
    # for i in tqdm(range(1324), ascii=True, desc="Initializing components"):
    #     time.sleep(0.001)
    #     pass
    create_db_file = open("LocalStorageService/LocalStorage/storage.db", "a+")
    create_all()


if __name__ == '__main__':
    init()
    storage = StorageInteraction()
    while True:
        if storage.existed_users() is None:
            log("serviceH:> Users not found. Need create new user.")
            time.sleep(1)
            username = input("root:> Enter username: ")
            current_user = username
            password = input("root:> Enter password: ")
            privilege = input(f"root:> Make user {username} root user. (Y/N) ")
            match privilege.lower():
                case "y":
                    new_user = storage.create_user(username, password, True)
                case "n":
                    new_user = storage.create_user(username, password, False)
                case _:
                    err("Undefined command")
                    continue

            log(f"serviceH:> Your auth-key: {new_user} \n You must use it for connection your services")
            time.sleep(1)
            continue
        else:
            while True:
                current_user = storage.root_user()
                if current_user is None:
                    current_user = "root"
                CommandHandler.command_handler(input(f"{current_user}:> "))
