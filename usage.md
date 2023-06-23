## Prerequisites

- Python 3.x
- Pyro4 library
- colorama library

## Installation

1. Clone the repository or download the `server.py` and `client.py` scripts.
2. Install the required dependencies using pip:

   ```shell
   pip install Pyro4 colorama
   ```

### File Server

The File Server provides file management functionality and exposes it as a Pyro4 remote object. The server script (`server.py`) needs to be running in order for clients to interact with it. To start the file server, run the following command:

```shell
python server.py
```

### Computation Server

The Computation Server performs computations on behalf of the client. It exposes methods for addition and sorting operations. The computation server is an integral part of the client script (`client.py`). It is assumed to be running locally and can be accessed via the Pyro4 naming server.

## Client

The File Client is a command-line interface for interacting with the file server and computation server. It allows users to perform operations such as uploading, downloading, deleting, renaming files, performing computations, and synchronization. To start the client, run the following command:

```shell
python client.py
```

### Options

The following options are available in the client program:

- UPLOAD: Upload a file to the file server.
- DOWNLOAD: Download a file from the file server.
- DELETE: Delete a file from the file server.
- RENAME: Rename a file on the file server.
- ADD: Perform addition of two numbers using the computation server.
- SORT: Sort an array of records using the computation server.
- SYNC NOW: Trigger an immediate synchronization with the file server.
- START AUTO SYNC: Start automatic synchronization at regular intervals.
- STOP AUTO SYNC: Stop automatic synchronization.
- EXIT: Exit the program.

## Sync Folder

The client maintains a sync folder where downloaded files are stored locally. By default, the sync folder is named "sync_folder" and resides in the same directory as the `client.py` script. You can modify the `SYNC_FOLDER` constant in the script to change the sync folder location.
