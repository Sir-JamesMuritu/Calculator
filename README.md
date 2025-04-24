# Basic Calculator

A simple Python program that allows users to perform basic arithmetic operations (addition, subtraction, multiplication, and division) interactively via the command line.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Description

This Basic Calculator program is a command-line tool written in Python. It prompts the user to enter two numbers and select an arithmetic operation, then computes and displays the result. It includes input validation and error handling for non-numeric input and division by zero.

## Features

- Addition, subtraction, multiplication, and division
- Interactive command-line interface
- Input validation for numeric values
- Graceful handling of division by zero
- Option to perform multiple calculations or quit

## Requirements

- Python 3.6 or higher

## Installation

1. **Clone the repository** (or download the `calculator.py` file):
   ```bash
   git clone https://github.com/Sir-JamesMuritu/Calculator.git
   cd basic-calculator
   ```

2. **(Optional) Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **No external dependencies** are required beyond the Python standard library.

## Usage

Run the program using the Python interpreter:

```bash
python calculator.py
```

Follow the on-screen prompts:

1. Enter the first number (or type `q` to quit).
2. Enter the second number.
3. Choose an operation: `+`, `-`, `*`, or `/`.
4. View the result, then repeat or quit.

## Examples

```text
Welcome to the Basic Calculator!
Enter the first number (or 'q' to quit): 10
Enter the second number: 5
Choose an operation (+, -, *, /): +

🎉  10.0 + 5.0 = 15.0

Enter the first number (or 'q' to quit): 9
Enter the second number: 0
Choose an operation (+, -, *, /): /

⚠️  Cannot divide by zero.

Enter the first number (or 'q' to quit): q
Goodbye!
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or bug fixes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

