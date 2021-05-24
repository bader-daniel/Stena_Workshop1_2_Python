
def return_ip_address():
    separator = ','

    with open('adresser.csv', 'r') as adresser:
        ip_str = adresser.read()
        ip_adresser = ip_str.split(separator)


    for enum, adress in enumerate(ip_adresser):
        ip_adresser[enum] = adress.strip()


    return ip_adresser