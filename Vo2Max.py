import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


def calculate_vo2max():
    try:
        # 1. Get user input data
        gender = gender_var.get()
        weight_kg = float(weight_entry.get())
        age = float(age_entry.get())
        time_minutes = float(time_entry.get())
        heart_rate = float(hr_entry.get())

        # 2. Convert kilograms to pounds for Rockport formula
        weight_lbs = weight_kg * 2.20462

        # 3. Gender value (1 = male, 0 = female)
        gender_value = 1 if gender == "Male" else 0

        # 4. Rockport VO2max formula
        vo2max = (
            132.853
            - (0.0769 * weight_lbs)
            - (0.3877 * age)
            + (6.315 * gender_value)
            - (3.2649 * time_minutes)
            - (0.1565 * heart_rate)
        )

        # 5. Fitness evaluation
        if vo2max < 30:
            fitness_level = "Low (Needs Improvement)"
        elif 30 <= vo2max < 40:
            fitness_level = "Average / Moderate"
        elif 40 <= vo2max <= 50:
            fitness_level = "Very Good (Active Lifestyle)"
        else:
            fitness_level = "Excellent (Athlete Level)"

        # 6. Display result
        result_label.config(
            text=f"VO2max: {vo2max:.2f} ml/kg/min\nFitness Level: {fitness_level}"
        )

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid numeric values in all fields."
        )


# ─────────────────────────────────────────────
# MAIN APPLICATION WINDOW
# ─────────────────────────────────────────────

root = tk.Tk()
root.title("VO2max Calculator (Rockport Test)")
root.geometry("450x622")
root.resizable(False, False)

# GUI Style
style = ttk.Style()
style.theme_use("clam")

# Main container frame
main_frame = ttk.Frame(root, padding="50")
main_frame.pack(fill=tk.BOTH, expand=True)
#==========================================
# Logo
logo_image = Image.open("Pedro_Green_6.png")
logo_image = logo_image.resize((180, 180))

logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = ttk.Label(main_frame, image=logo_photo)
logo_label.image = logo_photo
logo_label.pack(pady=(0, 15))

#===================================================
# Title
title_label = ttk.Label(
    main_frame,
    text="VO2max Calculation",
    font=("Helvetica", 16, "bold")
)
title_label.pack(pady=(0, 20))

# 1. Gender Selection
ttk.Label(
    main_frame,
    text="Gender:",
    font=("Helvetica", 10, "bold")
).pack(anchor=tk.W, pady=2)

gender_var = tk.StringVar(value="Male")

gender_frame = ttk.Frame(main_frame)
gender_frame.pack(fill=tk.X, pady=(0, 10))

ttk.Radiobutton(
    gender_frame,
    text="Male",
    variable=gender_var,
    value="Male"
).pack(side=tk.LEFT, padx=10)

ttk.Radiobutton(
    gender_frame,
    text="Female",
    variable=gender_var,
    value="Female"
).pack(side=tk.LEFT, padx=10)

# ─────────────────────────────────────────────
# Weight + Age Row
# ─────────────────────────────────────────────

row1 = ttk.Frame(main_frame)
row1.pack(fill=tk.X, pady=(0, 10))

# Weight
weight_frame = ttk.Frame(row1)
weight_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

ttk.Label(
    weight_frame,
    text="Weight (kg):",
    font=("Helvetica", 10, "bold")
).pack(anchor=tk.W)

weight_entry = ttk.Entry(weight_frame)
weight_entry.insert(0, "75")
weight_entry.pack(fill=tk.X)

# Age
age_frame = ttk.Frame(row1)
age_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))

ttk.Label(
    age_frame,
    text="Age (years):",
    font=("Helvetica", 10, "bold")
).pack(anchor=tk.W)

age_entry = ttk.Entry(age_frame)
age_entry.insert(0, "35")
age_entry.pack(fill=tk.X)


# ─────────────────────────────────────────────
# Time + Heart Rate Row
# ─────────────────────────────────────────────

row2 = ttk.Frame(main_frame)
row2.pack(fill=tk.X, pady=(0, 15))

# Time
time_frame = ttk.Frame(row2)
time_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

ttk.Label(
    time_frame,
    text="Time (minutes):",
    font=("Helvetica", 10, "bold")
).pack(anchor=tk.W)

time_entry = ttk.Entry(time_frame)
time_entry.insert(0, "12.0")
time_entry.pack(fill=tk.X)

# Heart Rate
hr_frame = ttk.Frame(row2)
hr_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))

ttk.Label(
    hr_frame,
    text="Heart Rate (bpm):",
    font=("Helvetica", 10, "bold")
).pack(anchor=tk.W)

hr_entry = ttk.Entry(hr_frame)
hr_entry.insert(0, "132")
hr_entry.pack(fill=tk.X)
# Calculate Button
calc_button = ttk.Button(
    main_frame,
    text="Calculate VO2max",
    command=calculate_vo2max
)
calc_button.pack(fill=tk.X, ipady=5, pady=(0, 20))

## Result Label
result_label = ttk.Label(
    main_frame,
    text="First complete a 1.6 km run test \nand measure your heart rate for one minute.\n Then enter your data and press Calculate.",
    font=("Helvetica", 10, "italic"),
    justify=tk.CENTER,
    anchor=tk.CENTER,
    wraplength=380
)

result_label.pack(fill=tk.X, pady=1)
result_label.pack(fill=tk.X)

# Start application
root.mainloop()
