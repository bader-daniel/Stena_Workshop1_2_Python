import netmiko
from netmiko import ConnectHandler

# variables
approved_ios_versions = [['1.1', 'ws-c2960x-24pc-l', 'ws-c2960x-24ts-l'], ['1.1', '9200']]
#  nestled list, inner list is always approved ios-version first ([0]) followed by the models it's designated for.

# Variables where we store the results of the compliance checks
ssh_check = True
ios_version_check = True
hostname_check = True
login_check = True

# other variables we will need
try_telnet = False

# login and check if SSH works
print('everything you enter will be processed in clear text!')
ip = input('IP: ')
username = input('Username: ')
password = input('Password: ')

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': ip,
    'username': username,
    'password': password,
}

iosv_l2_telnet = {
    'device_type': 'cisco_ios_telnet',
    'ip': ip,
    'username': username,
    'password': password,
}


#  The below section handles the connection with netmiko. It will try to log in using SSH first, then telnet
try:
    net_connect = ConnectHandler(**iosv_l2) # TODO: more specific error handling if the connection doesn't work
except netmiko.ssh_exception.NetmikoTimeoutException:
    try_telnet = True
except netmiko.ssh_exception.NetmikoAuthenticationException:
    # Authentication error, TACACS, changed password?, user deleted?
    try_telnet = True
except netmiko.ssh_exception:
    try_telnet = True
    # Login error: any reason

# IF SSH doesn't work, try telnet
if try_telnet:
    try:
        net_connect = ConnectHandler(**iosv_l2_telnet)
        ssh_check = False
    except:
        login_check = False


# check if AAA works: we will not be doing this now, as it would require saved tacacs-credentials to be tested first

# check if an approved ios version is being used

# check if poe-access ports are using non-poe clients

# check the hostname follows name standard



