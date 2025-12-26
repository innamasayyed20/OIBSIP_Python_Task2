import tkinter as tk
from tkinter import messagebox

# ------------------ App State ------------------
dark_mode = False

# ------------------ BMI Logic ------------------
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError
        bmi = round(weight / (height ** 2), 2)
        if bmi < 18.5:
            category, tip, scale, color = "Underweight", "Need to gain weight. Consult a pro.", "BMI Scale: [■□□□□]", "#f1c40f"
        elif bmi < 25:
            category, tip, scale, color = "Normal", "Healthy range. Keep it up!", "BMI Scale: [■■■□□]", "#2ecc71"
        elif bmi < 30:
            category, tip, scale, color = "Overweight", "Consider diet and exercise.", "BMI Scale: [■■■■□]", "#e67e22"
        else:
            category, tip, scale, color = "Obese", "Health risk! Seek medical advice.", "BMI Scale: [■■■■■]", "#e74c3c"

        result_label.config(text=f"BMI Score: {bmi}", fg=color)
        category_label.config(text=category, fg=color)
        tip_label.config(text=tip)
        scale_label.config(text=scale, fg=color)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid positive numbers.")

def reset_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="BMI Score: --", fg=current_fg)
    category_label.config(text="Category: --", fg=current_fg)
    tip_label.config(text="")
    scale_label.config(text="")

def toggle_theme():
    global dark_mode, current_bg, current_fg
    dark_mode = not dark_mode
    if dark_mode:
        current_bg, current_fg, card_bg, entry_bg = "#0F172A", "#F8FAFC", "#1E293B", "#334155"
        theme_btn.config(text="☀️ Light Mode", bg="#334155", fg="white")
    else:
        current_bg, current_fg, card_bg, entry_bg = "#F1F5F9", "#1E293B", "#FFFFFF", "#F8FAFC"
        theme_btn.config(text="🌙 Dark Mode", bg="#E2E8F0", fg="black")
    root.config(bg=current_bg)
    main_card.config(bg=card_bg)
    header_section.config(bg=card_bg)
    results_section.config(bg=card_bg)
    btn_container.config(bg=card_bg)
    secondary_btns.config(bg=card_bg)
    for widget in header_section.winfo_children():
        if isinstance(widget, tk.Label): widget.config(bg=card_bg, fg=current_fg)
    weight_label.config(bg=card_bg, fg=current_fg)
    height_label.config(bg=card_bg, fg=current_fg)
    weight_entry.config(bg=entry_bg, fg=current_fg, insertbackground=current_fg)
    height_entry.config(bg=entry_bg, fg=current_fg, insertbackground=current_fg)
    tip_label.config(bg=card_bg, fg="#94A3B8" if dark_mode else "#64748B")
    result_label.config(bg=card_bg, fg=current_fg if "Score: --" in result_label.cget("text") else result_label.cget("fg"))
    category_label.config(bg=card_bg, fg=current_fg if "Category: --" in category_label.cget("text") else category_label.cget("fg"))
    scale_label.config(bg=card_bg)

# ------------------ UI Setup ------------------
root = tk.Tk()
root.title("Modern BMI Calculator")
root.geometry("850x750") # Wide window, medium height
current_bg = "#F1F5F9"
current_fg = "#1E293B"
root.config(bg=current_bg)

# Main Card - Medium padding (pady=25) and much wider (padx=80)
main_card = tk.Frame(root, bg="white", padx=80, pady=25, highlightthickness=1, highlightbackground="#E2E8F0")
main_card.place(relx=0.5, rely=0.5, anchor="center")

# Header
header_section = tk.Frame(main_card, bg="white")
header_section.pack(fill=tk.X)
tk.Label(header_section, text="BMI Tracker", font=("Segoe UI", 28, "bold"), bg="white", fg="#3B82F6").pack()
tk.Label(header_section, text="Check your health status instantly", font=("Segoe UI", 11), bg="white", fg="#64748B").pack(pady=(2, 15))

# Inputs
weight_label = tk.Label(main_card, text="Weight (kg)", font=("Segoe UI", 12, "bold"), bg="white", fg=current_fg)
weight_label.pack(anchor="w")
weight_entry = tk.Entry(main_card, font=("Segoe UI", 16), justify="center", bd=0, highlightthickness=1, highlightbackground="#CBD5E1", bg="#F8FAFC")
weight_entry.pack(fill=tk.X, pady=(2, 15), ipady=8)

height_label = tk.Label(main_card, text="Height (m)", font=("Segoe UI", 12, "bold"), bg="white", fg=current_fg)
height_label.pack(anchor="w")
height_entry = tk.Entry(main_card, font=("Segoe UI", 16), justify="center", bd=0, highlightthickness=1, highlightbackground="#CBD5E1", bg="#F8FAFC")
height_entry.pack(fill=tk.X, pady=(2, 20), ipady=8)

# Buttons
btn_container = tk.Frame(main_card, bg="white")
btn_container.pack(fill=tk.X)
calc_btn = tk.Button(btn_container, text="Calculate Now", font=("Segoe UI", 14, "bold"), bg="#3B82F6", fg="white", 
                    relief="flat", command=calculate_bmi, cursor="hand2")
calc_btn.pack(fill=tk.X, ipady=10, pady=5)

secondary_btns = tk.Frame(btn_container, bg="white")
secondary_btns.pack(fill=tk.X, pady=5)
reset_btn = tk.Button(secondary_btns, text="Reset", font=("Segoe UI", 11), bg="#94A3B8", fg="white", relief="flat", command=reset_fields, width=15)
reset_btn.pack(side=tk.LEFT, padx=(0, 5), ipady=6)
exit_btn = tk.Button(secondary_btns, text="Exit App", font=("Segoe UI", 11), bg="#EF4444", fg="white", relief="flat", command=root.destroy, width=15)
exit_btn.pack(side=tk.RIGHT, padx=(5, 0), ipady=6)

# Results Section
results_section = tk.Frame(main_card, bg="white", pady=10)
results_section.pack(fill=tk.X)
result_label = tk.Label(results_section, text="BMI Score: --", font=("Segoe UI", 22, "bold"), bg="white", fg=current_fg)
result_label.pack()
category_label = tk.Label(results_section, text="Category: --", font=("Segoe UI", 15), bg="white", fg=current_fg)
category_label.pack()
scale_label = tk.Label(results_section, text="", font=("Consolas", 14), bg="white")
scale_label.pack(pady=5)
tip_label = tk.Label(results_section, text="", font=("Segoe UI", 10, "italic"), bg="white", fg="#64748B", wraplength=400)
tip_label.pack(pady=5)

# Theme Toggle
theme_btn = tk.Button(root, text="🌙 Dark Mode", font=("Segoe UI", 10), command=toggle_theme, relief="flat", padx=12, pady=5)
theme_btn.place(relx=0.98, rely=0.02, anchor="ne")

root.bind("<Return>", lambda e: calculate_bmi())
root.mainloop()