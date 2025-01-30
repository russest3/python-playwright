import tkinter as tk
from tkinter import ttk
import google_maps_parse as gmp
import re
import csv
import ast
import threading
import time

class WebCrawlerApp:
    def __init__(self, root):
        self.root = root
        self.urls = ""
        self.root.title("Web Crawler | Select Bot")
        self.root.geometry("1200x600")
        
        # Create the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)
        
        # Label
        self.label = tk.Label(self.main_frame, text="Please select which bot you would like to use:")
        self.label.pack(pady=10)
        
        # ComboBox
        self.bot_options = ["Parse Google Maps", "Parse apartments.com"]
        self.combobox = ttk.Combobox(self.main_frame, values=self.bot_options)
        self.combobox.pack(pady=10)
        self.combobox.bind("<<ComboboxSelected>>", self.on_bot_selected)

    def on_click_start(self):
        search_term = self.search_text.get("1.0", "end-1c")
        urls = gmp.get_search_results_links(str(search_term))
        results = str(gmp.get_search_results(urls))
        results = re.sub("{{", "{", results)
        results = re.sub("}}", "}, ", results)
        results = ast.literal_eval(results)
        self.results_text.insert(tk.END, results)

    def on_click_export(self):
        filename = self.search_text.get("1.0", "end-1c")
        filename = re.sub(" ", "-", filename)
        results = self.results_text.get("1.0", "end-1c")
        results = re.sub("{{", "{", results)
        results = re.sub("}}", "}, ", results)
        my_dict = ast.literal_eval(results)
        header = ["name", "category", "address", "website", "phone", "review_count", "stars", "5_stars", "4_stars", "3_stars", "2_stars", "1_stars"]
        with open(filename + '.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(my_dict)

    def on_click_delete(self):
        self.results_text.delete("1.0", "end-1c")
        self.search_text.delete("1.0", "end-1c")
    
    def on_bot_selected(self, event):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        self.root.title("Web Crawler Bot")
        self.new_frame = tk.Frame(self.root)
        self.new_frame.pack(padx=15, pady=15, fill=tk.BOTH, expand=False, anchor="n", side="top")  # Align to the top
        
        # Label for the new frame
        self.new_label = tk.Label(self.new_frame)
        self.new_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")  # Span across both columns
        
        # Create 3 nested frames
############ First row: Two frames side by side #####################################
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
        
        self.instructions_listbox.insert(tk.END, "Enter in a prompt to search Google Maps, i.e. 'restaurants in miami'")
        self.instructions_listbox.insert(tk.END, "")
        self.instructions_listbox.insert(tk.END, "Then click 'Start Bot', the results will show below")
        self.instructions_listbox.insert(tk.END, "")
        self.instructions_listbox.insert(tk.END, "To save results as a CSV file, click 'Export Data")
        self.instructions_listbox.insert(tk.END, "")
        self.instructions_listbox.insert(tk.END, "Click 'Delete Current Data' to clear the fields")
        self.instructions_listbox.insert(tk.END, "")
        self.instructions_listbox.insert(tk.END, "Click 'Stop Bot' to stop a processing search")
        
        self.frame2 = tk.Frame(self.new_frame)  # No background color
        self.frame2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        # Add a label and Text widget to frame2
        self.search_label = tk.Label(self.frame2, text="Enter Search Prompt")
        self.search_label.pack(pady=5)
        
        self.search_text = tk.Text(self.frame2, height=10, width=30)
        self.search_text.pack(fill=tk.BOTH, expand=True)
############ First row: Two frames side by side #####################################

        
################# Second row: One frame spanning the entire width ###############################
        self.frame3 = tk.Frame(self.new_frame)  # No background color
        self.frame3.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        # Add a label and Text widget to frame3
        self.search_label = tk.Label(self.frame3)
        self.search_label.pack(pady=5)
        
        self.results_text = tk.Text(self.frame3, height=10, width=30)
        self.results_text.pack(fill=tk.BOTH, expand=True)
################# Second row: One frame spanning the entire width ###############################



        
################## Third row: Buttons #####################################################
        self.button_frame = tk.Frame(self.new_frame)  # Frame for buttons
        self.button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        # Add buttons to the button frame
        self.start_bot_button = tk.Button(self.button_frame, text="Start Bot", width=15, command=self.on_click_start)
        self.start_bot_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_data_button = tk.Button(self.button_frame, text="Delete Current Data", width=15, command=self.on_click_delete)
        self.delete_data_button.pack(side=tk.LEFT, padx=5)
        
        self.export_data_button = tk.Button(self.button_frame, text="Export Data", width=15, command=self.on_click_export)
        self.export_data_button.pack(side=tk.LEFT, padx=5)
        
        # Configure grid weights to make frames expand proportionally
        self.new_frame.grid_rowconfigure(1, weight=1)
        self.new_frame.grid_rowconfigure(2, weight=1)
        self.new_frame.grid_columnconfigure(0, weight=1)
        self.new_frame.grid_columnconfigure(1, weight=1)
################## Third row: Buttons #####################################################

if __name__ == "__main__":
    root = tk.Tk()
    app = WebCrawlerApp(root)
    root.mainloop()