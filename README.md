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

Include any relevant screenshots here to visually demonstrate the functionality of the blockchain display.

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

![](/Users/peterstoyanov/Desktop/Screenshot 2024-04-09 at 10.49.52.png)