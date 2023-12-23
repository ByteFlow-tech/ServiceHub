import asyncio
import multiprocessing
import sys
from threading import Thread
from multiprocessing import Event, Process
import anyio
import time

# import click
import asyncclick as click
from art import text2art
from tqdm import tqdm

from Core.Exceptions import AuthException, Stop
from LocalStorageService.StorageInteraction import StorageInteraction
from LocalStorageService.Models import create_all
from Server.ServerInitialization import websocket_server_initialization


@click.group()
def cli():
    pass


def echo(msg: str):
    click.echo(f"srvh:> " + msg)


def prompt(placeholder: str):
    click.prompt(f"srvh:>" + placeholder)


@cli.command()
@click.argument("target")
@click.option("-pn", "--pool_name")
@click.option("-u", "--username")
@click.option("-p", "--password")
async def create(target=None, pool_name=None, username=None, password=None):
    click.clear()
    try:
        match target:
            case "pool":
                if pool_name is None:
                    echo("Enter pool name")
                    pool_name = input("srvh:> ")
                    print(pool_name)
                else:
                    print(pool_name)
            case "user":
                if username is None:
                    echo("Enter username")
                    username = input("srvh:> ")
                if password is None:
                    echo("Enter password")
                    password = input("srvh:> ")
                else:
                    print(username, password)
    except Exception:
        pass


def run_server(port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(websocket_server_initialization(port))


def run_console():
    try:
        while True:
            command = input("srvh:> ")
            print(command)
    except KeyboardInterrupt:
        pass


@cli.command()
@click.argument("server")
@click.option("-p", "--port", help="The WS server port")
async def run(server, port: int = None):
    click.clear()
    head = text2art("ServiceHUB v0.1", font="starwars")
    print(head)
    server_process = Process(target=run_server, args=(port, ))
    server_process.start()

    console_process = Process(target=run_console)
    console_process.start()

    try:
        server_process.join()
        server_process.join()
    except KeyboardInterrupt:
        server_process.terminate()
        console_process.terminate()

if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    cli()
