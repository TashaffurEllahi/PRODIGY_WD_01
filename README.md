# PRODIGY_WD_01
Python-based temperature scale converter (C/F/K) with robust error handling.
# Thermal Scale Conversion Tool v1.0

A robust, production-ready Python command-line utility that accurately converts temperatures between **Celsius**, **Fahrenheit**, and **Kelvin** scales. This project was developed as a software engineering internship task to demonstrate modular code design, clean user interfaces, and defensive programming.

---

## 🚀 Features

* **Multi-Scale Conversion:** Supports seamless bidirectional conversions between Celsius, Fahrenheit, and Kelvin.
* **Robust Input Validation:** Utilizes `try-except` blocks to handle non-numeric inputs gracefully without crashing.
* **User-Friendly CLI:** Built with case-insensitive input handling (`c` vs `C`) and automatically strips accidental whitespace.
* **Precision Formatting:** Outputs all converted temperatures cleanly, rounded to exactly 2 decimal places.
* **Scientific Sanity Check:** Includes built-in threshold warnings if a user inputs a temperature below absolute zero (0 K).
* **Modular Architecture:** Designed with clean, isolated, single-responsibility functions for easy reusability.

---

## 🧮 Conversion Formulas Used

The core engine relies on standard thermodynamic conversion logic:

* **Celsius to Fahrenheit:** $F = (C \times \frac{9}{5}) + 32$
* **Celsius to Kelvin:** $K = C + 273.15$
* **Fahrenheit to Celsius:** $C = (F - 32) \times \frac{5}{9}$
* **Kelvin to Celsius:** $C = K - 273.15$

---

## 💻 How to Run

### Prerequisites
Make sure you have **Python 3.x** installed on your machine.

### Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
