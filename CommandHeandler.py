import os
import time

from tqdm import tqdm

from logger import logging, log


class CommandHandler:

    @classmethod
    def command_handler(cls, command: str):
        prompt = command.lower().split()
        match prompt[0]:
            case "crt":
                print("Start creating new connection pool: ")
                pool_name = input("Enter pool name: ")
                for i in tqdm(range(1000), desc=f"Creating pool {pool_name}"):
                    time.sleep(0.01)
            case "help" | "-H":
                print("serviceH:> Commands")

