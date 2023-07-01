---------------------------------------------------
Name     					- Avinash Mahala(1002079433) & Amit Munna Gupta(1002066302)
Programming Language Used	- Python 3.9.7
---------------------------------------------------
Device Specifications:-
---------------------------------------------------
Processor	        Intel(R) Core(TM) i5-9300H CPU @ 2.40GHz   2.40 GHz
Installed RAM	    24.0 GB (23.8 GB usable)
System type	        64-bit operating system, x64-based processor
Pen and touch	    No pen or touch input is available for this display
Manufacturer		Acer
Device Model		Nitro AN517-51
---------------------------------------------------
Windows(Operating System) Specifications:-
---------------------------------------------------
Edition	      	Windows 11 Home Single Language Version	21H2
Installed on	Sat-30-Oct-2021
OS build		22000.1219
Experience		Windows Feature Experience Pack 1000.22000.1219.0
---------------------------------------------------
Python Used  	Version 3.9.7
---------------------------------------------------
This is a File Management System consisting of a File Server and a Client.
The File Server provides file management functionality, and the Client allows users to interact with the File Server to perform various operations on files.

Prerequisites
    - Python 3.x : Make sure you have Python 3.x installed on your system. You can download it from the official Python website: https://www.python.org/downloads/
    - Pyro4 library: Pyro4 is a library that enables communication between the client and server using Python Remote Objects (Pyro).
                     You can install Pyro4 using pip by running the following command:
                        pip install Pyro4

    - colorama library: The colorama library is used for styling the console output with colors. You can install it using pip by running the following command:
                        pip install colorama
Ensure that you have installed Python 3.x, Pyro4, and colorama before running the programs.

---------------------------------------------------
How the Code is Structured?
---------------------------------------------------
    The code is structured into two main components: 
    the client-side program (client.py) and the server-side program (server.py). 
    Each component serves a specific purpose and contains functions and classes related to that purpose.

Here's an overview of how the code is structured in each component:

Client-side Program (client.py)
    Import statements: Import necessary modules and libraries, including os, Pyro4, threading, time, traceback, colorama, base64, and subprocess.
    Constants: Define constants such as SYNC_FOLDER (the folder used for file synchronization) and SYNC_INTERVAL (the interval for synchronization).
    Class FileClient: Represents the file client and contains methods for interacting with the file server and performing operations.
    __init__(): Initialize the file client and set up the necessary attributes.
    handle_exception(): Handle and print exceptions with error messages.
    File operations: Methods for uploading, downloading, deleting, and renaming files on the file server.
    Computation operations: Methods for performing addition and sorting operations using the computation server.
    Synchronization methods: Methods for performing file synchronization between the client and server.
    Other utility methods: Methods for listing files, starting and stopping automatic synchronization, and the main synchronization loop.
    Main function: The entry point of the client program.

Create an instance of FileClient.
    Start the synchronization thread.
    Run a command loop to interact with the client program and perform various operations based on user input.

Server-side Program (server.py)
    Import statements: Import necessary modules and libraries, including os, Pyro4, base64, subprocess, and time.
    Constants: Define constants such as the Pyro4 object name for the file server.
    Class FileServer: Represents the file server and contains methods for file-related operations.
    __init__(): Initialize the file server and set up the necessary attributes.
    File operations: Methods for handling file uploads, downloads, deletions, and renames.
    Other utility methods: Method for listing files on the server.
    Class ComputationServer: Represents the computation server and contains methods for performing computations.
    __init__(): Initialize the computation server and set up the necessary attributes.
    Computation methods: Methods for performing addition and sorting operations.
    Main function: The entry point of the server program.
        Create instances of FileServer and ComputationServer.
        Register the server objects with Pyro4.
        Start the Pyro4 daemon to listen for client requests.

The code follows an object-oriented approach, with classes representing different components and methods encapsulating specific functionalities.
The main functions of both the client and server programs act as the entry points, where the necessary objects are instantiated and the programs are executed.

---------------------------------------------------
Steps To Run
    1. Clone the repository or download the `server.py` and `client.py` scripts.
    2. Install the required dependencies using pip:
            pip install Pyro4 colorama
    3. Open 3 Terminals(T1,T2,T3).
    4. In T1, Go To the Project Directory and Run The Below Command:-
        python -m Pyro4.naming
    5. Then, In T2, Run the Below Command:-
        python server.py
    6. Verify In T2, It should Run successfully and Message as below:-

        INFO: File and Computation servers registered.
        INFO: RPC Server is Running! Go To The Client Console and Do The Operations.

    7. Once The above message is displayed, then Open T3, Run the below command in T3:-
        python client.py
    8. In T3 Do The following Operations:-
        Options
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

File Server
    The File Server provides file management functionality and exposes it as a Pyro4 remote object. 
    The server script (`server.py`) needs to be running in order for clients to interact with it. 
    To start the file server, run the following command:

        python server.py

Computation Server
    The Computation Server performs computations on behalf of the client. 
    It exposes methods for addition and sorting operations. 
    The computation server is an integral part of the client script (`client.py`). 
    It is assumed to be running locally and can be accessed via the Pyro4 naming server.

Client
    The File Client is a command-line interface for interacting with the file server and computation server. 
    It allows users to perform operations such as uploading, downloading, deleting, renaming files, 
    performing computations, and synchronization. To start the client, run the following command:

        python client.py

Sync Folder
    The client maintains a sync folder where downloaded files are stored locally. 
    By default, the sync folder is named "sync_folder" and resides in the same directory as the `client.py` script.
    You can modify the `SYNC_FOLDER` constant in the script to change the sync folder location.

During the implementation of the client-side and server-side programs, 
I gained several insights and encountered a few issues. Here's a summary of what I learned and the challenges I faced:

Pyro4 and Remote Method Invocation (RMI):
    I learned about Pyro4, a powerful library for implementing distributed systems in Python.
    Pyro4 utilizes Remote Method Invocation (RMI) to enable communication between the client and server using Python objects.
    This allowed me to invoke remote methods on the server-side from the client-side seamlessly.

File Upload and Download:
    I implemented the functionality to upload and download files between the client and server.
    I learned how to read file data, encode it using base64, transmit it over the network, and decode it on the receiving end.

Synchronization:
    One of the key features of the project was automatic synchronization of files between the client and server.
    I implemented a synchronization mechanism that periodically checks for new, modified, and deleted files on both sides and performs the necessary actions to ensure consistency.
    This involved comparing file timestamps, handling file transfers, and managing file operations.

Error Handling and Exception Management:
    I focused on robust error handling and exception management to ensure the programs can gracefully handle unexpected scenarios.
    I learned to catch and handle various exceptions that can occur during file operations, network communication, and method invocations.

Threading and Concurrency:
    To enable automatic synchronization without blocking the main program, I utilized threading to run the synchronization process concurrently.
    I learned about creating and managing threads, synchronization mechanisms, and handling thread termination.

Challenges and Issues:

    Synchronization Timing:
        Determining the optimal synchronization timing was challenging. 
        I had to strike a balance between frequent syncing for real-time updates and longer intervals to minimize network and computational overhead.
    
    Exception Handling:
        Managing and handling exceptions in a distributed system can be complex. 
        I encountered some difficulties in handling exceptions across different components and ensuring error messages are informative and helpful.
    
    Network Configuration:
        Configuring the network settings, such as hostname, port number, and Pyro4 name server, required attention to ensure proper communication between the client and server. 
        Ensuring the firewall settings allow the required network traffic was also a consideration.
        Overall, this project provided valuable hands-on experience in building a client-server application using Pyro4, handling file operations, implementing synchronization, and managing exceptions. 
        It deepened my understanding of distributed systems, network communication, and concurrency.

