import tkinter as tk

def draw_triangle():
    # Define the coordinates of the triangle vertices
    triangle_coordinates = [100, 100, 100,200, 200, 200,200,100, 100, 100]  # Repeat the first point to close the shape
    
    canvas.create_polygon(triangle_coordinates, fill="orange", outline="black", width=2)

root = tk.Tk()
root.title("Custom Shape Example")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

draw_button = tk.Button(root, text="Draw Triangle", command=draw_triangle)
draw_button.pack()

root.mainloop()
