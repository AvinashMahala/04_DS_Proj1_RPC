import threading
import time
from client import FileClient
import os

SYNC_FOLDER = "sync_folder"
SYNC_INTERVAL = 5  # Sync interval in seconds

def synchronize():
    # Create the sync folder if it doesn't exist
    if not os.path.exists(SYNC_FOLDER):
        os.makedirs(SYNC_FOLDER)

    client = FileClient()

    while True:
        # Check if it's time to sync
        current_time = time.time()
        if current_time - client.last_sync_time >= SYNC_INTERVAL:
            client.last_sync_time = current_time
            client.perform_sync()

        time.sleep(1)  # Sleep for 1 second

if __name__ == "__main__":
    # Create the sync folder if it doesn't exist
    if not os.path.exists(SYNC_FOLDER):
        os.makedirs(SYNC_FOLDER)

    # Start the synchronization thread
    sync_thread = threading.Thread(target=synchronize)
    sync_thread.start()
