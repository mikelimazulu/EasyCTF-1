import socket

host = "127.0.0.1"
port = 55555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    clientsocket.send(b"""
                                                                                    
                                                                                
                                  .*//((///*.                                   
                             *((#####%%%%####(((/*                              
                          *(##%%%%%%%%%%%%%%####((((*                           
                        /(#%%%%%%%%%%%%%%%%%%%%%####((/                         
                      ,(#%%%%%%%%%%%%%%%%%%%%%%%%%%##(((*                       
                     /##%%%%%%%%%%%%%%%%%%%%%%%%%%%#/**,(/                      
                    #(##%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*,,,((                     
                    #(##%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(,../(.                    
                   .(###%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(,,.*(/                    
                    ((###((((%%%%%%%%%%%%%%%%%%%%%%%#(*,,/(/                    
                    #(###////(%%%%%%%%%%%%%%%%%%%%%%#(**,(((                    
                    %((##(////(%%%%%%%%%%%%%%%%%%%%%%##(((#                     
                     #((##(///(#%%%%%%%%%%%%%%%%%%%%%#####                      
                      %#(###//(#%%%%%%%%%%%%%%%%%%%%%###%                       
                        ######%%%%%%%%%%%%%%%%%%%%%%####                        
                         (###%%%%%%%%%%%%%%%%%%%%%%%#(                          
                           ,###%%%%%%%%%%%%%%%%%%%%(                            
                              (##%%%%%%%%%%%%%%#%/                              
                                /##%%%%%%%%%%##                                 
                                   .((%%###(                                    
                                      &%*                                       
                                        (                                       
                                                                                
                                           .                                    
                                                                                
                                            /                                   
                                          (                                     
                                                                                
                                           ,,                                   
                                              #                                 
                                            /                                   
                                         ,                                      
                                         /                                      
                                            (                                   
                                                                                
                                           (                                    
                                                                                
                                          /,,(.   
                                            
W3LC0M3 T0 CIBanc0, MY D3AR G0LD S0UTHFI3LD AG3NT.
T3LL M3, WHAT IS Y0UR MALWAR3???\n""")
    alias = clientsocket.recv(1024)
    print(alias)
    if alias == b"REvil\n":
        clientsocket.send(b"Y0U AR3 N0W C0NN3CT3D... PR0C33D.\n")
        while True:
            try:
                alias2 = clientsocket.recv(1024)
                if alias2 == b"help\n":
                    clientsocket.send(b"AVAILABL3 C0MMANDS: \n1 - help\n2 - ip\n3 - telnet\n")
                elif alias2 == b"ip\n":
                    clientsocket.send(b"S3RV3R: 10.10.10.1\nY0UR IP: 10.10.10.3\n")
                elif alias2 == b"telnet 10.10.10.2\n":
                    clientsocket.send(b"GRATZ! TH3 FLAG IS : W0lF-#RAE7S$86Yvqt8.\n")
                    clientsocket.close()
                else:
                    clientsocket.send(b"PR0C33D.\n")
            except OSError:
                break

    else:
        clientsocket.send(b"Y0U AR3 FAILUR3... TAK3 A BR3AK.\n")
        clientsocket.close()
