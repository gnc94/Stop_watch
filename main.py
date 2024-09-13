# ***** IMPORTS *****
import tkinter as tk

# ***** VARIABLES *****
# Use a boolean variable to help control the state of time (running or not running)
running = False
# Time variables initially set to 0
hours, minutes, seconds = 0, 0, 0

# ***** FUNCTIONS *****
# Start, stop, and reset functions will be called when the buttons are clicked
# Start function
def start():
    global running
    if not running:
        update()
        running = True

# Stop function (renamed from pause)
def stop():
    global running
    if running:
        # Cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

# Reset function
def reset():
    global running
    if running:
        # Cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False
    # Set variables back to zero
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    # Set label back to zero
    stopwatch_label.config(text='00:00:00')

# Update stopwatch function
def update():
    # Update seconds with (addition) compound assignment operator
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    # Format time to include leading zeros
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    # Update timer label after 1000 ms (1 second)
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # After each second (1000 milliseconds), call update function
    global update_time
    update_time = stopwatch_label.after(1000, update)

# ***** WIDGETS *****
# Create main window
root = tk.Tk()
root.geometry('485x240')  # Adjusted height
root.title('Stopwatch')
root.config(bg='black')  # Set background color to black

# Label to display time
stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 80), fg='white', bg='black')  # White text, black background
stopwatch_label.pack(pady=20)  # Add padding to center vertically

# Create a frame to hold buttons and center it
button_frame = tk.Frame(root, bg='black')
button_frame.pack(pady=20)  # Center frame with padding

# Start, stop, reset, exit buttons inside the frame
start_button = tk.Button(button_frame, text='start', height=3, width=7, font=('Arial', 20), command=start, fg='white', bg='black')
start_button.pack(side=tk.LEFT, padx=10)  # Add padding between buttons
stop_button = tk.Button(button_frame, text='stop', height=3, width=7, font=('Arial', 20), command=stop, fg='white', bg='black')  # Renamed button
stop_button.pack(side=tk.LEFT, padx=10)
reset_button = tk.Button(button_frame, text='reset', height=3, width=7, font=('Arial', 20), command=reset, fg='white', bg='black')
reset_button.pack(side=tk.LEFT, padx=10)
exit_button = tk.Button(button_frame, text='exit', height=3, width=7, font=('Arial', 20), command=root.quit, fg='white', bg='black')  # Renamed button
exit_button.pack(side=tk.LEFT, padx=10)

# Created by label (bottom left corner)
created_by_label = tk.Label(root, text='Created by Sameer Khan', font=('Arial', 10), fg='white', bg='black')
created_by_label.pack(side=tk.LEFT, anchor='sw', padx=10, pady=10)

# ***** MAINLOOP *****
# Run app
root.mainloop()
