import os
import Pyro4

UPLOADS_FOLDER = "uploads"
SYNC_FOLDER = "sync_folder"

@Pyro4.expose
class FileServer:
    def __init__(self):
        if not os.path.exists(UPLOADS_FOLDER):
            os.makedirs(UPLOADS_FOLDER)
        if not os.path.exists(SYNC_FOLDER):
            os.makedirs(SYNC_FOLDER)

    def upload(self, file_name, file_data, file_size):
        try:
            file_path = os.path.join(UPLOADS_FOLDER, file_name)
            with open(file_path, "wb") as file:
                file.write(file_data)
            return True
        except IOError as e:
            print(f"Error while uploading file '{file_name}': {e}")
            return False

    def download(self, file_name):
        file_path = os.path.join(UPLOADS_FOLDER, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as file:
                    return Pyro4.util.SerializerBase().serializeData(file.read())
            except IOError as e:
                print(f"Error while downloading file '{file_name}': {e}")
        else:
            print(f"File '{file_name}' not found on the server")
        return None

    def delete(self, file_name):
        file_path = os.path.join(UPLOADS_FOLDER, file_name)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                return True
            except OSError as e:
                print(f"Error while deleting file '{file_name}': {e}")
                return False
        else:
            print(f"File '{file_name}' not found on the server")
            return False

    def rename(self, old_name, new_name):
        old_path = os.path.join(UPLOADS_FOLDER, old_name)
        new_path = os.path.join(UPLOADS_FOLDER, new_name)
        if os.path.isfile(old_path):
            try:
                os.rename(old_path, new_path)
                return True
            except OSError as e:
                print(f"Error while renaming file '{old_name}' to '{new_name}': {e}")
                return False
        else:
            print(f"File '{old_name}' not found on the server")
            return False

    def list_files(self):
        files = os.listdir(UPLOADS_FOLDER)
        return files

@Pyro4.expose
class ComputationServer:
    def add(self, i, j):
        return i + j

    def sort(self, array):
        return sorted(array)

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
file_server_uri = daemon.register(FileServer)
comp_server_uri = daemon.register(ComputationServer)
ns.register("file.server", file_server_uri)
ns.register("computation.server", comp_server_uri)

print("File and Computation servers registered.")
print("RPC Server is Running! Go To The Client Console and Do The Operations.")
daemon.requestLoop()
