# VO2Max_Calculator
Vo2Max CALCULATOR FOR RUNNING ATHLETS


# 🏃‍♂️ VO2max Calculator (Rockport 1-Mile Test)

A lightweight Python desktop application to estimate maximal oxygen uptake (**VO2max**) using the scientifically validated **Rockport 1-Mile Test** formula.

## 📝 Overview

This app features a clean graphical user interface (GUI) built with `tkinter`. Users input their core metrics to instantly view their VO2max score and fitness classification.

### 🧬 Physiological Logic
The algorithm accounts for natural cardiovascular aging. As age increases, standard markers like Maximum Heart Rate (Max HR) and stroke volume decrease. Therefore, an older individual achieving the same time and heart rate as a younger person reflects a higher relative fitness level, which this formula accurately calculates.

## 🚀 Features

- 💻 **Native GUI:** Powered by Python's built-in `tkinter` library (no external installations required).
- ⚡ **Real-Time Calculation:** Instant results and fitness tiering at the click of a button.
- 🛡️ **Input Validation:** Built-in error handling to prevent crashes from empty or invalid data.

## 🛠️ Quick Start

### Run from Source
Ensure you have Python 3 installed. No external packages are needed.

```bash
# Clone the repository
git clone [https://github.com/YOUR-USERNAME/vo2max-calculator.git](https://github.com/YOUR-USERNAME/vo2max-calculator.git)
cd vo2max-calculator

# Run the app
python vo2max_app.py
