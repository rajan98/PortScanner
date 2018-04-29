import module as scanner

nm = scanner.PortScanner()

print('\n---------------------------Welcome-----------------------')
print('nmap version: {0}\n'.format(nm.nmap_version()))

scanHost = input('Enter IP: ')

fr = input('Enter starting port(Ex:-0) : ')
to = input('Enter Ending Port(Ex:-1024 : ')
scanPort = fr+'-'+to

print('\nScaning....')
nm.scan(scanHost,scanPort)

if(nm.all_hosts()==[]):
    print("Host Is Down")

for host in nm.all_hosts():
    print('Host: {0} ({1})'.format(host,nm[host].hostname()))
    print('State: {0}'.format(nm[host].state()))
    print('MAC: {0}'.format(nm[host]['addresses']['mac']))
    print('Vendor: {0}'.format(nm[host]['vendor'][nm[host]['addresses']['mac']]))

    for protocol in nm[host].all_protocols():
        print('Protocol: ', protocol)
        
        portList = nm[host][protocol].keys()

        print('{0:6s}'.format('Port'),end = '')
        print('{0:20s}'.format('Name'),end = '')
        print('{0:35s}'.format('Product'),end = '')
        print('{0:10s}'.format('Version'))

        for port in portList:
            print('{0:6s}'.format(str(port)),end = '')
            print('{0:20s}'.format(nm[host][protocol][port]['name']),end = '')
            print('{0:35s}'.format(nm[host][protocol][port]['product']),end ='')
            
            if(nm[host][protocol][port]['version']==''):
                version = 'Unknown'
            else:
                version = nm[host][protocol][port]['version']

            print('{0:10s}'.format(version))
