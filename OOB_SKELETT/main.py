from import_addresses import return_ip_address
import network_elements
import netmiko
from netmiko import ConnectHandler

appliances = []
ip_addresses = return_ip_address()


for ip_of_appliance in ip_addresses:
    appliances.append(network_elements.Appliances(ip_of_appliance))

for all_appliance in appliances:
    all_appliance.type = all_appliance.get_device_type()
    print(f"ip: {all_appliance.ip}, type: {all_appliance.type}")

# loopa alla objekt
# pinga alla objekt i loopen
# om ping går bra:
    # kolla wan utilization
    # kolla cpu
    # kolla ram
    # kolla temp
    # skicka till grafana
    # hämta snmp data
# om inte, uppdatera dns

# och pinga igen, skicka till grafana, osv


objeklt.kommandon[0]