# 🎰 Python Slot Machine Game

## 📌 Description

This is a simple **command-line slot machine game** built using Python.
Players can deposit money, choose the number of betting lines, place bets, and spin the slot machine to try their luck.

The game simulates a real slot machine with different symbols, values, and winning logic.

---

## 🚀 Features

* Deposit system 💰
* Multiple betting lines (1–3)
* Custom bet per line
* Random slot spin generator 🎲
* Winning calculation based on matching symbols
* Balance tracking system

---

## 🧠 How the Game Works

* The slot machine is a **3x3 grid**.
* Each column is randomly generated.
* Different symbols have:

  * **Different frequencies**
  * **Different values**
* If all symbols in a selected row match → you win 🎉

---

## 🎯 Symbols & Values

| Symbol | Count | Value |
| ------ | ----- | ----- |
| A      | 2     | 5     |
| B      | 4     | 4     |
| C      | 6     | 3     |
| D      | 8     | 2     |

* Higher value symbols appear less frequently.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/slot-machine-python.git
cd slot-machine-python
```

### 2. Run the program

```bash
python main.py
```

---

## ▶️ Usage

1. Enter deposit amount
2. Choose number of lines (1–3)
3. Enter bet per line
4. Spin the slot machine 🎰
5. Check if you win or lose

---

## 📂 Project Structure

```
slot-machine/
│── main.py          # Main game logic
│── README.md        # Project documentation
```

---

## 🛠️ Technologies Used

* Python 3
* Random module

---

## 📌 Example Output

```
A | B | C
D | A | C
B | B | B

You won $12.
You won on lines: 2
```

---

## ⚠️ Notes

* This is a beginner-friendly project for learning:

  * Functions
  * Loops
  * Conditionals
  * Dictionaries
* No external libraries required.

---

## 👨‍💻 Author

**Naim Islam**

---

## ⭐ Future Improvements

* Add GUI (Tkinter / PyGame)
* Add sound effects 🔊
* Add bonus rounds
* Improve UI/UX

---

## 📜 License

This project is open-source and free to use.
