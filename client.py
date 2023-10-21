import socket, sys, threading, time, datetime

wrc = 100

def generate_data_sensor():
    global wrc
    wrc = wrc + 2
    return ((str(datetime.datetime.fromtimestamp(time.time()))), wrc)

def tcp_client():
    c_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_s.connect(("127.0.0.1", 8889))
    c_s.settimeout(10.0)
    initial_time = time.time()
    c_s.send("ping".encode())
    msg = c_s.recv(1024)
    ending_time = time.time()
    print(f"Connection establish: {datetime.datetime.fromtimestamp(time.time())} {str(ending_time - initial_time)}")
    while True:
        msg = "ping / " + str(generate_data_sensor())
        time.sleep(1)
        try:
            initial_time = time.time()
            c_s.send(msg.encode())
            msg_r = c_s.recv(1024)
            ending_time = time.time()
            elapsed_time = str(ending_time - initial_time)
            print(f"send: {msg} recv: {msg_r.decode()} in {elapsed_time}")
        except:
            print("Packet loss (Timeout > 10s)")

def main():
    thread = threading.Thread(target=tcp_client)
    thread.start()


main() if __name__ == "__main__" else sys.exit(1)