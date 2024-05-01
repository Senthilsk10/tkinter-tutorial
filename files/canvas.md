## Tkinter Custom Shape Example

This repository contains a simple example of creating a custom shape (triangle) using Tkinter in Python.

### Code Explanation

- **Syntax:** `import tkinter as tk`
  - **Explanation:** Imports the Tkinter module and aliases it as `tk` for ease of use.

- **Syntax:** `def draw_triangle():`
  - **Explanation:** Defines a function `draw_triangle()` that draws a triangle on the canvas when the "Draw Triangle" button is clicked.

- **Syntax:** `root = tk.Tk()`
  - **Explanation:** Creates the main application window.

- **Syntax:** `canvas = tk.Canvas(root, width=300, height=300)`
  - **Explanation:** Creates a canvas widget with a width of 300 pixels and a height of 300 pixels.

- **Syntax:** `canvas.pack()`
  - **Explanation:** Packs the canvas widget into the root window.

- **Syntax:** `draw_button = tk.Button(root, text="Draw Triangle", command=draw_triangle)`
  - **Explanation:** Creates a button widget with the text "Draw Triangle" that calls the `draw_triangle()` function when clicked.

- **Syntax:** `draw_button.pack()`
  - **Explanation:** Packs the button widget into the root window.

- **Syntax:** `canvas.create_polygon(triangle_coordinates, fill="orange", outline="black", width=2)`
  - **Explanation:** Draws a polygon (triangle) on the canvas using the specified coordinates for the vertices, filling it with orange color, and outlining it with a black border of width 2 pixels.

### Comments

- Tkinter provides a canvas widget that allows you to draw various shapes and graphics.
- The `create_polygon()` method of the canvas widget is used to draw a polygon (in this case, a triangle) by specifying the coordinates of its vertices.
- When the "Draw Triangle" button is clicked, the `draw_triangle()` function is called, which in turn draws the triangle on the canvas.
