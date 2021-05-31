showver = """Cisco IOS Software, 3800 Software (C3825-ADVENTERPRISEK9-M), Version 15.1(4)M12a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Tue 04-Oct-16 04:18 by prod_rel_team

ROM: System Bootstrap, Version 12.3(11r)T2, RELEASE SOFTWARE (fc1)

vedvpn001 uptime is 8 weeks, 6 days, 7 hours, 4 minutes
System returned to ROM by reload at 11:58:51 CEST Tue Mar 23 2021
System restarted at 12:00:52 CEST Tue Mar 23 2021
System image file is "flash:c3825-adventerprisek9-mz.151-4.M12a.bin"
Last reload type: Normal Reload


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.
          
A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 3825 (revision 1.1) with 1010688K/37888K bytes of memory.
Processor board ID FTX1039A0C5
3 Gigabit Ethernet interfaces
1 Virtual Private Network (VPN) Module
DRAM configuration is 64 bits wide with parity enabled.
479K bytes of NVRAM.
126976K bytes of ATA System CompactFlash (Read/Write)


License Info:

License UDI:

-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO3825             FTX1039A0C5     



Configuration register is 0x2102"""


for line in showver.split('\n'):
    if ' (revision' not in line:
        continue
    words_in_line = line.split(' ')
    type = words_in_line[1]

    print(type)

