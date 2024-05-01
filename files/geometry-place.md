## Tkinter Place Example

This repository contains a simple example of using the place geometry manager in Tkinter to create a GUI (Graphical User Interface) application.

### Code Explanation

- **Syntax:** `import tkinter as tk`
  - **Explanation:** Imports the Tkinter module and aliases it as `tk` for ease of use.

- **Syntax:** `root = tk.Tk()`
  - **Explanation:** Creates the main application window.

- **Syntax:** `root.title("Place Example")`
  - **Explanation:** Sets the title of the window to "Place Example".

- **Syntax:** `root.geometry("300x200")`
  - **Explanation:** Sets the initial size of the window to 300 pixels wide and 200 pixels high.

- **Syntax:** `label1 = tk.Label(root, text="Label 1", bg="lightblue")`
  - **Explanation:** Creates a label widget with the specified text "Label 1" and background color "lightblue".

- **Syntax:** `label1.place(x=50, y=50)`
  - **Explanation:** Places the label at the absolute position (50, 50) within the root window.

- **Syntax:** `label2 = tk.Label(root, text="Label 2", bg="lightgreen")`
  - **Explanation:** Creates a label widget with the specified text "Label 2" and background color "lightgreen".

- **Syntax:** `label2.place(relx=0.10, rely=0.10)`
  - **Explanation:** Places the label at the relative position (10% of the width, 10% of the height) within the root window.

- **Syntax:** `label3 = tk.Label(root, text="Label 3", bg="lightcoral")`
  - **Explanation:** Creates a label widget with the specified text "Label 3" and background color "lightcoral".

- **Syntax:** `label3.place(x=200, y=150, width=50, height=25)`
  - **Explanation:** Places the label at the absolute position (200, 150) within the root window, with a width of 50 pixels and a height of 25 pixels.

### Comments

- The `place()` method is used to precisely position widgets within a container by specifying either absolute or relative coordinates.
- Parameters such as `x`, `y`, `relx`, `rely`, `width`, and `height` can be used to customize the placement and size of widgets.
