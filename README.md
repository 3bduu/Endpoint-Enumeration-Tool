# Simple Endpoint Checker

This Python script checks the availability of different endpoints on a specified URL target.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/3bduu/Endpoint-Enumeration-Tool.git
   
2. Navigate to the project directory:

   ```bash
   cd Endpoint-Enumeration-Tool
   
4. Run the script:
   
   ```bash
   python3 endenum.py
   
  Follow the on-screen instructions to input the target URL and observe the results.
  
# Features

  • Reads a list of endpoints from a file (wordlist.txt).
  
  • Sends HTTP GET requests to each endpoint.
  
  • Checks and prints the content if the status code is 200, otherwise prints an error message.

# Example

```bash
  URL target: https://example.com
------------------------------------------------------------START-------------------------------------------------------------
-> The 'endpoint1' Content : <content1>
-> The 'endpoint2' is not Working 'Status code: 404'
...
------------------------------------------------------------FINISH-------------------------------------------------------------
