#Write a Python program to call an external command.
import subprocess

def main():
    subprocess.call('ping 8.8.8.8')
main()
