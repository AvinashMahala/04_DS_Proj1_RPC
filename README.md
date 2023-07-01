# DS_Proj1_RPC

## Project Description

In this programming project, you will implement a simple file upload and download service and a computation service using remote procedure call (RPC) based communication.  
The file server needs to support four basic operations: UPLOAD, DOWNLOAD, DELETE, and RENAME a file.  
The computation server provides a set of predefined procedures that can be called from a client. The server should support add(i,j), and sort(array A).
You can use any programming language to implement this project.

https://docs.google.com/document/d/1W48EcuJl6pRcbRfCvdawZQdw74fPxbNHt2h-bs6Nnso/edit?usp=sharing



## Part-1 (20 points)  
Implement a multi-threaded file server that supports UPLOAD, DOWNLOAD, DELETE, and RENAME file operations. Use different folders to hold files downloaded to the client or uploaded to the server. 

## Part-2 (30 points)  
The file transfer between the client and the server can be made transparent to users and automatically handled by a helper thread. This creates a Dropbox-like synchronized storage service. Whenever changes are made to the synchronized folder at the client side, e.g., creating a new file, updating a file, or deleting a file, the helper thread will establish a connection with the server and automatically send the corresponding operation to the server to update the folder at the server side. You can configure the helper thread to periodically check if there are changes made to the synchronized folder. If the last update time to a file is later than the last check, the file should be synchronized. To simplify the design, we do not need to consider incremental updates. Thus, if the content of a file is updated, the entire file can be sent to the server to overwrite the original copy at the server.  

## Part-3 (30 points)  
Implement a computation server to support add(i, j), and sort(array A) operations using synchronous, asynchronous RPCs. In synchronous RPC, the client makes the RPC call and waits for the result from the server. In asynchronous RPC, the client makes the RPC call and waits for an acknowledgment from the server, and continues after receiving an acknowledgment. On the other hand, after completing the computation the server sends the result of the call back to the client/the client fetches the result from the server afterward.

## Deliverables  (20 points) 
The deliverables include the source code of the client-side and server-side programs, a README file (10 points) containing instructions on how to compile and run your program, and a report (10 points) that briefly describes how you implemented the programs, what you have learned, and what issues you encountered. Put all the required documents into a zipped folder. Make sure you clearly list your names and student IDs in the report and the report should clearly mention which student worked on which part of the project. The late penalty is 20% per day.

Getting Started:

Java RMI: https://docs.oracle.com/javase/7/docs/technotes/guides/rmi/hello/hello-world.html
