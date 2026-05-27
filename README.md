📈 Stock Portfolio Tracker

A simple Python-based stock portfolio tracker that allows users to calculate their total investment using predefined stock prices.

📌 Project Description

Stock Portfolio Tracker is a beginner-friendly Python project that runs in the terminal. Users can enter stock symbols and quantities, and the program calculates the total investment value based on hardcoded stock prices. The portfolio details can also be saved into a text file for future reference.

✨ Features
📊 Predefined Stock Prices -- Supports AAPL, TSLA, GOOGL, and MSFT
➕ Multiple Stock Entries --	Add multiple stocks and quantities
✅ Input Validation	-- Rejects invalid stock names and incorrect quantity inputs
💰 Total Investment Calculator	-- Automatically calculates portfolio value
📁 File Saving Option	-- Save portfolio details into portfolio.txt
🔄 User-Friendly Interface	-- Simple terminal-based interaction
🗂️ Folder Structure
StockPortfolioTracker/
│
├── main.py            # Main source code
├── README.md          # Project documentation
└── portfolio.txt      # Saved portfolio output file
🛠️ Technologies & Key Concepts
Concept	Where Used
Dictionaries	Store stock prices and portfolio data
Functions	Modular program structure
Loops	User input handling
Conditional Statements	Input validation and logic
Exception Handling	Handling invalid quantity inputs
File Handling	Saving portfolio to text file
Strings	User input formatting and display
🚀 How to Run
# Navigate into the project folder
cd StockPortfolioTracker

# Run the program
python main.py

Use python3 main.py on Linux/Mac if required.

🖥️ Sample Console Output
Welcome to the Stock Portfolio Tracker!

Enter stock name (or type 'done' to finish): AAPL
Enter quantity of AAPL: 5

Enter stock name (or type 'done' to finish): TSLA
Enter quantity of TSLA: 2

Enter stock name (or type 'done' to finish): done

Your Portfolio:
AAPL: 5 shares @ $180 each
TSLA: 2 shares @ $250 each

Total Investment: $1400

Do you want to save this portfolio? (yes/no): yes

Portfolio saved to portfolio.txt
📁 Example Saved File
Stock Portfolio:

AAPL: 5 shares @ $180 each
TSLA: 2 shares @ $250 each

Total Investment: $1400
📚 Learning Concepts

This project helps beginners understand:

Python Dictionaries
Functions
Loops & Conditionals
Exception Handling
File Operations
User Input Validation
🚀 Future Improvements
Add real-time stock prices using APIs
Create graphical charts for investment analysis
Add profit/loss calculation
Store data using databases
Build a GUI version using Tkinter
👩‍💻 Author

Monika M
Python Programming Intern

📄 License

Open-source — free to use for educational purposes.
