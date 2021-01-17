import os
import re
import telnetlib
import time

rta_f0 = "192.168.1.3"
rta_s0 = None
RTA = None

rtb_f0 = "192.168.1.4"
rtb_s0 = None
RTB = None

password = b"123456"


def connect():
    global RTA
    RTA = connect_to_routing(rta_f0)
    global RTB
    RTB = connect_to_routing(rtb_f0)
    print(RTA is None)
    print(RTB is None)

def connect_to_routing(host):
    tn = telnetlib.Telnet(host, timeout=400000)

    tn.read_until(b'Password:')
    tn.write(password + b'\n')
    # 进入enable模式
    tn.write(b'enable\n')
    tn.write(password + b'\n')
    return tn


def init_config(routing, hostname, ip_address, mask):
    global rta_s0, rtb_s0

    if routing == 'RTA':
        rta_s0 = ip_address
    else:
        rtb_s0 = ip_address

    commands = read_commands("config.txt", hostname, ip_address, mask)
    return send_commands(commands, routing, 1)


def acl_config(routing):
    rt1_s0 = rtb_s0 if routing == 'RTA' else rta_s0
    rt2_s0 = rta_s0 if routing == 'RTA' else rtb_s0

    commands = read_commands("acl.txt", rt1_s0, rt2_s0)
    return send_commands(commands, routing, 1)


def cancel_acl_config(routing):
    commands = read_commands("cancel.txt")
    return send_commands(commands, routing, 1)


def verify(routing):
    rt_s0 = rta_s0 if routing == 'RTB' else rtb_s0
    commands = read_commands("ping.txt", rt_s0)
    result = send_commands(commands, routing, 5)
    # result = str(result).replace('\\r\\n', '\\n')
    print(result)
    return result


# 读取文件中的命令，并替换掉其中的占位词
# 按顺序使用args中的元素替换
# 返回命令列表
def read_commands(filename, *args):
    file_path = os.path.join(os.path.abspath('.'),'Telnet_Backend','script',filename)
    with open(file_path, 'r') as f:
        content = f.read()
        matches = re.findall(r"(?<=\$\{).*?(?=\})", content)
        for i in range(len(matches)):
            content = content.replace("${" + matches[i] + "}", str(args[i]))
        res = content.split('\n')
    return res


# 发送命令到路由器
def send_commands(commands, routing, time_interval):
    tn = RTA if routing == 'RTA' else RTB

    tn.read_very_eager()

    for one_command in commands:
        tn.write(bytes(one_command, encoding='UTF-8') + b'\n')

    time.sleep(time_interval)
    return tn.read_very_eager()
