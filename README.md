# Simple Calculator

This is a simple calculator application built using Python's `tkinter` library for graphical user interface (GUI). It supports basic arithmetic operations including addition, subtraction, multiplication, and division, along with the functionality to clear the display and show results.

## Features

- **Basic Operations**: Perform addition, subtraction, multiplication, and division.
- **Clear Button**: Clear the current input.
- **Equals Button**: Evaluate the expression and show the result.
- **Responsive Layout**: Adjusts to different screen sizes using grid layout.
- **Error Handling**: Displays "Error" if an invalid calculation is attempted.

## Requirements

To run this program, you need to have Python installed on your system along with the `tkinter` library (which comes pre-installed with Python by default).

- Python 3.x
- tkinter (comes with Python)

## Installation

1. Install Python 3.x from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. The `tkinter` library should already be included with your Python installation.
3. Download the calculator code (e.g., `calculator.py`) to your local machine.

## Usage

To run the calculator:

1. Open your terminal or command prompt.
2. Navigate to the directory where the `calculator.py` file is located.
3. Run the program using Python by typing:


4. The calculator window will appear, and you can start performing calculations.

## How to Use

- Click on the number buttons (0-9) to enter numbers.
- Click on the operation buttons (+, -, *, /) to perform arithmetic operations.
- Click `C` to clear the current input.
- Click `=` to calculate the result.

## Code Structure

- **GUI Layout**: The application uses a grid layout where the entry widget (for display) spans across four columns. Each button is placed in the grid with proper padding for a neat appearance.
- **Functions**:
- `button_click(number)`: Updates the entry field with the clicked number.
- `clear_entry()`: Clears the entry field.
- `calculate()`: Evaluates the expression entered in the entry field and shows the result. If there is an error, it displays "Error".

## Example

Here is a simple sequence of operations:

1. Press `7`, `+`, `3`, `=`.
2. The result displayed will be `10`.

## screenshots
![Screenshot 2024-11-25 215146](https://github.com/user-attachments/assets/80917622-b367-4f78-ab5d-1cc5e70d1faf)
![Screenshot 2024-11-25 215210](https://github.com/user-attachments/assets/c98a46ae-859c-4d6a-9c0c-1fb7d16e5618)
![Screenshot 2024-11-25 215218](https://github.com/user-attachments/assets/69f61d57-773b-47d0-bc27-30887d0ec04d)
