# DS_Proj1_RPC

## Project Description

In this programming project, you will implement a simple file upload and download service and a computation service using remote procedure call (RPC) based communication.  
The file server needs to support four basic operations: UPLOAD, DOWNLOAD, DELETE, and RENAME a file.  
The computation server provides a set of predefined procedures that can be called from a client. The server should support add(i,j), and sort(array A).
You can use any programming language to implement this project.

https://docs.google.com/document/d/1W48EcuJl6pRcbRfCvdawZQdw74fPxbNHt2h-bs6Nnso/edit?usp=sharing


# RPC


## Table of Contents

- [Workflows](#workflows)
  - [UPLOAD a File](#upload-a-file)
  - [DOWNLOAD a File](#download-a-file)
  - [DELETE a File](#delete-a-file)
  - [RENAME a File](#rename-a-file)
  - [ADD 2 Numbers](#add-2-numbers)
  - [SORT a Given Array of Records](#sort-a-given-array-of-records)
  - [START AUTO SYNC](#start-auto-sync)
  - [STOP AUTO SYNC](#stop-auto-sync)
  - [EXIT](#exit)
- [Key Considerations](#key-considerations)
- [What We Have Learned](#what-we-have-learned)
- [What Issues We Have Encountered](#what-issues-we-have-encountered)
- [Installation, Setup, and Execution Instructions](#installation-setup-and-execution-instructions)
- [Pros or Cons of Our Approach](#pros-or-cons-of-our-approach)

## Workflows

### UPLOAD a File

Allows users to upload a file to the server-side program. Users specify the path to the file on their local machine, and the file is transferred to the server.

### DOWNLOAD a File

Enables users to download a file from the server-side program. Users provide the name of the file they want to download, and the file is retrieved from the server and saved locally.

### DELETE a File

Allows users to delete a file from the server-side program. Users specify the name of the file they wish to remove, and the file is deleted from the server.

### RENAME a File

Empowers users to rename a file on the server-side program. Users input the current name of the file and the new desired name. The file is then renamed on the server.

### ADD 2 Numbers

Enables users to perform addition operations using the client-side program. Users input two numbers, and the program calculates the sum, leveraging the computation capabilities of the server-side program.

### SORT a Given Array of Records

Allows users to sort an array of records using the client-side program. Users input the array of records, and the server-side program efficiently sorts it using an appropriate sorting algorithm (e.g., quicksort, mergesort, etc.). The sorted result is then provided to the user.

### START AUTO SYNC

Initiates automatic synchronization between the client-side program and the server-side program. This feature ensures that changes made on either side are automatically reflected in the other, providing seamless and up-to-date file synchronization.

### STOP AUTO SYNC

Allows users to stop the automatic synchronization between the client-side program and the server-side program. This gives users control over when the synchronization process should be halted.

### EXIT

Gracefully terminates the client-side program and exits the application. Ensures that all processes are properly closed, ongoing synchronization is stopped, and program resources are released.

## Key Considerations

- **Error Handling**: The client-side program should handle any exceptions that occur during network communication or file operations.

- **File Validation**: The client-side program can perform checks to ensure the current file name is valid and exists on the server before initiating file operations.

- **New Name Validation**: The client-side program can validate the new file name provided by the user to ensure it adheres to any naming conventions or restrictions.

- **Duplicate Names**: The server-side program should handle cases where the new file name conflicts with an existing file on the server.

- **File References**: If the renamed file is referenced by other files or systems, appropriate updates or notifications should be implemented to reflect the new file name.

- **Logging**: Logging file renaming actions can be beneficial for auditing purposes or troubleshooting.

- **Input Validation**: The client-side program can validate user inputs to ensure they are valid and meet the required format or constraints.

- **Data Types**: Consider the data types of numbers being added and ensure compatibility and accurate results.

- **Integer vs. Floating-Point**: Depending on requirements, determine whether addition should be performed on integers or floating-point numbers.

- **Overflow/Underflow**: Take into account potential issues with integer overflow or underflow when dealing with large or small numbers in addition operations.

- **Sorting Algorithm**: Choose an appropriate sorting algorithm based on the requirements and characteristics of the records in the array for the sorting workflow.

- **Record Structure**: Define the structure of the records and ensure consistency between the client-side and server-side programs for the sorting workflow.

- **Sorting Order**: Determine the desired sorting order (e.g., ascending or descending) and implement the sorting algorithm accordingly for the sorting workflow.

- **Synchronization Interval**: Define the time interval at which the synchronization thread checks for changes and performs synchronization for the auto sync workflows.

- **Conflict Resolution**: Decide how conflicts between client-side and server-side changes will be resolved (e.g., latest modification timestamp, user confirmation, etc.) for the auto sync workflows.

- **Termination**: Provide an option for the user to stop the automatic synchronization if desired for the auto sync workflows.

- **Efficient Synchronization**: Implement mechanisms to optimize synchronization, such as checking file modification timestamps and only syncing modified files for the auto sync workflows.

## What We Have Learned

Throughout the implementation of the client-side and server-side programs, We have gained valuable insights and learned several key lessons. Here are some of the main things We have learned:

- **Distributed Systems**: Implementing a client-server architecture using Pyro4 library has provided me with a practical understanding of distributed systems. We have learned how to design and develop applications that utilize remote procedure calls (RPC) to communicate between client and server.

- **Pyro4 Library**: Working with the Pyro4 library has given me hands-on experience with building distributed systems in Python. We have learned how to create Pyro objects, register them with a name server, and use proxies to invoke remote methods.

- **File Transfer**: Implementing file upload and download functionality has enhanced our knowledge of handling file operations in Python. We have learned how to read and write files, encode and decode file data using base64, and transfer files between client and server.

- **Error Handling**: Dealing with exceptions and error handling has been an important aspect of this project. We have learned how to catch and handle different types of exceptions to provide meaningful error messages and maintain the stability of the application.

- **Synchronization**: Implementing the synchronization feature has provided me with insights into managing concurrent processes. We have learned how to schedule and perform periodic tasks, handle file changes, and synchronize data between the client and server.

- **Command-Line Interface (CLI)**: Building a command-line interface for the client-side program has improved our understanding of user interaction and input validation. We have learned how to present options to the user, handle user inputs, and provide appropriate feedback.

- **Troubleshooting and Debugging**: During the development process, We encountered various issues and errors. This experience has taught me the importance of effective troubleshooting and debugging techniques. We have learned to use tools like traceback and print statements to identify and resolve issues in the code.

## What Issues We Have Encountered

During the implementation of the client-side and server-side programs, We encountered several challenges and issues that required troubleshooting and resolution. Here are some of the main issues We encountered:

- **Pyro4 Configuration**: Setting up the Pyro4 library and configuring the

 Pyro nameserver initially posed some challenges. We had to ensure that the Pyro4 library was properly installed and the nameserver was running correctly to establish communication between the client and server.

- **File Encoding and Decoding**: Working with file data required careful handling of encoding and decoding operations using base64. Ensuring the correct conversion between binary data and text representation was crucial to successfully transfer files between the client and server.

- **Error Handling and Exception Management**: Managing exceptions and error handling was an important aspect of the implementation. We had to anticipate and handle various types of errors, such as file not found, server not available, or invalid inputs from the user. Effectively capturing and conveying error messages to the user was crucial for a smooth user experience.

- **Synchronization Logic**: Implementing the synchronization feature required careful consideration of file changes and synchronization intervals. We encountered challenges in detecting file modifications, managing synchronization threads, and ensuring that the synchronization process functioned correctly without any conflicts or data loss.

- **User Input Validation**: Implementing a command-line interface required robust input validation to handle user inputs accurately. We faced challenges in validating user input for options, file paths, numbers, and arrays to prevent unexpected behavior or errors in the program.

- **Debugging and Testing**: Throughout the development process, We encountered various bugs and inconsistencies. Debugging and testing the code required careful examination of the program's behavior, using print statements and debugging tools to identify and fix issues.

## Installation, Setup, and Execution Instructions

To install, set up, and execute the client-side and server-side programs, please follow the instructions below:

**Prerequisites:**
- Python 3.x installed on your system.
- Pyro4 library installed. You can install it using the following command:
  ```
  pip install Pyro4
  ```
- Colorama library installed. You can install it using the following command:
  ```
  pip install colorama
  ```

**In One Terminal Run The Below Command before running server and client code (Make Sure Pyro4 is installed properly):**
```
Python -m Pyro4.naming
```

**Client-Side:**
1. Download the `client.py` file to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the `client.py` file is located.
3. Execute the following command to start the client program:
   ```
   python client.py
   ```
4. The client program will start running, and you will see a command-line interface (CLI) with a list of options.

**Server-Side:**
1. Download the `server.py` file to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the `server.py` file is located.
3. Execute the following command to start the server program:
   ```
   python server.py
   ```

4. The server program will start running and display the Pyro4 daemon URI, indicating that the server is ready to accept client connections.

**Using the Client-Side Program:**
- Once the client program is running, you can interact with the server using the provided command-line interface (CLI). Detailed usage instructions for each workflow are available in the workflows section above.

Please note that the provided instructions assume that the client and server are running on the same machine. If the client and server are running on different machines, you will need to modify the code to specify the correct IP address or hostname of the server in the client program.

## Pros or Cons of Our Approach

Based on the provided code and implementation, here are the potential pros and cons of our approach:

### Pros:

- **Modularity**: The code is structured into separate client and server programs, promoting modularity and separation of concerns. This makes it easier to understand and maintain the codebase.

- **Use of Pyro4**: Pyro4 is a powerful library for building distributed systems in Python. By leveraging Pyro4, we benefit from its features such as object serialization, remote method invocation, and name server integration, which simplify the development of distributed applications.

- **Synchronization**: The implementation includes a synchronization feature that automatically syncs files between the client and server at regular intervals. This ensures data consistency and reduces the risk of data loss or discrepancies.

- **Error Handling**: The code includes error handling and exception management, which helps in capturing and handling potential errors gracefully. This improves the overall robustness and reliability of the application.

- **Command-Line Interface**: The client program provides a command-line interface (CLI) for interacting with the server. This allows users to perform various operations by providing input through the CLI, offering a convenient and user-friendly way to interact with the system.

### Cons:

- **Lack of User Interface**: The application relies solely on a command-line interface, which may not be the most intuitive or visually appealing for all users. Consider adding a graphical user interface (GUI) to enhance the user experience and make the application more accessible.

- **Limited Error Reporting**: While the code includes error handling, the current implementation provides minimal error reporting to the user. Enhancing the error messages and providing more specific feedback can help users understand and resolve issues more effectively.

- **Lack of Authentication and Security**: The provided code does not include any authentication or security measures. It is important to consider implementing secure authentication mechanisms to ensure authorized access and protect data integrity.

- **Scalability and Performance**: The scalability and performance of the application may become a concern as the number of concurrent clients or the size of files increases. Consider optimizing the code and exploring distributed computing techniques to handle larger workloads efficiently.

- **Documentation and Comments**: While the code is well-structured, it lacks detailed documentation and comments to explain the purpose and functionality of each component. Adding comprehensive documentation and comments can improve code maintainability and facilitate collaboration with other developers.


