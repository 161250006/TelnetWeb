import telnetlib
import time

hostA = "192.168.1.3"
passwordA = b"123456"
RTA = None

hostB = "192.168.1.4"
passwordB = b"123456"
RTB = None


def connect():
    global RTA
    RTA = connect_to_routing(hostA,  passwordA)
    global RTB
    RTB = connect_to_routing(hostB, passwordB)


def connect_to_routing(host, password):
    tn = telnetlib.Telnet(host)

    tn.read_until(b'Password:')
    tn.write(password + b'\n')
    return tn


def send_command(command, routing):
    if routing == 'RTA':
        tn = RTA
    else:
        tn = RTB
    tn.write(bytes(command, encoding='UTF-8') + b'\n')
    if command.startswith('ping'):
        time.sleep(5)
    else:
        time.sleep(1)
    return tn.read_very_eager()
