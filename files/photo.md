## Tkinter Image Viewer Example

This repository contains a simple example of creating an image viewer using Tkinter in Python.

### Code Explanation

- **Syntax:** `import tkinter as tk`
  - **Explanation:** Imports the Tkinter module and aliases it as `tk` for ease of use.

- **Syntax:** `from tkinter import PhotoImage`
  - **Explanation:** Imports the `PhotoImage` class from the Tkinter module.

- **Syntax:** `def display_image():`
  - **Explanation:** Defines a function `display_image()` that displays an image on the label widget when the "Display Image" button is clicked.

- **Syntax:** `root = tk.Tk()`
  - **Explanation:** Creates the main application window.

- **Syntax:** `entry = tk.Entry(root, width=50)`
  - **Explanation:** Creates an entry widget where the user can input the file path of the image.

- **Syntax:** `entry.pack()`
  - **Explanation:** Packs the entry widget into the root window.

- **Syntax:** `open_button = tk.Button(root, text="Display Image", command=display_image)`
  - **Explanation:** Creates a button widget with the text "Display Image" that calls the `display_image()` function when clicked.

- **Syntax:** `open_button.pack()`
  - **Explanation:** Packs the button widget into the root window.

- **Syntax:** `image_label = tk.Label(root)`
  - **Explanation:** Creates a label widget where the image will be displayed.

- **Syntax:** `image_label.pack()`
  - **Explanation:** Packs the label widget into the root window.

- **Syntax:** `image = PhotoImage(file=file_path)`
  - **Explanation:** Loads the image from the file path specified in the entry widget using the `PhotoImage` class.

- **Syntax:** `image_label.config(image=image)`
  - **Explanation:** Configures the label widget to display the loaded image.

- **Syntax:** `image_label.image = image`
  - **Explanation:** Keeps a reference to the loaded image to prevent it from being garbage-collected.

- **Syntax:** `except:`
  - **Explanation:** Catches any exceptions that may occur during the loading of the image, such as an invalid file path or format.

- **Syntax:** `print("Invalid image path or format.")`
  - **Explanation:** Prints a message to the console if an invalid image path or format is provided.

### Comments

- Tkinter provides the `PhotoImage` class for displaying images in GUI applications.
- Users can input the file path of the image in the entry widget, and clicking the "Display Image" button loads and displays the image on the label widget.
- Error handling is implemented to handle cases where the provided image path is invalid or the image format is unsupported.
