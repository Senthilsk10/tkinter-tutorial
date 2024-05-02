
# Tkinter Events Reference

Tkinter provides various events that you can bind to widgets to trigger specific actions. Here's a list of commonly used events along with their syntax and explanations:

## Mouse Events

### Mouse Button Events

- **`<Button-1>`**: Left mouse button click
- **`<Button-2>`**: Middle mouse button click
- **`<Button-3>`**: Right mouse button click

```python
widget.bind("<Button-1>", callback)
```

### Double-Click Events

- **`<Double-Button-1>`**: Double-click with the left mouse button
- **`<Double-Button-2>`**: Double-click with the middle mouse button
- **`<Double-Button-3>`**: Double-click with the right mouse button

```python
widget.bind("<Double-Button-1>", callback)
```

### Mouse Motion Events

- **`<Enter>`**: Mouse enters the widget's area
- **`<Leave>`**: Mouse leaves the widget's area
- **`<Motion>`**: Mouse is moved within the widget's area

```python
widget.bind("<Enter>", callback)
```

## Keyboard Events

### Key Press Events

- **`<KeyPress>`**: Any key is pressed
- **`<KeyPress-KeyPressName>`**: A specific key is pressed (e.g., `<KeyPress-a>` for the 'a' key)

```python
widget.bind("<KeyPress>", callback)
```

### Key Release Events

- **`<KeyRelease>`**: Any key is released
- **`<KeyRelease-KeyPressName>`**: A specific key is released (e.g., `<KeyRelease-a>` for the 'a' key)

```python
widget.bind("<KeyRelease>", callback)
```

## Widget Events

### Focus Events

- **`<FocusIn>`**: Widget gains focus
- **`<FocusOut>`**: Widget loses focus

```python
widget.bind("<FocusIn>", callback)
```

### Change Events

- **`<Configure>`**: Widget is resized or moved

```python
widget.bind("<Configure>", callback)
```
```
