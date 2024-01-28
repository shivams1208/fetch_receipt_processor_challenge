# Receipt Processor

## Exercise Overview

Build a webservice that fulfils the documented API. A formal definition is provided in the api.yml file.

### Summary

#### Endpoint: Process Receipts
```
Path: `/receipts/process`
Method: POST
Payload: Receipt JSON
Response: JSON containing an id for the receipt.
```

#### Endpoint: Get Points
```
Path: `/receipts/{id}/points`
Method: GET
Response: A JSON object containing the number of points awarded.
```

##### Point Rules

These rules collectively define how many points should be awarded to a receipt.

* One point for every alphanumeric character in the retailer name.
* 50 points if the total is a round dollar amount with no cents.
* 25 points if the total is a multiple of 0.25.
* 5 points for every two items on the receipt.
* If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
* 6 points if the day in the purchase date is odd.
* 10 points if the time of purchase is after 2:00pm and before 4:00pm.

## Solution Description

The Receipt Processor is a package designed to handle the processing and analysis of receipts. It offers a convenient and efficient way to calculate points based on specific purchasing behaviors and criteria.

### Key Features

1. Receipt Validation:

   * Validates each receipt against a data schema, patterns and other rules defined in `yml`, ensuring data integrity.
   * Checks for correct retailer name format, purchase date and time, total amount, and item validity.
  > **Assumption: Even though the Regex for `retailer` implied that spaces are not allowed but `M&M Corner Market` example in README suggested otherwise. Therefore, I assumed having spaces in retailer's name is a valid name.**
  
1. Points Calculation:
   * Awards points based on various criteria, including the alphanumeric characters in the retailer's name, total purchase amount, purchase time, and individual item details.

2. API Integration:
   * Provides a Flask-based REST API for easy integration with front-end systems or other applications.
   * Supports POST requests for receipt processing and GET requests for retrieving calculated points. 
  
3. Scalable and Modular Design:
   * Built using Python's Pydantic models for data validation and serialization, ensuring robustness and scalability.
   * Modular design allows easy extension or modification to suit specific business requirements.
  
4. Data Storage:
   * Receipt data is temporarily stored in-memory, making it fast and efficient for smaller datasets.
   * The design allows for easy adaptation to more persistent storage solutions if needed.

## Installation
```bash
git clone https://github.com/shivams1208/fetch_receipt_processor_challenge.git

cd fetch_rewards_SRE_take_home-main
```

## Usage
For running this receipt processor, Docker, empty port `5001` and `curl` commands is required. Therefore, first make sure you have docker installed in your system and if not you can get the docker from [here](https://docs.docker.com/get-docker/).

> Before running given below commands, make sure that port `5001` is not running any other processes or if you prefer, you can use another port in the command.

### Steps
1. Build the docker:

   `docker build -t receipt_processor .`
2. Run the docker:

   `docker run -p 5001:5000 --rm -it receipt_processor`
3. Although there are many ways you can execute `GET` and `POST` commands but this one requires no additional installation. 
Following are `curl` commands for running the endpoints. Here, replace `localhost` with IP address of your local machine and ensure it is correct.  (**I have included steps to find `local` at the last of this README.**)

   > If you are running Docker on the same machine where you are accessing the application, then you can simply use `localhost`.
   But if you need to access the Dockerized application from a different machine on the same network, then you'll need to find the local IP address you find with the steps mentioned in Additional Notes.


   1. `curl -X POST http://localhost:5001/receipts/process -H "Content-Type: application/json" -d '{"key":"value"}'`
      1. Here `{"key":"value"}` is receipt JSON.
   2. `curl http://localhost:5001/receipts/<receipt_id>/points`
      1. Here `<receipt_id>` is a variable part of URL and stands for ID of a receipt whose points needs to be calculated.


## Testing

The package includes comprehensive unit tests to ensure the functionality's reliability and correctness. The unit tests are included in src/tests directory and segregated into different files for each class.

Docker Command to run Tests file:
`docker run -it receipt_processor /bin/bash run_tests.sh`

## Additional Notes

### Find `localhost` IP address

#### Windows

1. **Using Command Prompt**:
   - Open Command Prompt.
   - Type `ipconfig` and press Enter.
   - Look for the “IPv4 Address” under your active network connection. This is your local IP address.

2. **Using PowerShell**:
   - Open PowerShell.
   - Type `Get-NetIPConfiguration` and press Enter.
   - Find your active network adapter and note the IPv4 address.

#### macOS

1. **Using Terminal**:
   - Open Terminal.
   - Type `ifconfig` and press Enter.
   - Look for `en0` or `en1` section and find the `inet` line, which will give your IP address.

### Linux

1. **Using Terminal**:
   - Open Terminal.
   - Type `hostname -I` or `ip addr show` and press Enter.
   - Look for the IP address listed under your active network interface (usually `eth0` for wired or `wlan0` for wireless).