# Simple Blockchain Implementation with Django in Python 3.12

This project provides a simple implementation of a blockchain using Django, demonstrating the creation, display, and validation of a basic blockchain.

## Overview

The code consists of a Django app named `dlt` (Distributed Ledger Technology) that includes the following components:
- `blockchain.py`: Defines the `Block` and `Blockchain` classes for the blockchain implementation.
- `views.py`: Contains Django views to interact with the blockchain, including displaying and validating the chain.
- `urls.py`: Defines URL patterns to map views to specific URLs.
- `templates/chain.html`: A Django template to display the blockchain data.

## Functionality

The `blockchain.py` file contains the core logic for creating and managing the blockchain. It includes classes for `Block` and `Blockchain`, along with methods for adding blocks, validating the chain, and displaying the chain data.

The `DisplayChainView` in `views.py` renders the `chain.html` template to display the blockchain data, while the `ValidateChainView` validates the integrity of the blockchain.

## Usage

To use this project:
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Django development server using `python manage.py runserver`.
4. Access the `display_chain` and `validate_chain` URLs to interact with the blockchain.



## Screenshots
![Screenshot 2024-04-12 112946](https://github.com/PeterStoyanov83/DLT/assets/108938447/ad0fbc83-f315-4dab-92f2-eb98d9451f5b)



## Contributing


