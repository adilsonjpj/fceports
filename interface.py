import tkinter as tk
    
window = tk.Tk()
# Título da Janela
window.title("FCEPORTS")
# Tamanho da Janela
window.geometry("800x600")
# Não deixo ela ser redimensionada
window.resizable(
    width=False,
    height=False
)

# CONFIGURANDO O GRID
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# TESTE
options = {'padx': 5, 'pady': 5}

# temperature label
frm_data_input = tk.Frame(
    master = window,
    highlightbackground="black", 
    highlightthickness=2
    )
btn_calculate = tk.Button(
    master = frm_data_input, 
    text="Calcular", 
    font=("Calibri",12,"bold")
    ).pack(padx=10, pady=10)

frm_data_input.pack(
    expand=True,
    fill='both',
    side='left'
)

# temperature label
temperature_label = tk.Label(window, text='Fahrenheit')
temperature_label.grid(row=0, column=1, columnspan=2)





# DESENVOLVEDOR DO SOFTWARE
frm_owner_info = tk.Frame(
    master = window,
    highlightbackground="black", 
    highlightthickness=2
    )
frm_owner_info.grid_columnconfigure(0, weight=1)
frm_owner_info.grid_columnconfigure(1, weight=1)
lbl_owner_name = tk.Label(
    master = frm_owner_info, 
    text="Adilson José Pereira Junior",
    highlightbackground="black", 
    highlightthickness=2
    )
lbl_owner_email = tk.Label(
    master = frm_owner_info, 
    text="adilsonjpj@outlook.com",highlightbackground="black", 
    highlightthickness=2
    )
frm_owner_info.grid(row=1, columnspan=2, sticky=tk.EW)
lbl_owner_email.grid(row=0, column=0, **options, sticky=tk.EW)
lbl_owner_name.grid(row=0, column=1, **options, columnspan=2, sticky=tk.EW)

window.mainloop()