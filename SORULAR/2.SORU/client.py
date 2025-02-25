import socket
import base64

def encode_message(message):
    
    encoded_message = base64.b64encode(message.encode('utf-8')).decode('utf-8')
    return encoded_message

def start_client():
    host = '127.0.0.1'  
    port = 12345         

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Göndermek istediğiniz mesajı yazın (çıkmak için 'exit' yazın): ")

        if message == 'exit':
            break

        
        encoded_message = encode_message(message)

       
        client_socket.send(encoded_message.encode('utf-8'))

        
        data = client_socket.recv(1024)
        decoded_response = base64.b64decode(data).decode('utf-8')
        print(f"Sunucudan gelen yanıt: {decoded_response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
