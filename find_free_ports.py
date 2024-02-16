import socket

def find_free_port(start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
                return port
        except OSError:
            pass
    return None

start_port = 5000
end_port = 6000
free_port = find_free_port(start_port, end_port)
if free_port:
    print("Found available port:", free_port)
else:
    print("No available port found in the specified range.")