**Getting Started**

This repository provides a Python script (app.py) for interacting with a MongoDB database using the pymongo library.

**Prerequisites**

- Python 3.x (download from https://www.python.org/downloads/)
- pipenv (package installer) - Install using `pip install pipenv`

**Installation**

1. Clone this repository:
    
    Bash
    
    `git clone https://github.com/AlanRMA/PyMongoRunner`
    
    `cd PyMongoRunner`
    
    
2. Install dependencies using pipenv:
    
    Bash
    
    `pipenv install`
    
    
    This will create a virtual environment and install the required packages, including pymongo.
    

**Configuration**

1. Create a file named `.env` in the root directory of your project (**exclude this file from version control**). This file stores your MongoDB connection string securely:
    
    `MONGO_CONNECTION_STRING="your_actual_mongodb_connection_string"`
    
    Replace `"your_actual_mongodb_connection_string"` with the appropriate connection string for your MongoDB database. You can find instructions on obtaining your connection string in your MongoDB provider's documentation.
    

**Usage**

1. **Explore the Code:**
    - Open the `app.py` file to see the available functions for interacting with your MongoDB database.
    - These functions likely handle operations such as creating collections, inserting data, querying documents and deleting data.
2. **Create Tasks:**
    - **(Optional):** If your script uses a queue or similar mechanism for executing commands, modify the `__main__` function in `app.py` to enqueue the commands you want to run against MongoDB.
3. **Run the Script:**
    

    1. `pipenv shell`

    2. `pipenv install pymongo`
    
    3. `python app.py`
    

This will execute the script and interact with your MongoDB database based on the defined commands.
