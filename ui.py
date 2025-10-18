import tkinter as tk
import core 

def main() -> None:
    app = tk.Tk()
    app.title("Calculator")
    app.config(bg="black")
    app.geometry("400x300")

    equation = tk.StringVar(value="")

    label = tk.Label(app, text="Entry", font=("Times New Roman", 12), bg="lightgrey")
    label.grid(row=0, column=0, columnspan=4, sticky="ew", padx=4, pady=4)

    expression_box = tk.Entry(app, textvariable=equation)
    expression_box.grid(row=1, column=0, columnspan=4, ipadx=70, padx=4, pady=4, sticky="ew")

    history_label = tk.Label(app, text="", fg="black", bg="lightgrey",
                             font=("Times New Roman", 10), justify="left", anchor="w")
    history_label.grid(row=7, column=0, columnspan=4, sticky="ew", padx=4, pady=4)

    def refresh() -> None:
        """Sync GUI with core state."""
        equation.set(core.expression)
        history_label.config(text=core.history_text())

    # --- Numbers/Buttons wrappers---
    def on_press(ch: str | int) -> None:
        core.press(ch)
        refresh()

    def on_decimal() -> None:
        core.press_decimal()
        refresh()

    def on_back() -> None:
        core.press_back()
        refresh()

    def on_equal() -> None:
        result = core.equalpress() 
        equation.set(result if result != "ERROR" else " ERROR ")
        refresh()

    def on_clear() -> None:
        core.clear()
        refresh()

    def on_clear_history() -> None:
        core.clear_history()
        refresh()

    # --- Numbers ---
    btns = [
        ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
        ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
        ("7", 4, 0), ("8", 4, 1), ("9", 4, 2),
        ("0", 5, 0),
    ]
    for t, r, c in btns:
        tk.Button(app, text=f" {t} ", fg="black", bg="white",
                  command=lambda x=t: on_press(x), height=1, width=7).grid(row=r, column=c, padx=2, pady=2)

    # --- Operators ---
    tk.Button(app, text=' + ', fg="black", bg="lightblue",
              command=lambda: on_press("+"), height=1, width=7).grid(row=2, column=3, padx=2, pady=2)
    tk.Button(app, text=' - ', fg="black", bg="lightblue",
              command=lambda: on_press("-"), height=1, width=7).grid(row=3, column=3, padx=2, pady=2)
    tk.Button(app, text=' * ', fg="black", bg="lightblue",
              command=lambda: on_press("*"), height=1, width=7).grid(row=4, column=3, padx=2, pady=2)
    tk.Button(app, text=' / ', fg="black", bg="lightblue",
              command=lambda: on_press("/"), height=1, width=7).grid(row=5, column=3, padx=2, pady=2)

    # --- Special Buttons ---
    tk.Button(app, text=' = ', fg="black", bg="lightblue",
              command=on_equal, height=1, width=7).grid(row=5, column=2, padx=2, pady=2)
    tk.Button(app, text='AC', fg="black", bg="yellow",
              command=on_clear, height=1, width=7).grid(row=5, column=1, padx=2, pady=2)
    tk.Button(app, text='.', fg="black", bg="lightblue",
              command=on_decimal, height=1, width=7).grid(row=6, column=0, padx=2, pady=2)
    tk.Button(app, text='←', fg="black", bg="lightblue",
              command=on_back, height=1, width=7).grid(row=6, column=1, padx=2, pady=2)
    tk.Button(app, text="Delete History", fg="black", bg="lightblue",
              command=on_clear_history, height=1, width=28).grid(row=8, column=0, columnspan=4, padx=2, pady=4, sticky="ew")

    for c in range(4):
        app.grid_columnconfigure(c, weight=1)

    refresh()
    app.mainloop()


if __name__ == "__main__":
    main()
