import os
import Pyro4
import threading
import time
import traceback
from colorama import Fore, Style, init
import pickle

SYNC_FOLDER = "sync_folder"
SYNC_INTERVAL = 5  # Sync interval in seconds

class FileClient:
    def __init__(self):
        self.file_server = Pyro4.Proxy("PYRONAME:file.server@localhost:9090")
        self.comp_server = Pyro4.Proxy("PYRONAME:computation.server@localhost:9090")
        self.last_sync_time = 0

    def handle_exception(self, message, exception):
        print(f"{Fore.RED}Error: {message}{Style.RESET_ALL}")
        print(f"{Fore.RED}Exception: {exception}{Style.RESET_ALL}")
        traceback.print_exc()

    def upload(self, file_path):
        try:
            with open(file_path, "rb") as file:
                file_name = file_path.split("/")[-1]
                file_data = file.read()
            file_size = len(file_data)
            file_data_serialized = pickle.dumps(file_data)
            success = self.file_server.upload(file_name, file_data_serialized, file_size)
            if success:
                print(f"File '{file_name}' uploaded successfully")
            else:
                print(f"Error while uploading file '{file_name}'")
        except IOError as e:
            print(f"Error while reading file '{file_path}': {e}")
        except Exception as e:
            print(f"Error while uploading file '{file_path}': {e}")
            traceback.print_exc()

    def download(self, file_name):
        try:
            file_data, file_size = self.file_server.download(file_name)
            if file_data:
                file_path = os.path.join(SYNC_FOLDER, file_name)
                with open(file_path, "wb") as file:
                    file.write(file_data)
                print(f"{Fore.GREEN}File '{file_name}' downloaded successfully{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}File '{file_name}' not found on the server{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error while downloading file '{file_name}': {e}{Style.RESET_ALL}")

    def delete(self, file_name):
        try:
            success = self.file_server.delete(file_name)
            if success:
                print(f"{Fore.GREEN}File '{file_name}' deleted successfully{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}File '{file_name}' not found on the server{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error while deleting file '{file_name}': {e}{Style.RESET_ALL}")

    def rename(self, old_name, new_name):
        try:
            success = self.file_server.rename(old_name, new_name)
            if success:
                print(f"{Fore.GREEN}File '{old_name}' renamed to '{new_name}'{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}File '{old_name}' not found on the server{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error while renaming file '{old_name}': {e}{Style.RESET_ALL}")

    def add(self, i, j):
        try:
            return self.comp_server.add(i, j)
        except Exception as e:
            print(f"{Fore.RED}Error while performing addition: {e}{Style.RESET_ALL}")

    def sort(self, array):
        try:
            return self.comp_server.sort(array)
        except Exception as e:
            print(f"{Fore.RED}Error while performing sort: {e}{Style.RESET_ALL}")

    def synchronize(self):
        while True:
            # Check if it's time to sync
            current_time = time.time()
            if current_time - self.last_sync_time >= SYNC_INTERVAL:
                self.last_sync_time = current_time
                self.perform_sync()

            time.sleep(1)  # Sleep for 1 second

    def perform_sync(self):
        # Get the list of files in the sync folder
        local_files = os.listdir(SYNC_FOLDER)

        # Check for new files or modified files
        for file_name in local_files:
            file_path = os.path.join(SYNC_FOLDER, file_name)
            if os.path.isfile(file_path):
                # Check if the file was modified after the last sync
                if os.path.getmtime(file_path) > self.last_sync_time:
                    self.upload(file_path)

        # Check for deleted files
        server_files = self.list_files()
        for file_name in server_files:
            file_path = os.path.join(SYNC_FOLDER, file_name)
            if not os.path.isfile(file_path):
                self.download(file_name)

    def list_files(self):
        try:
            return self.file_server.list_files()
        except Exception as e:
            print(f"{Fore.RED}Error while listing files: {e}{Style.RESET_ALL}")
            return []

def main():
    client = FileClient()

    while True:
        command = input(f"{Fore.CYAN}Enter command (UPLOAD, DOWNLOAD, DELETE, RENAME, ADD, SORT): {Style.RESET_ALL}")
        if command == "UPLOAD":
            file_name = input("Enter file name: ")
            client.upload(file_name)
        elif command == "DOWNLOAD":
            file_name = input("Enter file name: ")
            client.download(file_name)
        elif command == "DELETE":
            file_name = input("Enter file name: ")
            client.delete(file_name)
        elif command == "RENAME":
            old_name = input("Enter old file name: ")
            new_name = input("Enter new file name: ")
            client.rename(old_name, new_name)
        elif command == "ADD":
            i = int(input("Enter first number: "))
            j = int(input("Enter second number: "))
            result = client.add(i, j)
            print(f"Addition result: {result}")
        elif command == "SORT":
            array = input("Enter the array (comma-separated values): ").split(",")
            array = [int(x.strip()) for x in array]
            result = client.sort(array)
            print(f"Sorted array: {result}")
        else:
            print(f"{Fore.RED}Invalid command{Style.RESET_ALL}")

if __name__ == "__main__":
    # Initialize colorama for cross-platform styling
    init(autoreset=True)

    main()
