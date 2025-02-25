import socket
import base64

def decode_message(message):
    
    decoded_message = base64.b64decode(message).decode('utf-8')
    return decoded_message

def start_server():
    host = '127.0.0.1'  
    port = 12345         

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  

    print(f"Sunucu başlatıldı, {host}:{port} adresinde dinleniyor...")
    client_socket, client_address = server_socket.accept()
    print(f"Bağlantı kuruldu: {client_address}")

    while True:
        data = client_socket.recv(1024)  
        if not data:
            break  
        
        decoded_message = decode_message(data.decode('utf-8'))
        print(f"Gelen mesaj: {decoded_message}")

        
        response = "Mesaj alındı"
        encoded_response = base64.b64encode(response.encode('utf-8')).decode('utf-8')
        client_socket.send(encoded_response.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    start_server()
