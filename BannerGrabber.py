import socket

def banner(ip, port):
    """ดึงข้อมูล banner จาก server"""
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, int(port)))
        
        banner_data = s.recv(1024)
        if banner_data:
            print(f"Banner: {banner_data.decode('utf-8', errors='ignore').strip()}")
        else:
            print("No banner received")
            
    except socket.timeout:
        print("Connection timeout")
    except socket.error as e:
        print(f"Connection error: {e}")
    except ValueError:
        print("Invalid port number")
    finally:
        if s:
            s.close()

def validate_input(ip, port):
    """ตรวจสอบ input ที่รับมา"""
    try:
        port_num = int(port)
        if not (1 <= port_num <= 65535):
            print("Port must be between 1-65535")
            return False
        return True
    except ValueError:
        print("Invalid port number")
        return False

def main():
    ip = input("Enter IP address: ")
    port = input("Enter port: ")
    
    if validate_input(ip, port):
        banner(ip, port)

if __name__ == "__main__":
    main()