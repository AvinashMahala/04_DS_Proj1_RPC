import os
import Pyro4
import threading
import time
import traceback
from colorama import Fore, Style, init
import base64
import subprocess

SYNC_FOLDER = "sync_folder"
SYNC_INTERVAL = 5  # Sync interval in seconds

class FileClient:
    def __init__(self):
        self.file_server = Pyro4.Proxy("PYRONAME:file.server@localhost:9090")
        self.comp_server = Pyro4.Proxy("PYRONAME:computation.server@localhost:9090")
        self.last_sync_time = 0
        self.sync_thread = None
        self.is_syncing = False

    def handle_exception(self, message, exception):
        print(f"{Fore.RED}Error: {message}{Style.RESET_ALL}")
        print(f"{Fore.RED}Exception: {exception}{Style.RESET_ALL}")
        traceback.print_exc()

    def upload(self, file_path):
        try:
            with open(file_path, "rb") as file:
                file_name = file_path.split("/")[-1]
                file_data = file.read()
                encoded_data = base64.b64encode(file_data).decode("utf-8")
                success = self.file_server.upload(file_name, encoded_data)
                if success:
                    print(f"{Fore.GREEN}File '{file_name}' uploaded successfully.")
                else:
                    print(f"Error while uploading file '{file_name}'.")
        except IOError as e:
            msg = f"Error while reading file '{file_path}'"
            self.handle_exception(msg, e)
        except Exception as e:
            msg = f"Error while uploading file '{file_path}'"
            self.handle_exception(msg, e)

    def download(self, file_name):
        try:
            file_data = self.file_server.download(file_name)
            if file_data is not None:
                file_path = os.path.join(SYNC_FOLDER, file_name)
                decoded_data = base64.b64decode(file_data)
                with open(file_path, "wb") as file:
                    file.write(decoded_data)
                print(f"{Fore.GREEN}File '{file_name}' downloaded successfully.")
            else:
                print(f"Error while downloading file '{file_name}'")
        except IOError as e:
            msg = f"Error while writing file '{file_name}'."
            self.handle_exception(msg, e)
        except Exception as e:
            msg = f"Error while downloading file '{file_name}'."
            self.handle_exception(msg, e)

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
        while self.is_syncing:
            # Check if it's time to sync
            current_time = time.time()
            if current_time - self.last_sync_time >= SYNC_INTERVAL:
                self.last_sync_time = current_time
                self.perform_sync()

            time.sleep(SYNC_INTERVAL)  # Sleep for SYNC_INTERVAL second(s).

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

    def start_sync(self):
        if self.is_syncing:
            print("Sync is already in progress.")
        else:
            self.is_syncing = True
            self.sync_thread = threading.Thread(target=self.synchronize)
            self.sync_thread.start()
            print("Sync started.")

    def stop_sync(self):
        if self.is_syncing:
            self.is_syncing = False
            self.sync_thread.join()
            self.sync_thread = None
            print("Sync stopped.")
        else:
            print("Sync is not currently active.")

def main():
    client = FileClient()

    # Start synchronization in a separate thread
    sync_thread = threading.Thread(target=client.synchronize)
    sync_thread.daemon = True  # Allow the program to exit even if the thread is still running
    sync_thread.start()

    while True:
        print("\n Choose an option:")
        print("   1. UPLOAD: Upload a file.")
        print("   2. DOWNLOAD: Download a file.")
        print("   3. DELETE: Delete a file.")
        print("   4. RENAME: Rename a file.")
        print("   5. ADD: Add Two Numbers.")
        print("   6. SORT: Sort a given an array of records.")
        print("   7. SYNC NOW: Sync immediately.")
        print("   8. START AUTO SYNC: Start automatic synchronization.")
        print("   9. STOP AUTO SYNC: Stop automatic synchronization.")
        print("   0. EXIT: Exit the program.\n")
        command = input("Enter the option number: ")

        if command == "1":
            file_path = input("Enter file path: ")
            client.upload(file_path)
        elif command == "2":
            file_name = input("Enter file name: ")
            client.download(file_name)
        elif command == "3":
            file_name = input("Enter file name: ")
            client.delete(file_name)
        elif command == "4":
            old_name = input("Enter old file name: ")
            new_name = input("Enter new file name: ")
            client.rename(old_name, new_name)
        elif command == "5":
            i = int(input("Enter first number: "))
            j = int(input("Enter second number: "))
            result = client.add(i, j)
            print(f"Addition result: {result}")
        elif command == "6":
            array = input("Enter the array (comma-separated values): ").split(",")
            array = [int(x.strip()) for x in array]
            result = client.sort(array)
            print(f"Sorted array: {result}")
        elif command == "7":
            client.perform_sync()
            print("Sync is Completed.")
        elif command == "8":
            client.start_sync()
        elif command == "9":
            client.stop_sync()
        elif command == "0":
            break
        else:
            print(f"{Fore.YELLOW}Invalid option!{Style.RESET_ALL}")
    print("Exiting...")

if __name__ == "__main__":
    # Initialize colorama for cross-platform styling
    init(autoreset=True)

    main()
