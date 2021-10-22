# Use this script to stresstest the Zenon Network Testnet. 
# This script sends 1 znn between pairs in your wallet (keystore). I used 5 pairs, or all 10 addresses.
# You can use less addresses, then make sure you still have an even amount and remove unused addresses from the ADDRESS_LIST variable.

# Make sure all your addresses have a sufficient balance of ZNN (I recommend at least a couple hundred, I did 1000 per address). 
# Make sure all your addresses have Plasma. (I did 20k QSR per address)

# Fill in your passphrase for the wallet and copy & paste the addresses from syrius settings. 

import subprocess
import time

# Variable settings
USE_SCHEDULED_MODE = True # Scheduled mode uses START_TIME and DURATION_IN_SECS. Otherwise script runs infinitely and must be cancelled manually
START_TIME = '2021-10-13_09-37'
DURATION_IN_SECS = 60

KEYSTORE = 'Instance of \'Future<Address?>\'_1234567890123' # Example only
PASSPRASE = ''
AMOUNT = 1
COIN = 'znn'

ZNN_CLI = './znn-cli'
CMD_ZNND_START = ZNN_CLI + ' start znnd'
CMD_RPC_ENABLE = ZNN_CLI + ' enableRPC'
CMD_ZNND_STOP = ZNN_CLI + ' stop znnd' # Only used in scheduled mode
CMD_RPC_DISABLE = ZNN_CLI + ' disableRPC' # Only used in scheduled mode

SYRIUS_ADDRESS_0 = ''
SYRIUS_ADDRESS_1 = ''
SYRIUS_ADDRESS_2 = ''
SYRIUS_ADDRESS_3 = ''
SYRIUS_ADDRESS_4 = ''
SYRIUS_ADDRESS_5 = ''
SYRIUS_ADDRESS_6 = ''
SYRIUS_ADDRESS_7 = ''
SYRIUS_ADDRESS_8 = ''
SYRIUS_ADDRESS_9 = ''

ADDRESS_LIST = [SYRIUS_ADDRESS_0, SYRIUS_ADDRESS_1, SYRIUS_ADDRESS_2, SYRIUS_ADDRESS_3, SYRIUS_ADDRESS_4,
                SYRIUS_ADDRESS_5, SYRIUS_ADDRESS_6, SYRIUS_ADDRESS_7, SYRIUS_ADDRESS_8, SYRIUS_ADDRESS_9]

START_TIME_EPOCH = time.mktime(time.strptime(START_TIME, "%Y-%m-%d_%H-%M"))
END_TIME_EPOCH = START_TIME_EPOCH + DURATION_IN_SECS
if USE_SCHEDULED_MODE and START_TIME_EPOCH < time.time():
    print(f'Error: START_TIME variable is set to {START_TIME} but must be < than current time')
    exit()

TOTAL_SEND_TXS = 0
TOTAL_RECEIVE_TXS = 0
send_commands = []

for index_first_address, (first_in_pair, second_in_pair) in enumerate(zip(ADDRESS_LIST[::2], ADDRESS_LIST[1::2])):
    index_first_address = index_first_address * 2
    index_second_address = index_first_address + 1
    znn_send_command_1 = f'{ZNN_CLI} send {second_in_pair} {AMOUNT} {COIN} -i {index_first_address} -p {PASSPRASE} -k "{KEYSTORE}"' 
    znn_send_command_2 = f'{ZNN_CLI} send {first_in_pair} {AMOUNT} {COIN} -i {index_second_address} -p {PASSPRASE} -k "{KEYSTORE}"' 
    send_commands.append(znn_send_command_1)
    send_commands.append(znn_send_command_2)
    
receive_commands = []
for index, address in enumerate(ADDRESS_LIST):
    receive_commands.append(f'{ZNN_CLI} receiveAll -i {index} -p {PASSPRASE} -k "{KEYSTORE}"')

def run(cmd: str) -> str:
    completed = subprocess.run([cmd], capture_output=True, shell=True, text=True)
    if completed.returncode != 0:
        print(f'An error occured:" {completed.stderr}')
    else:
        print(f'Command executed successfully: {completed.stdout}') 

def run_childs():
    i = 0
    procs = []
    for command in send_commands:
        print(f'sending from address {i}')
        procs.append(subprocess.Popen([command], shell=True, text=True))
        i = i + 1
    for proc in procs:
        proc.wait()
        
    global TOTAL_SEND_TXS
    TOTAL_SEND_TXS = TOTAL_SEND_TXS + i
    print(f'Total sending transactions so far: {TOTAL_SEND_TXS}')
        
    j = 0
    procs = []
    for command in receive_commands:
        print(f'receiving on address {j}')
        procs.append(subprocess.Popen([command], shell=True, text=True))
        j = j + 1
    for proc in procs:
        proc.wait()
    
    global TOTAL_RECEIVE_TXS
    TOTAL_RECEIVE_TXS = TOTAL_RECEIVE_TXS + j
    print(f'Total receiving transactions so far: {TOTAL_RECEIVE_TXS}')
    
    return 

if __name__ == '__main__':
    run(CMD_RPC_ENABLE)
    run(CMD_ZNND_START)
    if USE_SCHEDULED_MODE:
        while time.time() < START_TIME_EPOCH:
            time.sleep(30)
        while time.time() < END_TIME_EPOCH:
            run_childs()
        run(CMD_ZNND_STOP)
        run(CMD_RPC_DISABLE)
        print(f'Script successfully executed for {DURATION_IN_SECS} seconds.')
        print(f'Total sending transactions performed: {TOTAL_SEND_TXS}.')
        print(f'Total receiving transactions performed: {TOTAL_RECEIVE_TXS}.')
    else:
        while True:
            run_childs()
