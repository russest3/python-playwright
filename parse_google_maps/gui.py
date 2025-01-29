import tkinter as tk
from tkinter import ttk
import google_maps_parse

class WebCrawlerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Crawler | Select Bot")
        self.root.geometry("640x480")  # Set the window size to 640x480
        
        # Create the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Label
        self.label = tk.Label(self.main_frame, text="Please select which bot you would like to use:")
        self.label.pack(pady=10)
        
        # ComboBox
        self.bot_options = ["value 1", "value 2", "value 3"]
        self.combobox = ttk.Combobox(self.main_frame, values=self.bot_options)
        self.combobox.pack(pady=10)
        self.combobox.bind("<<ComboboxSelected>>", self.on_bot_selected)
    
    def on_click_start(self):
        search_terms = self.search_text.get("1.0", tk.END).strip()
        print(search_terms)
        # google_maps_parse(search_terms)  # Now pass this to the google_maps_parse and display output in frame4
        
    def on_bot_selected(self, event):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        self.new_frame = tk.Frame(self.root)
        self.new_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=False, anchor="n")  # Align to the top
        
        # Label for the new frame
        self.new_label = tk.Label(self.new_frame, text="New Page")
        self.new_label.grid(row=0, column=0, columnspan=2, pady=10)  # Span across both columns
        
        # Create 3 nested frames
        # First row: Two frames side by side
        self.frame1 = tk.Frame(self.new_frame)  # No background color
        self.frame1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        # Add a label and scrollable Listbox to frame1
        self.instructions_label = tk.Label(self.frame1, text="Instructions")
        self.instructions_label.pack(pady=5)
        
        self.instructions_listbox = tk.Listbox(self.frame1)
        self.instructions_listbox.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        self.instructions_scrollbar = tk.Scrollbar(self.frame1, orient=tk.VERTICAL)
        self.instructions_scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
        
        self.instructions_listbox.config(yscrollcommand=self.instructions_scrollbar.set)
        self.instructions_scrollbar.config(command=self.instructions_listbox.yview)
        
        # Add some sample data to the Listbox
        for i in range(1, 21):
            self.instructions_listbox.insert(tk.END, f"Instruction {i}")
        
        self.frame2 = tk.Frame(self.new_frame)  # No background color
        self.frame2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        # Add a label and Text widget to frame2
        self.search_label = tk.Label(self.frame2, text="Enter Search Term(s)")
        self.search_label.pack(pady=5)
        
        self.search_text = tk.Text(self.frame2, height=10, width=30)
        self.search_text.pack(fill=tk.BOTH, expand=True)
        
        # Second row: One frame spanning the entire width
        self.frame3 = tk.Frame(self.new_frame)  # No background color
        self.frame3.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        # Add a label and scrollable Listbox to frame3
        self.log_label = tk.Label(self.frame3, text="Log")
        self.log_label.pack(pady=5)
        
        self.log_listbox = tk.Listbox(self.frame3)
        self.log_listbox.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        self.log_scrollbar = tk.Scrollbar(self.frame3, orient=tk.VERTICAL)
        self.log_scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
        
        self.log_listbox.config(yscrollcommand=self.log_scrollbar.set)
        self.log_scrollbar.config(command=self.log_listbox.yview)
        
        # Add some sample data to the Listbox
        for i in range(1, 51):
            self.log_listbox.insert(tk.END, f"Log Entry {i}")
        
        # Third row: Buttons
        self.button_frame = tk.Frame(self.new_frame)  # Frame for buttons
        self.button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        # Add buttons to the button frame
        self.start_bot_button = tk.Button(self.button_frame, text="Start Bot", width=15, command=self.on_click_start)
        self.start_bot_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_bot_button = tk.Button(self.button_frame, text="Stop Bot", width=15)
        self.stop_bot_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_data_button = tk.Button(self.button_frame, text="Delete Current Data", width=15)
        self.delete_data_button.pack(side=tk.LEFT, padx=5)
        
        self.export_data_button = tk.Button(self.button_frame, text="Export Data", width=15)
        self.export_data_button.pack(side=tk.LEFT, padx=5)
        
        # Configure grid weights to make frames expand proportionally
        self.new_frame.grid_rowconfigure(1, weight=1)
        self.new_frame.grid_rowconfigure(2, weight=1)
        self.new_frame.grid_columnconfigure(0, weight=1)
        self.new_frame.grid_columnconfigure(1, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = WebCrawlerApp(root)
    root.mainloop()