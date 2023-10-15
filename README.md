# AirBnB_clone - HBnB
ALX AirBnB Clone Project with @Shannon-Kioko that simulates the core functionalities of Airbnb. It allows users to create and manage data about users, places, reviews, amenities, and more.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface](#command-line-interface)
- [Features](#features)

## Getting Started

### Prerequisites

- Python 3.6 or higher
- [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide
- Additional dependencies (See Installation section)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/AirBnB_clone.git

2. Change the repository:
   ```bash
   cd AirBnB_clone

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

### Usage
#### Command-Line Interface
To run the HolbertonBnB command-line interface:
```bash
./console.py
```
The command-line interface provides various commands to interact with the application, such as create, show, destroy, all, and more. Refer to the command's built-in help for usage instructions:
```
(hbnb) help
```

### Features
#### User Management
* Create and manage user profiles.
* Store user information, including first name, last name, email, and password.
* Unique user identification via user ID.
* Passwords are securely hashed for user privacy.

#### Object Management
* Create and manage objects like places, reviews, and amenities.
* Access object details by providing a unique object ID.
* List all objects of a specific class to view and filter data.

#### Data Persistence
* Load and save data to a JSON file for persistence.
* Automatically update the "created_at" and "updated_at" timestamps.
* Data retrieval from the JSON file on startup for continued work.
* Extensible with additional classes and features for future expansion.


   
