import socket
import time

def send_scpi_commands(ip_address, port, commands, delay=0.5):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the device
        sock.connect((ip_address, port))
        
        for command in commands:
            # Send the command
            sock.sendall(command.encode('utf-8') + b'\n')
            
            # Receive the response
            response = sock.recv(4096)
            print(f"Response: {response.decode('utf-8')}")
            
            # Introduce a delay between commands
            time.sleep(delay)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the socket
        sock.close()

# Example usage
ip_address = '192.168.1.11'  # Replace with the actual IP address of the FSV43
port = 5025  # Replace with the actual port number
commands = [
    #":SYST:DISP:UPD ON\n",
    ":SENS1:SWE:TIME 5\n"
    '''
    ":*STB?\n",
    ":INIT:CONT:OFF\n",
    ":*STB?\n",
    ":SENS1:SWE:POIN 300\n",
    ":*STB?\n",
    ":SENS1:BAND:RES 5000000\n",
    ":*STB?\n",
    ":SENS1:SWE:TIME:AUTO OFF\n",
    ":*STB?\n",
    ":SENS1:BAND:VID 20000000\n",
    ":SENS1:SWE:TIME 5\n",
    ":*STB?\n",
    ":*TRG,*OPC?\n",
    ":CALC1:MARK1:FUNC:MAX:PEAK\n",
    ":SYST:DISP:UPD ON"
    '''
]

send_scpi_commands(ip_address, port, commands)
