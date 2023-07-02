import os
import Pyro4
import threading
import time
import traceback
from colorama import Fore, Style, init
import base64

UPLOADS_FOLDER = "server_uploads"
SYNC_FOLDER = "client_downloads"

@Pyro4.expose
class FileServer:
    def __init__(self):
        self.sync_folder = SYNC_FOLDER
        if not os.path.exists(UPLOADS_FOLDER):
            os.makedirs(UPLOADS_FOLDER)
        if not os.path.exists(SYNC_FOLDER):
            os.makedirs(SYNC_FOLDER)

    def check_file_exists(self, file_name):
        try:
            file_path = os.path.join(self.folder_path, file_name)
            return os.path.exists(file_path)
        except Exception:
            return False

    def upload(self, file_name, file_data):
        try:
            file_path = os.path.join(UPLOADS_FOLDER, file_name)
            with open(file_path, "wb") as file:
                decoded_data = base64.b64decode(file_data)
                file.write(decoded_data)
            return True
        except IOError as e:
            print(f"SERVER: Error while uploading file '{file_name}': {e}")
            return False
        except Exception as e:
            print(f"SERVER: Error while uploading file '{file_name}': {e}")
            import traceback
            traceback.print_exc()
            return False



    def download(self, file_name):
        try:
            file_path = os.path.join(UPLOADS_FOLDER, file_name)
            if os.path.isfile(file_path):
                with open(file_path, "rb") as file:
                    file_data = file.read()
                    encoded_data = base64.b64encode(file_data).decode("utf-8")
                    return encoded_data
            else:
                print(f"SERVER: File '{file_name}' not found on the server")
        except IOError as e:
            print(f"SERVER: Error while downloading file '{file_name}': {e}")
        except Exception as e:
            print(f"SERVER: Error while downloading file '{file_name}': {e}")
            import traceback
            traceback.print_exc()
        return None

    def delete(self, file_name):
        try:
            file_path = os.path.join(UPLOADS_FOLDER, file_name)
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    return True
                except OSError as e:
                    print(f"SERVER: Error while deleting file '{file_name}': {e}")
                    return False
            else:
                print(f"SERVER: File '{file_name}' not found on the server")
                return False
        except Exception as e:
            print(f"SERVER: Error while deleting file '{file_name}': {e}")
            import traceback
            traceback.print_exc()
            return False

    def rename(self, old_name, new_name):
        try:
            old_path = os.path.join(UPLOADS_FOLDER, old_name)
            new_path = os.path.join(UPLOADS_FOLDER, new_name)
            if os.path.isfile(old_path):
                try:
                    os.rename(old_path, new_path)
                    return True
                except OSError as e:
                    print(f"SERVER: Error while renaming file '{old_name}' to '{new_name}': {e}")
                    return False
            else:
                print(f"SERVER: File '{old_name}' not found on the server")
                return False
        except Exception as e:
            print(f"SERVER: Error while renaming file '{old_name}' to '{new_name}': {e}")
            import traceback
            traceback.print_exc()
            return False

    def list_files(self):
        try:
            files = os.listdir(UPLOADS_FOLDER)
            return files
        except Exception as e:
            print(f"SERVER: Error while listing files: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def get_last_modified(self, file_name):
        file_path = os.path.join(self.sync_folder, file_name)
        if os.path.exists(file_path):
            return os.path.getmtime(file_path)
        else:
            return None

@Pyro4.expose
class ComputationServer:
    def add(self, i, j):
        try:
            return i + j
        except Exception as e:
            print(f"SERVER: Error while adding {i} and {j}: {e}")
            import traceback
            traceback.print_exc()
            return None

    def sort(self, array):
        try:
            return sorted(array)
        except Exception as e:
            print(f"SERVER: Error while sorting {array}: {e}")
            import traceback
            traceback.print_exc()
            return None

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
file_server_uri = daemon.register(FileServer)
comp_server_uri = daemon.register(ComputationServer)
ns.register("file.server", file_server_uri)
ns.register("computation.server", comp_server_uri)

print("INFO: File and Computation servers registered.")
print("INFO: RPC Server is Running! Go To The Client Console and Do The Operations.")

try:
    daemon.requestLoop()
except Exception as e:
    print(f"SERVER: Error while running the server: {e}")
    import traceback
    traceback.print_exc()
    daemon.shutdown()
