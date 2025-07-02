# ================== 1. Resource Cleanup ==================
# Python provides better alternatives for resource cleanup, such as context managers (with statement).
class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print(f"File '{filename}' opened.")

    def write_data(self, data):
        self.file.write(data)

    # Destructor to close the file
    def __del__(self):
        if self.file:
            self.file.close()
            print("File closed.")

file_handler = FileHandler("example.txt")
file_handler.write_data("Hello, World!")
# Destructor is called when `file_handler` goes out of scope or is explicitly deleted.


print("==================================================")
# ================== 2. Dropping Temporary Objects==================
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        print(f"Connecting to database at {self.host}...")

    def query(self, sql):
        print(f"Executing query: {sql}")

    def __del__(self):
        print("Closing database connection.")

db = DatabaseConnection("localhost")
db.query("SELECT * FROM users")
# Destructor is called automatically when `db` goes out of scope.


print("==================================================")
# ================== 3. Cleanup for Classes With Circular References =================
class Node:
    def __init__(self, name):
        self.name = name
        self.child = None

    def __del__(self):
        print(f"Node {self.name} is being destroyed.")

# Create cyclic references
node1 = Node("node1")
node2 = Node("node2")
node1.child = node2
node2.child = node1

# Delete the nodes
del node1
del node2
# Garbage collection eventually destroys the objects.


# print("==================================================")
# ================== 4. For Classes Managing External APIs or Services =================
# import socket
# oop NetworkClient:
#     def __init__(self, server, port):
#         self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.connection.connect((server, port))
#         print(f"Connected to {server}:{port}")
#
#     def send_data(self, data):
#         self.connection.sendall(data.encode())
#
#     def __del__(self):
#         print(f"Closing connection to {self.connection.getpeername()}")
#         self.connection.close()
#
# # Usage
# client = NetworkClient("localhost", 8080)
# client.send_data("Hello, Server!")
# # Destructor ensures connection cleanup when `client` is deleted or goes out of scope.
