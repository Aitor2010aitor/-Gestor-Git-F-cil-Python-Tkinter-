import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

# Variable global para almacenar el repositorio actual
REPOSITORIO_ACTUAL = ""

def pedir_link_repositorio():
    """Ventana inicial para introducir el link del repositorio."""
    def guardar_link():
        global REPOSITORIO_ACTUAL
        link = entry_link.get().strip()
        if not link:
            messagebox.showerror("Error", "Debes introducir un enlace de GitHub válido.")
            return
        REPOSITORIO_ACTUAL = link
        win_link.destroy()
        abrir_ventana_principal()

    win_link = tk.Tk()
    win_link.title("Configurar Repositorio - Gestor Git Fácil")
    win_link.geometry("450x200")
    
    frame = ttk.Frame(win_link, padding="20")
    frame.pack(fill="both", expand=True)
    
    ttk.Label(frame, text="¡Bienvenido! Introduce el link de tu repositorio de GitHub:", font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 5))
    ttk.Label(frame, text="Ejemplo: https://github.com/tu-usuario/tu-repositorio", font=("Arial", 8), foreground="gray").pack(anchor="w", pady=(0, 10))
    
    global entry_link
    entry_link = ttk.Entry(frame, width=50)
    entry_link.pack(fill="x", pady=(0, 15))
    
    btn_continuar = ttk.Button(frame, text="Continuar al Gestor ➔", command=guardar_link)
    btn_continuar.pack(fill="x")
    
    win_link.mainloop()

def abrir_ventana_principal():
    """Ventana principal categorizada."""
    root = tk.Tk()
    root.title(f"Gestor Git Fácil - {REPOSITORIO_ACTUAL}")
    root.geometry("520x480")
    
    frame = ttk.Frame(root, padding="15")
    frame.pack(fill="both", expand=True)
    
    # Mostrar el repositorio actual arriba
    lbl_repo = ttk.Label(frame, text=f"📂 Repositorio: {REPOSITORIO_ACTUAL}", font=("Arial", 9, "italic"), foreground="blue")
    lbl_repo.pack(anchor="w", pady=(0, 10))

    # --- CATEGORÍA 1: Publicar y Versiones ---
    cat1_frame = ttk.LabelFrame(frame, text=" 🚀 Categoría 1: Publicar y Versiones ", padding="10")
    cat1_frame.pack(fill="x", pady=(0, 10))

    ttk.Label(cat1_frame, text="Ruta de la carpeta local:").pack(anchor="w")
    global entry_ruta
    entry_ruta = ttk.Entry(cat1_frame, width=50)
    entry_ruta.pack(fill="x", pady=(0, 5))

    ttk.Label(cat1_frame, text="Mensaje del cambio (Commit):").pack(anchor="w")
    global entry_mensaje
    entry_mensaje = ttk.Entry(cat1_frame, width=50)
    entry_mensaje.pack(fill="x", pady=(0, 5))

    ttk.Label(cat1_frame, text="Nombre de la Versión / Rama (ej. VERSION-1.0):").pack(anchor="w")
    global entry_version
    entry_version = ttk.Entry(cat1_frame, width=50)
    entry_version.pack(fill="x", pady=(0, 8))

    btn_subir = ttk.Button(cat1_frame, text="Guardar y Crear Rama de Versión", command=ejecutar_subida)
    btn_subir.pack(fill="x")

    # --- CATEGORÍA 2: Enlaces y Web ---
    cat2_frame = ttk.LabelFrame(frame, text=" 🌐 Categoría 2: Enlaces y GitHub ", padding="10")
    cat2_frame.pack(fill="x", pady=(0, 10))

    btn_link = ttk.Button(cat2_frame, text="🔗 Abrir este Repositorio en la Web", command=lambda: webbrowser.open(REPOSITORIO_ACTUAL))
    btn_link.pack(fill="x", pady=(0, 5))

    btn_doc = ttk.Button(cat2_frame, text="📖 Ver Documentación / Guía de Ayuda", command=mostrar_documentacion)
    btn_doc.pack(fill="x")

    root.mainloop()

def ejecutar_subida():
    ruta = entry_ruta.get().strip('"')
    mensaje = entry_mensaje.get()
    version = entry_version.get().strip()

    if not ruta or not os.path.exists(ruta):
        messagebox.showerror("Error", "La ruta de la carpeta no es válida.")
        return

    if not mensaje:
        messagebox.showerror("Error", "Escribe un mensaje para el commit.")
        return

    try:
        os.chdir(ruta)
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run(["git", "commit", "-m", mensaje])

        if version:
            # Crear rama local
            subprocess.run(["git", "checkout", "-B", version], check=True)
            # Subir especificando refs/heads/ para evitar conflictos
            subprocess.run(["git", "push", "-u", "origin", f"refs/heads/{version}:{version}", "--force"], check=True)

        # Volver a la rama de respaldo codecord
        subprocess.run(["git", "checkout", "codecord"], check=True)
        subprocess.run(["git", "push", "-u", "origin", "codecord"], check=True)

        messagebox.showinfo("Éxito", "¡Rama de versión creada y subida correctamente sin errores!")
    except Exception as e:
        messagebox.showerror("Error de Git", f"Ocurrió un error:\n{e}")

def mostrar_documentacion():
    doc_win = tk.Toplevel()
    doc_win.title("Documentación - Gestor Git")
    doc_win.geometry("620x480")

    notebook = ttk.Notebook(doc_win)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # Pestaña 1
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Cómo entrar / Clonar")
    txt1 = tk.Text(tab1, wrap="word", padx=10, pady=10)
    txt1.insert("1.0", f"Para descargar este repositorio en otro PC:\n\n git clone {REPOSITORIO_ACTUAL}.git\n")
    txt1.config(state="disabled")
    txt1.pack(fill="both", expand=True)

    # Pestaña 2
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Versión Default en Web")
    txt2 = tk.Text(tab2, wrap="word", padx=10, pady=10)
    txt2.insert("1.0", "Para cambiar la versión principal que se ve al abrir el link:\n1. Entra a tu GitHub -> Settings -> General.\n2. Busca 'Default branch' y cambia la rama por tu versión.")
    txt2.config(state="disabled")
    txt2.pack(fill="both", expand=True)

    # Pestaña 3 (Actualizada con la guía detallada de borrado local y online)
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text="Eliminar Versiones")
    txt3 = tk.Text(tab3, wrap="word", padx=10, pady=10)
    txt3.insert("1.0", 
        "CÓMO ELIMINAR UNA VERSIÓN (LOCAL Y ONLINE):\n\n"
        "1. Borrar la versión en tu ordenador (Local):\n"
        "   git branch -D NOMBRE_VERSION\n\n"
        "2. Borrar la versión Online (en GitHub):\n"
        "   git push origin --delete refs/heads/NOMBRE_VERSION\n\n"
        "Nota: Recuerda que si una versión está configurada como 'Default branch' "
        "en la web de GitHub, no te dejará borrarla online hasta que cambies la rama "
        "principal a otra desde Settings > General."
    )
    txt3.config(state="disabled")
    txt3.pack(fill="both", expand=True)

if __name__ == "__main__":
    pedir_link_repositorio()