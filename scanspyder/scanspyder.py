#!/usr/bin/env python 

import argparse
import socket
import pyfiglet
from termcolor import colored

banner = pyfiglet.figlet_format("Pyspyder", font="slant")
print(colored(banner, "red"))

print(colored("Author   : Nikhil Kumar", "green"))
print(colored("Tool     : Python Scan Tool", "yellow"))
print(colored("Version  : 1.0", "cyan"))
print(colored("Github   : github.com/N1KHIL-KUMAR", "magenta"))

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[+] Port {port} is open")
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
        exit()
    except socket.gaierror:
        print("[!] Hostname could not be resolved")
        exit()
    except socket.error:
        print("[!] Couldn't connect to server")
        exit()

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("host", help="Target host to scan (e.g. 192.168.1.1 or example.com)")
    parser.add_argument("start_port", type=int, help="Start of port range")
    parser.add_argument("end_port", type=int, help="End of port range")

    args = parser.parse_args()


    print(f"[*] Scanning {args.host} from port {args.start_port} to {args.end_port}...")

    for port in range(args.start_port, args.end_port + 1):
        scan_port(args.host, port)

if __name__ == "__main__":
    main()


