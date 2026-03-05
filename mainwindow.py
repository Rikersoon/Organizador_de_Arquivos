import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from pathlib import Path
from file_organizer import FileOrganizer
import darkdetect


class MainWindow(ctk.CTk):
    #Janela principal da aplicação
    
    def __init__(self):
        super().__init__()
        
        # Configurações básicas
        self.title("Organizador de Arquivos")
        self.geometry("700x600")
        self.resizable(True, True)
        
        # Define o tema de acordo com o sistema
        self._apply_system_theme()
        
        # Variáveis
        self.selected_path = ctk.StringVar()
        self.organizer = None
        
        # Cria widgets
        self._create_widgets()
        
        # Centraliza a janela
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def _apply_system_theme(self):
        #Aplica o tema de acordo com as preferências do sistema#
        try:
            is_dark = darkdetect.isDark()
            theme = "dark" if is_dark else "light"
        except:
            # Fallback para light theme se darkdetect falhar
            theme = "light"
        
        ctk.set_appearance_mode(theme)
        ctk.set_default_color_theme("blue")
    
    def _create_widgets(self):
        #Cria os widgets da interface#
        
        # Frame principal
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        title_label = ctk.CTkLabel(
            main_frame,
            text="Organizador de Arquivos",
            font=("Helvetica", 24, "bold")
        )
        title_label.pack(pady=(0, 20))
        
        # Frame de seleção de pasta
        select_frame = ctk.CTkFrame(main_frame)
        select_frame.pack(fill="x", pady=(0, 20))
        
        select_label = ctk.CTkLabel(
            select_frame,
            text="Selecione a pasta:",
            font=("Helvetica", 12)
        )
        select_label.pack(side="left", padx=(0, 10))
        
        path_entry = ctk.CTkEntry(
            select_frame,
            textvariable=self.selected_path,
            state="readonly",
            placeholder_text="Nenhuma pasta selecionada"
        )
        path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        browse_btn = ctk.CTkButton(
            select_frame,
            text="Procurar",
            command=self._select_folder,
            width=100
        )
        browse_btn.pack(side="left")
        
        # Frame de tema
        theme_frame = ctk.CTkFrame(main_frame)
        theme_frame.pack(fill="x", pady=(0, 20))
        
        theme_label = ctk.CTkLabel(
            theme_frame,
            text="Tema:",
            font=("Helvetica", 12)
        )
        theme_label.pack(side="left", padx=(0, 10))
        
        self.theme_menu = ctk.CTkOptionMenu(
            theme_frame,
            values=["Light", "Dark", "Sistema"],
            command=self._change_theme,
            width=150
        )
        self.theme_menu.pack(side="left")
        self.theme_menu.set("Sistema")
        
        # Frame de estrutura da pasta
        structure_label = ctk.CTkLabel(
            main_frame,
            text="Estrutura atual:",
            font=("Helvetica", 12, "bold")
        )
        structure_label.pack(anchor="w", pady=(20, 10))
        
        # Text widget para mostrar a estrutura
        self.structure_text = ctk.CTkTextbox(
            main_frame,
            height=200,
            state="disabled"
        )
        self.structure_text.pack(fill="both", expand=True, pady=(0, 20))
        
        # Frame de botões
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(fill="x", pady=(0, 20))
        
        refresh_btn = ctk.CTkButton(
            button_frame,
            text="Atualizar",
            command=self._show_structure,
            width=150
        )
        refresh_btn.pack(side="left", padx=(0, 10))
        
        organize_btn = ctk.CTkButton(
            button_frame,
            text="Organizar Arquivos",
            command=self._organize_files,
            width=200,
            fg_color="green",
            hover_color="darkgreen"
        )
        organize_btn.pack(side="left", padx=(0, 10))
        
        # Frame de resultados
        result_label = ctk.CTkLabel(
            main_frame,
            text="Resultados:",
            font=("Helvetica", 12, "bold")
        )
        result_label.pack(anchor="w", pady=(20, 10))
        
        # Text widget para resultados
        self.result_text = ctk.CTkTextbox(
            main_frame,
            height=150,
            state="disabled"
        )
        self.result_text.pack(fill="both", expand=True)
    
    def _select_folder(self):
        #Abre um diálogo para selecionar pasta#
        folder_path = filedialog.askdirectory(title="Selecione a pasta a organizar")
        if folder_path:
            self.selected_path.set(folder_path)
            self._show_structure()
    
    def _show_structure(self):
        #Mostra a estrutura atual da pasta#
        path = self.selected_path.get()
        if not path:
            messagebox.showwarning("Aviso", "Selecione uma pasta primeiro!")
            return
        
        self.organizer = FileOrganizer(path)
        structure = self.organizer.get_folder_structure()
        
        # Limpa o texto anterior
        self.structure_text.configure(state="normal")
        self.structure_text.delete("1.0", "end")
        
        # Exibe os arquivos não organizados
        if structure["unorganized"]:
            self.structure_text.insert("end", "Arquivos a organizar:\n")
            for file in structure["unorganized"]:
                self.structure_text.insert("end", f"  • {file}\n")
        else:
            self.structure_text.insert("end", "Nenhum arquivo para organizar!\n")
        
        self.structure_text.insert("end", "\nPastas já criadas:\n")
        
        # Exibe os arquivos organizados
        if structure["categories"]:
            for category, count in structure["categories"].items():
                self.structure_text.insert("end", f"  • {category} ({count} arquivos)\n")
        else:
            self.structure_text.insert("end", "  (Nenhuma pasta criada)\n")
        
        self.structure_text.configure(state="disabled")
    
    def _organize_files(self):
        #Organiza os arquivos
        path = self.selected_path.get()
        if not path:
            messagebox.showwarning("Aviso", "Selecione uma pasta primeiro!")
            return
        
        if not self.organizer:
            self.organizer = FileOrganizer(path)
        
        # Organiza os arquivos
        results = self.organizer.organize()
        
        # Limpa o texto anterior
        self.result_text.configure(state="normal")
        self.result_text.delete("1.0", "end")
        
        # Exibe os resultados
        self.result_text.insert("end", "Resultados da Organização:\n\n")
        self.result_text.insert("end", f"Movidos: {results['moved']}\n")
        self.result_text.insert("end", f"Ignorados: {results['skipped']}\n")
        self.result_text.insert("end", f"Erros: {results['errors']}\n\n")
        self.result_text.insert("end", "Detalhes:\n")
        self.result_text.insert("end", "-" * 50 + "\n")
        
        for detail in results["details"]:
            self.result_text.insert("end", f"{detail}\n")
        
        self.result_text.configure(state="disabled")
        
        # Atualiza a estrutura
        self._show_structure()
        
        messagebox.showinfo(
            "Sucesso",
            f"Organização concluída!\n\n"
            f"Movidos: {results['moved']}\n"
            f"Erros: {results['errors']}"
        )
    
    def _change_theme(self, choice):
        #Muda o tema da aplicação
        if choice == "Light":
            ctk.set_appearance_mode("light")
        elif choice == "Dark":
            ctk.set_appearance_mode("dark")
        else:  # Sistema
            self._apply_system_theme()
