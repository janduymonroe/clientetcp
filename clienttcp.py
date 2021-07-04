import socket
import sys

def main ():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("The connection has been fail!")
        print(f"Error: {e}")
        sys.exit()
    print("Socket has been succesfull created!")


    targethost = input("Type the Host or IP for connection: ")

    while True:

        try:
            targetport = int(input("Type the port for access: "))
            break
        except:
            print("Type only the available port number")


    try:
            s.connect((targethost, (targetport)))
            print(f"TCP Client succesfull connected on host {targethost} in port {targetport}.")
            s.shutdown(2)
    except socket.error as e:
            print(f"It was not possible to connect to port {targetport} in host {targethost}.")
            print(f"Error: {e}")
            sys.exit()


if __name__ == "__main__":
    main()

