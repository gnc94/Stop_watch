import tkinter as tk

running = False
hours, minutes, seconds = 0, 0, 0


def start():
    global running
    if not running:
        update()
        running = True

def stop():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    stopwatch_label.config(text='00:00:00')

def update():
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    global update_time
    update_time = stopwatch_label.after(1000, update)

root = tk.Tk()
root.geometry('485x240')
root.title('Stopwatch')
root.config(bg='black')

stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 80), fg='white', bg='black')
stopwatch_label.pack(pady=20)

button_frame = tk.Frame(root, bg='black')
button_frame.pack(pady=20)

start_button = tk.Button(button_frame, text='start', height=3, width=7, font=('Arial', 20), command=start, fg='white', bg='black')
start_button.pack(side=tk.LEFT, padx=10)
stop_button = tk.Button(button_frame, text='stop', height=3, width=7, font=('Arial', 20), command=stop, fg='white', bg='black')
stop_button.pack(side=tk.LEFT, padx=10)
reset_button = tk.Button(button_frame, text='reset', height=3, width=7, font=('Arial', 20), command=reset, fg='white', bg='black')
reset_button.pack(side=tk.LEFT, padx=10)
exit_button = tk.Button(button_frame, text='exit', height=3, width=7, font=('Arial', 20), command=root.quit, fg='white', bg='black')
exit_button.pack(side=tk.LEFT, padx=10)

created_by_label = tk.Label(root, text='Created by Sameer Khan', font=('Arial', 10), fg='white', bg='black')
created_by_label.pack(side=tk.LEFT, anchor='sw', padx=10, pady=10)

root.mainloop()
