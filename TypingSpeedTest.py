import customtkinter

screen = customtkinter.CTk()
screen.geometry("800x500")
screen.title("Typing Speed Test GUI")

def button_click():
    print("Button clicked")

text = customtkinter.CTkLabel(screen, text="Will add everything that is to be typed will be placed here.Hello chirag this side", bg_color="white", font=("Arial", 25), wraplength=800)
text.grid(row=0, column=0, columnspan=3)

type_text = customtkinter.CTkTextbox(screen,width=800, height=5, )
type_text.grid(column=0, row=2, columnspan=3)

button = customtkinter.CTkButton(screen, text="clickMe", command=button_click)
button.grid(row=3, column=1, padx=20, pady=20, sticky="ew")
screen.mainloop()