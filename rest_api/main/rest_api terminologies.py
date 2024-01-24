'''
-All 6 https methods:
In the context of RESTful APIs, there are six primary HTTP methods (also known as HTTP verbs) that are commonly used to perform different actions on resources. These methods are used to interact with resources (data entities) in a stateless manner. Here are explanations for each of the six HTTP methods:

GET:

Purpose: Retrieve data from a specified resource.
Usage: Used to request data from a specified resource. The request parameters, if any, are included in the URL. It should not have a side effect on the data.

POST:

Purpose: Submit data to be processed to a specified resource.
Usage: Used to send data to the server to create a new resource. The data is typically included in the request body. It may have a side effect on the data, such as creating a new record.

PUT:

Purpose: Update a specified resource or create it if it does not exist.
Usage: Used to update the entire resource with the provided data. If the resource does not exist, it may create a new one. It should be idempotent, meaning repeated identical requests will have the same effect as a single request.

PATCH:

Purpose: Update a specified resource, partially modifying its data.
Usage: Similar to PUT, but used for partial updates. It allows you to update specific fields of a resource without affecting the rest. It should also be idempotent.

DELETE:

Purpose: Delete a specified resource.
Usage: Used to request the removal of a resource. After a successful deletion, the server should respond with a 204 (No Content) status code. It should be idempotent.

OPTIONS:

Purpose: Get information about the communication options available for a specified resource.
Usage: Used to describe the communication options for the target resource. It is often used by browsers to check what methods are allowed for a resource at a given URL.
These HTTP methods, when used in combination with URLs, form the basis of how RESTful APIs handle operations on resources. For example, when you perform a CRUD (Create, Read, Update, Delete) operation on a resource, you might use POST, GET, PUT, and DELETE requests, respectively.

It's important to design your RESTful API routes and endpoints in a way that aligns with these HTTP methods to follow RESTful principles. Each method has its specific purpose and is designed to perform a specific type of operation on the server.
'''

'''
-Allow: GET, POST, HEAD, OPTIONS:
The message you are seeing, "Allow: GET, POST, HEAD, OPTIONS," is part of the HTTP response headers returned by the server. These headers provide information about what HTTP methods are allowed for a particular resource. Let's break down what each part of the message means:

Allow: This is an HTTP response header that indicates the set of HTTP methods that are supported by the server for the requested resource.

GET, POST, HEAD, OPTIONS: These are the HTTP methods that the server allows for the specified resource.

GET: Allows retrieving data from the resource.

POST: Allows submitting data to create a new resource or process data on the server.

HEAD: Similar to GET but returns only the headers, not the actual data.

OPTIONS: Describes the communication options for the target resource. It is often used by clients (e.g., browsers) to check what methods are allowed for a resource at a given URL.

In the context of your REST API, this response header indicates that the server allows the client to use the mentioned HTTP methods (GET, POST, HEAD, OPTIONS) when interacting with the resource.

{
        "id": 2,
        "first_name": "John",
        "last_name": "Smitth",
        "email": "john1123@gmail.com",
        "password": "admin"
    }
    
It looks like a JSON representation of an Employee instance created on the server. The server responds with the newly created data, including an id field, which is likely assigned by the server to uniquely identify this resource.
'''