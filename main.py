import time

# import click
import asyncclick as click
from art import text2art
from tqdm import tqdm

from Core.Exceptions import AuthException
from Server.LocalStorageService import StorageInteraction
from Server.LocalStorageService import create_all
from Server.ServerInitialization import websocket_server_initialization
from logger import err

global DEFAULT_USER
DEFAULT_USER = "srvh"


@click.group()
def cli():
    pass


def echo(msg: str, current_user: str = DEFAULT_USER):
    click.echo(f"{current_user}:>.." + msg)


def prompt(placeholder: str, current_user: str = DEFAULT_USER):
    click.prompt(f"{current_user}:>.." + placeholder)


@cli.command()
# @click.argument("server")
async def start():
    click.clear()
    click.echo(text2art("ServiceHUB", font="starwars"))
    create_db_file = open("Server/LocalStorageService/LocalStorage/storage.db", "a+")
    create_all()
    for _ in tqdm(range(1324), ascii=True, desc="Initializing components"):
        time.sleep(0.0001)
    storage = StorageInteraction()
    user = storage.existed_users()
    if user is None:
        echo("No users found")
        echo("Please use 'srvh user add' to add user")
    else:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            user = storage.check_user(password)
            echo("Welcome back", user)
            await websocket_server_initialization()
        except AuthException as e:
            err(e)
            echo("Invalid username or password")


if __name__ == '__main__':
    cli()

# async def init():
#     head = text2art("ServiceHUB", font="starwars")
#     print(head)
#     # for _ in tqdm(range(1324), ascii=True, desc="Initializing components"):
#     #     await asyncio.sleep(0.001)
#     create_db_file = open("LocalStorageService/LocalStorage/storage.db", "a+")
#     create_all()
#
# async def server_loop():
#     while True:
#         await websocket_server_initialization()
#         await asyncio.sleep(1)
#
# def user_interaction(storage):
#     while True:
#         if storage.existed_users() is None:
#             log("serviceH:> Users not found. Need to create a new user.")
#             time.sleep(1)
#             username = input("root:> Enter username: ")
#             password = input("root:> Enter password: ")
#             privilege = input(f"root:> Make user {username} root user. (Y/N) ")
#             match privilege.lower():
#                 case "y":
#                     new_user = storage.create_user(username, password, True)
#                 case "n":
#                     new_user = storage.create_user(username, password, False)
#                 case _:
#                     err("Undefined command")
#                     continue
#
#             log(f"serviceH:> Your auth-key: {new_user} \n You must use it for connecting your services")
#             time.sleep(1)
#             continue
#         else:
#             while True:
#                 current_user = storage.root_user()
#                 if current_user is None:
#                     current_user = "root"
#                 CommandHandler.command_handler(input(f"{current_user}:> "))
#
# def run_server():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(server_loop())
#
# def run_user_interaction(storage):
#     user_interaction(storage)
#
# if __name__ == '__main__':
#     # Инициализация ресурсов
#     storage = StorageInteraction()
#     init_thread = threading.Thread(target=lambda: asyncio.run(init()))
#
#     # Запуск потока инициализации
#     init_thread.start()
#     init_thread.join()  # Ждем завершения инициализации перед запуском остального
#
#     # Запуск двух потоков: сервера и взаимодействия с пользователем
#     server_thread = threading.Thread(target=run_server)
#     user_interaction_thread = threading.Thread(target=run_user_interaction, args=(storage,))
#
#     # Запускаем потоки
#     server_thread.start()
#     user_interaction_thread.start()
#
#     # Ожидаем завершения работы потоков
#     server_thread.join()
#     user_interaction_thread.join()
