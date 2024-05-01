## Tkinter Grid Example

This repository contains a simple example of using the grid layout manager in Tkinter to create a GUI (Graphical User Interface) application.

### Code Explanation

- **Syntax:** `import tkinter as tk`
  - **Explanation:** Imports the Tkinter module and aliases it as `tk` for ease of use.

- **Syntax:** `root = tk.Tk()`
  - **Explanation:** Creates the main application window.

- **Syntax:** `root.title("Grid Example")`
  - **Explanation:** Sets the title of the window to "Grid Example".

- **Syntax:** `root.geometry("300x200")`
  - **Explanation:** Sets the initial size of the window to 300 pixels wide and 200 pixels high.

- **Syntax:** `label1 = tk.Label(root, text="Label 1", bg="lightblue")`
  - **Explanation:** Creates a label widget with the specified text "Label 1" and background color "lightblue".

- **Syntax:** `label1.grid(row=0, column=0, padx=5, pady=5, rowspan=2)`
  - **Explanation:** Places the label in the first row and first column of the grid, with a horizontal and vertical padding of 5 pixels, and spans 2 rows.

- **Syntax:** `label2 = tk.Label(root, text="Label 2", bg="lightgreen")`
  - **Explanation:** Creates a label widget with the specified text "Label 2" and background color "lightgreen".

- **Syntax:** `label2.grid(row=1, column=0, padx=5, pady=5)`
  - **Explanation:** Places the label in the second row and first column of the grid, with a horizontal and vertical padding of 5 pixels.

- **Syntax:** `label3 = tk.Label(root, text="Label 3", bg="lightcoral")`
  - **Explanation:** Creates a label widget with the specified text "Label 3" and background color "lightcoral".

- **Syntax:** `label3.grid(row=0, column=1, padx=5, pady=5, columnspan=2)`
  - **Explanation:** Places the label in the first row and second column of the grid, with a horizontal and vertical padding of 5 pixels, and spans 2 columns.

- **Syntax:** `label4 = tk.Label(root, text="Label 4", bg="lightyellow")`
  - **Explanation:** Creates a label widget with the specified text "Label 4" and background color "lightyellow".

- **Syntax:** `label4.grid(row=1, column=1, padx=5, pady=5)`
  - **Explanation:** Places the label in the second row and second column of the grid, with a horizontal and vertical padding of 5 pixels.

- **Syntax:** `label5 = tk.Label(root, text="Label 5", bg="lightpink")`
  - **Explanation:** Creates a label widget with the specified text "Label 5" and background color "lightpink".

- **Syntax:** `label5.grid(row=1, column=2, padx=5, pady=5)`
  - **Explanation:** Places the label in the second row and third column of the grid, with a horizontal and vertical padding of 5 pixels.

### Comments

- The `grid()` method is used to place widgets in a grid layout, allowing for more precise control over the positioning and alignment of widgets within the window.
- Parameters such as `row`, `column`, `padx`, `pady`, `rowspan`, and `columnspan` can be used to customize the layout of widgets in the grid.
