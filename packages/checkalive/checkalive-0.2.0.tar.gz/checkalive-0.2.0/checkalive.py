# -*- coding: utf-8 -*-
from __future__ import print_function
import six
import os
import re
import subprocess
from io import open
import ipaddress
import socket
import click
import psutil


def get_self_pids():
    if os.name == "nt" and __name__ != "__main__":
        return [os.getpid(), os.getppid()]
    else:
        return [os.getpid()]

def get_cmdline_or_name(p):
    try:
        return p.cmdline()
    except psutil.AccessDenied:
        return [p.name()]

def get_ip(ip):
    if isinstance(ip, (ipaddress.IPv4Address,  ipaddress.IPv6Address)):
        return ip
    if isinstance(ip, int):
        return ipaddress.IPv4Address(ip)
    ip = six.ensure_text(ip)
    if ":" in ip:
        return ipaddress.IPv6Address(ip)
    else:
        return ipaddress.IPv4Address(ip)


def get_nics(nic):
    all_nics = psutil.net_if_addrs()
    nics = {}
    if not nic:
        nics = all_nics
    elif isinstance(nic, (list, tuple, set)):
        for name in nic:
            nics[name] = all_nics[name]
    else:
        nic = six.ensure_str(nic)
        nics[nic] = all_nics[nic]
    return nics


def get_ips(nics):
    ips = set()
    for nic in nics:
        for addr in nic:
            if addr.family in (socket.AF_INET, socket.AF_INET6):
                ips.add(get_ip(addr.address))
    return list(ips)


def checkip(ip, nic=None):
    ip = get_ip(ip)
    nics = get_nics(nic)
    for name, nic in nics.items():
        for addr in nic:
            if addr.family in (socket.AF_INET, socket.AF_INET6):
                if get_ip(addr.address) == ip:
                    return True, name
    return False, None


def checkport(port, proto="tcp", nic=None):
    found = False
    found_ips = []
    nics = get_nics(nic)
    ips = get_ips(nics.values())
    connections = psutil.net_connections(kind=proto)
    for connection in connections:
        if connection.status == "LISTEN":
            if connection.laddr.port == port:
                if connection.laddr.ip == "0.0.0.0" or connection.laddr.ip == "::" or get_ip(connection.laddr.ip) in ips:
                    found = True
                    found_ips.append(connection.laddr.ip)
    return found, found and found_ips or None


def checkproc_by_pid(pid):
    try:
        p = psutil.Process(pid=pid)
        return True, p.cmdline()
    except psutil.NoSuchProcess:
        return False, None

def checkproc_by_pidfile(pidfile):
    if not os.path.exists(pidfile):
        return False, None, None
    pidstr = ""
    with open(pidfile, "r", encoding="utf-8") as fobj:
        pidstr = fobj.read().strip()
    pid = int(pidstr)
    try:
        p = psutil.Process(pid=pid)
        return True, pid, p.cmdline()
    except psutil.NoSuchProcess:
        return False, None, None


def checkproc_by_command(command):
    found = False
    ps = []
    self_pids = get_self_pids()
    for p in psutil.process_iter():
        if p.pid in self_pids:
            continue
        cmdline = subprocess.list2cmdline(get_cmdline_or_name(p))
        if re.findall(command, cmdline):
            found = True
            ps.append(p)
    if not found:
        return False, None
    else:
        return True, ps


def cmd_checkip_core(ip, nic=None):
    found, nic = checkip(ip, nic)
    if found:
        print("Result:", "FOUND")
        print("    IP:", ip)
        print("   NIC:", nic)
        os.sys.exit(0)
    else:
        print("Result:", "NOT FOUND")
        print("    IP:", ip)
        os.sys.exit(1)

def cmd_checkport_core(port, proto="tcp", nic=None):
    found, ip = checkport(port, proto, nic)
    if found:
        print("Result:", "FOUND")
        print("  Port:", port)
        print("    IP:", ip)
        os.sys.exit(0)
    else:
        print("Result:", "NOT FOUND")
        print("  Port:", port)
        os.sys.exit(1)


def cmd_checkproc_by_pid(pid):
    running, cmdline = checkproc_by_pid(pid)
    if running:
        print("Result:", "FOUND")
        print("   PID:", pid)
        print("   Cmd:", subprocess.list2cmdline(cmdline))
        os.sys.exit(0)
    else:
        print("Result:", "NOT FOUND")
        print("   PID:", pid)
        os.sys.exit(1)


def cmd_checkproc_by_pidfile(pidfile):
    running, pid, cmdline = checkproc_by_pidfile(pidfile)
    if running:
        print("  Result:", "FOUND")
        print("PID file:", pidfile)
        print("     PID:", pid)
        print("     Cmd:", subprocess.list2cmdline(cmdline))
        os.sys.exit(0)
    else:
        print("  Result:", "NOT FOUND")
        print("PID file:", pidfile) 
        os.sys.exit(1)

def cmd_checkproc_by_command(command):
    running, ps = checkproc_by_command(command)
    if running:
        print("Result:", "FOUND")
        print("Search:", command)
        for p in ps:
            print("-"*60)
            print("   PID:", p.pid)
            print("   Cmd:", subprocess.list2cmdline(get_cmdline_or_name(p)))
        os.sys.exit(0)
    else:
        print("Result:", "NOT FOUND")
        print("Search:", command)
        os.sys.exit(1)

def cmd_checkproc_core(pid=None, pidfile=None, command=None):
    c = 0
    for o in [pid, pidfile, command]:
        if not o is None:
            c += 1
    if c != 1:
        print("Error: parameter can be one and only one of pid、pidfile、command.")
        os.sys.exit(2)
    if not pid is None:
        cmd_checkproc_by_pid(pid)
    elif not pidfile is None:
        cmd_checkproc_by_pidfile(pidfile)
    else:
        cmd_checkproc_by_command(command)


@click.group()
def main():
    """Check the status of the service by checking whether the IP exists whether the PROCESS exists or whether the LISTENING PORT exists.
    """
    pass


@main.command(name="checkip")
@click.option("-i", "--nic", multiple=True, required=False)
@click.argument("ip", nargs=1, required=True)
def cmd_checkip(nic, ip):
    """Check the IP address exists or not.
    """
    cmd_checkip_core(ip, nic)


@main.command(name="checkport")
@click.option("-i", "--nic", multiple=True, required=False)
@click.option("-p", "--proto", default="tcp", required=False, type=click.Choice(["tcp", "tcp4", "udp", "udp4", "inet", "inet4", "inet6", "tcp6", "udp6"]), help="Default to tcp.")
@click.argument("port", type=int, nargs=1, required=True)
def cmd_checkport(nic, proto, port):
    """Check the listening port exists or not.
    """
    cmd_checkport_core(port, proto, nic)


@main.command(name="checkproc")
@click.option("-i", "--pid", type=int, required=False)
@click.option("-f", "--pidfile", required=False)
@click.option("-c", "--command", required=False)
def cmd_checkproc(pid, pidfile, command):
    """Check process is still running or not.

    Notice: parameter can be one and only one of pid、pidfile、command.
    """
    cmd_checkproc_core(pid, pidfile, command)


if __name__ == "__main__":
    main()
