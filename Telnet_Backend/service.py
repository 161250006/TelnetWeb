import telnetlib

hostA = ""
usernameA = ""
passwordA = ""
RTA = None

hostB = ""
usernameB = ""
passwordB = ""
RTB = None


def connect():
    global RTA
    RTA = connect_to_routing(hostA, usernameA, passwordA)
    global RTB
    RTB = connect_to_routing(hostB, usernameB, passwordB)


def connect_to_routing(host, username, password):
    tn = telnetlib.Telnet(host)

    tn.read_until('login:')
    tn.write(username + '\n')

    tn.read_until('Password:')
    tn.write(password + '\n')
    return tn


def send_command(command, routing):
    if routing == 'RTA':
        tn = RTA
    else:
        tn = RTB
    tn.read_some()
    tn.write(command + '\n')
    return tn.read_some()
