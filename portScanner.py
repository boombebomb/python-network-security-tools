import socket

def port_scanner(host, port):
    """ตรวจสอบสถานะ port และดึง banner"""
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        
        # ตรวจสอบสถานะ port
        result = s.connect_ex((host, port))
        
        if result == 0:
            print(f"Port {port} is open on {host}")
            
            # พยายามดึง banner
            try:
                banner_data = s.recv(1024)
                if banner_data:
                    print(f"Banner: {banner_data.decode('utf-8', errors='ignore').strip()}")
                else:
                    print("No banner available")
            except socket.timeout:
                print("Banner timeout")
            except socket.error:
                print("Cannot retrieve banner")
        else:
            print(f"Port {port} is closed on {host}")
            
    except socket.error as e:
        print(f"Connection error: {e}")
    finally:
        if s:
            s.close()

def validate_input(port):
    """ตรวจสอบ port ที่รับมา"""
    try:
        port_num = int(port)
        if not (1 <= port_num <= 65535):
            print("Port must be between 1-65535")
            return False, 0
        return True, port_num
    except ValueError:
        print("Invalid port number")
        return False, 0

def main():
    host = input("Please Enter the IP you want to scan: ")
    port_input = input("Port: ")
    
    is_valid, port_num = validate_input(port_input)
    if is_valid:
        port_scanner(host, port_num)

if __name__ == "__main__":
    main()