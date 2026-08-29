

```markdown
# 🚀 Gestor Git Fácil (Python & Tkinter)

Una aplicación de escritorio ligera e intuitiva desarrollada en **Python** con **Tkinter** para automatizar las tareas más comunes de **Git y GitHub** sin complicaciones desde la consola.

---

## ✨ Características Principales

* **🔗 Configuración Dinámica:** Introduce el enlace de tu repositorio de GitHub al iniciar la aplicación.
* **🚀 Publicación Rápida:** Añade todos los cambios (`git add`), escribe tu mensaje de commit y súbelos de forma automatizada.
* **🏷️ Control de Versiones por Ramas:** Crea y sube ramas específicas de versión (`git checkout -B` / `git push`) de forma limpia y sin conflictos de nombres.
* **🛡️ Rama de Respaldo Automática:** Diseñado para mantener una rama principal de seguridad (`codecord`) activa mientras experimentas con nuevas versiones.
* **📖 Documentación Integrada:** Pestaña de ayuda interna con comandos útiles para clonar, cambiar la rama predeterminada en la web y eliminar versiones locales u online.

---

## 💻 Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener instalado en tu equipo:
1. **Python 3.x**
2. **Git** (configurado con tu cuenta de GitHub).

---

## 🛠️ Cómo Utilizarlo

1. Clona este repositorio o descarga el script de Python en tu ordenador.
2. Ejecuta el archivo desde tu terminal o IDE de confianza:
   ```bash
   python gestor_git.py

```

3. **Paso 1:** Introduce la URL completa de tu repositorio de GitHub en la ventana de bienvenida.
4. **Paso 2:** En la ventana principal, indica la ruta de tu proyecto local, escribe tu mensaje de cambio (Commit) y opcionalmente el nombre de tu versión/rama.
5. **Paso 3:** Haz clic en **Guardar y Crear Rama de Versión**.

---

## 📖 Guía Rápida (Comandos Útiles)

### 1. Clonar el repositorio en otro equipo

```bash
git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)

```

### 2. Eliminar una versión obsoleta

* **Localmente:**
```bash
git branch -D NOMBRE_VERSION

```


* **Online (Remoto en GitHub):**
```bash
git push origin --delete refs/heads/NOMBRE_VERSION

```



*(Nota: Si la versión está configurada como `Default branch` en GitHub, recuerda cambiar la rama principal en `Settings > General` antes de borrarla).*

---

## 👨‍💻 Autor

Desarrollado por [Aitor](https://github.com/Aitor2010aitor). ¡Ideal para simplificar el flujo de trabajo diario en desarrollo!




<img width="262" height="267" alt="C3BC5210-CA09-45DD-B1EC-BBB9DD604A11" src="https://github.com/user-attachments/assets/03911ce4-ca77-4c00-a787-9a16475bf1a3" />

