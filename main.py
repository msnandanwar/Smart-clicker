# Import libraries for GUI, mouse control, keyboard listening, random numbers, and system tray integration
import pyautogui
import tkinter as tk
from tkinter import messagebox, ttk
from pynput import keyboard
import random
import threading
from pynput.mouse import Button, Listener as MouseListener
import time
import sys

# Global variables
clicking_active = False
click_thread = None
hotkey_listener = None
click_count = 0

# Modern color scheme
COLORS = {
    'bg': '#1e1e1e',           # Dark background
    'surface': '#2d2d2d',      # Surface color
    'primary': '#0078d4',      # Primary blue
    'success': '#107c10',      # Success green
    'danger': '#d13438',       # Danger red
    'warning': '#ff8c00',      # Warning orange
    'text': '#ffffff',         # White text
    'text_secondary': '#cccccc', # Secondary text
    'accent': '#00bcf2',       # Accent blue
    'border': '#3f3f3f'        # Border color
}

class SmartClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Screen Region Clicker")
        self.root.geometry("520x750")
        self.root.resizable(True, True)
        self.root.minsize(500, 700)
        
        # Modern dark theme
        self.root.configure(bg=COLORS['bg'])
        
        # Center the window on screen
        self.center_window()
        
        # Initialize click statistics
        self.click_count = 0
        self.start_time = None
        
        # Initialize GUI components
        self.setup_modern_gui()
        
        # Setup hotkey listener
        self.setup_hotkey()
        
        # Handle window closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Start update loop for real-time feedback
        self.update_gui()
        
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        pos_x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        pos_y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        
    def setup_modern_gui(self):
        """Create a modern, beautiful GUI with enhanced visual feedback"""
        
        # Configure style for ttk widgets
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main container with padding
        main_container = tk.Frame(self.root, bg=COLORS['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # Header section
        self.create_header(main_container)
        
        # Configuration section
        self.create_config_section(main_container)
        
        # Control section
        self.create_control_section(main_container)
        
        # Statistics section
        self.create_stats_section(main_container)
        
        # Status section
        self.create_status_section(main_container)
    
    def create_header(self, parent):
        """Create the header section with title and description"""
        header_frame = tk.Frame(parent, bg=COLORS['bg'])
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Title with gradient effect simulation
        title_label = tk.Label(header_frame, text="Smart Screen Region Clicker", 
                              font=("Segoe UI", 18, "bold"), 
                              fg=COLORS['primary'], bg=COLORS['bg'])
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(header_frame, text="Automated clicking with random positioning", 
                                font=("Segoe UI", 10), 
                                fg=COLORS['text_secondary'], bg=COLORS['bg'])
        subtitle_label.pack(pady=(3, 0))
        
        # Separator line
        separator = tk.Frame(header_frame, height=2, bg=COLORS['primary'])
        separator.pack(fill=tk.X, pady=(10, 0))
    
    def create_config_section(self, parent):
        """Create the configuration section with modern styling"""
        config_frame = tk.LabelFrame(parent, text=" Click Region Configuration ", 
                                   font=("Segoe UI", 11, "bold"), 
                                   fg=COLORS['text'], bg=COLORS['bg'], 
                                   bd=2, relief="groove")
        config_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Inner frame for padding
        inner_frame = tk.Frame(config_frame, bg=COLORS['bg'])
        inner_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)
        
        # Coordinates grid
        coords_grid = tk.Frame(inner_frame, bg=COLORS['bg'])
        coords_grid.pack(fill=tk.X, pady=(0, 12))
        
        # Create coordinate inputs in a 2x2 grid
        self.create_coord_input(coords_grid, "Top Left X:", "100", 0, 0, "entry_tlx")
        self.create_coord_input(coords_grid, "Top Left Y:", "100", 0, 1, "entry_tly")
        self.create_coord_input(coords_grid, "Bottom Right X:", "500", 1, 0, "entry_brx")
        self.create_coord_input(coords_grid, "Bottom Right Y:", "400", 1, 1, "entry_bry")
        
        # Delay configuration
        delay_frame = tk.Frame(inner_frame, bg=COLORS['bg'])
        delay_frame.pack(fill=tk.X, pady=(8, 0))
        
        delay_label = tk.Label(delay_frame, text="Click Delay (seconds):", 
                             font=("Segoe UI", 10, "bold"), 
                             fg=COLORS['text'], bg=COLORS['bg'])
        delay_label.pack(side=tk.LEFT)
        
        self.entry_delay = tk.Entry(delay_frame, font=("Segoe UI", 10), 
                                  width=10, justify='center',
                                  bg=COLORS['surface'], fg=COLORS['text'],
                                  insertbackground=COLORS['text'], bd=1, relief="solid")
        self.entry_delay.pack(side=tk.RIGHT)
        self.entry_delay.insert(0, "1.0")
        
        # Utility button
        utils_frame = tk.Frame(inner_frame, bg=COLORS['bg'])
        utils_frame.pack(fill=tk.X, pady=(12, 0))
        
        get_coords_btn = tk.Button(utils_frame, text="📍 Get Current Mouse Position", 
                                 command=self.get_mouse_position,
                                 font=("Segoe UI", 9), 
                                 bg=COLORS['warning'], fg='white',
                                 bd=0, padx=12, pady=6, cursor="hand2")
        get_coords_btn.pack()
    
    def create_coord_input(self, parent, label_text, default_value, row, col, attr_name):
        """Create a coordinate input field with modern styling"""
        frame = tk.Frame(parent, bg=COLORS['bg'])
        frame.grid(row=row, column=col, padx=10, pady=8, sticky="ew")
        
        parent.grid_columnconfigure(col, weight=1)
        
        label = tk.Label(frame, text=label_text, 
                        font=("Segoe UI", 10, "bold"), 
                        fg=COLORS['text'], bg=COLORS['bg'])
        label.pack(anchor="w")
        
        entry = tk.Entry(frame, font=("Segoe UI", 11), 
                        bg=COLORS['surface'], fg=COLORS['text'],
                        insertbackground=COLORS['text'], bd=1, relief="solid",
                        justify='center')
        entry.pack(fill=tk.X, pady=(5, 0))
        entry.insert(0, default_value)
        
        setattr(self, attr_name, entry)
    
    def create_control_section(self, parent):
        """Create the control section with modern buttons"""
        control_frame = tk.LabelFrame(parent, text=" Control Panel ", 
                                    font=("Segoe UI", 11, "bold"), 
                                    fg=COLORS['text'], bg=COLORS['bg'], 
                                    bd=2, relief="groove")
        control_frame.pack(fill=tk.X, pady=(0, 15))
        
        inner_frame = tk.Frame(control_frame, bg=COLORS['bg'])
        inner_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)
        
        # Button frame
        button_frame = tk.Frame(inner_frame, bg=COLORS['bg'])
        button_frame.pack()
        
        # Start button (centered)
        self.start_button = tk.Button(button_frame, text="▶ START CLICKING", 
                                    command=self.start_clicking,
                                    font=("Segoe UI", 12, "bold"), 
                                    bg=COLORS['success'], fg='white',
                                    bd=0, padx=30, pady=12, cursor="hand2",
                                    width=20)
        self.start_button.pack()
        
        # Hotkey info
        hotkey_frame = tk.Frame(inner_frame, bg=COLORS['bg'])
        hotkey_frame.pack(pady=(15, 0))
        
        # Only ESC key info
        escape_label = tk.Label(hotkey_frame, text="⌨️ Press ESC to stop clicking", 
                              font=("Segoe UI", 11, "bold"), 
                              fg=COLORS['danger'], bg=COLORS['bg'])
        escape_label.pack()
    
    def create_stats_section(self, parent):
        """Create the statistics section with real-time feedback"""
        stats_frame = tk.LabelFrame(parent, text=" Live Statistics ", 
                                  font=("Segoe UI", 11, "bold"), 
                                  fg=COLORS['text'], bg=COLORS['bg'], 
                                  bd=2, relief="groove")
        stats_frame.pack(fill=tk.X, pady=(0, 15))
        
        inner_frame = tk.Frame(stats_frame, bg=COLORS['bg'])
        inner_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)
        
        # Stats grid
        stats_grid = tk.Frame(inner_frame, bg=COLORS['bg'])
        stats_grid.pack(fill=tk.X)
        
        # Click count
        self.click_count_label = tk.Label(stats_grid, text="Clicks: 0", 
                                        font=("Segoe UI", 10, "bold"), 
                                        fg=COLORS['primary'], bg=COLORS['bg'])
        self.click_count_label.grid(row=0, column=0, padx=8, sticky="w")
        
        # Runtime
        self.runtime_label = tk.Label(stats_grid, text="Runtime: 00:00", 
                                    font=("Segoe UI", 10, "bold"), 
                                    fg=COLORS['primary'], bg=COLORS['bg'])
        self.runtime_label.grid(row=0, column=1, padx=8)
        
        # Click rate
        self.rate_label = tk.Label(stats_grid, text="Rate: 0.0/min", 
                                 font=("Segoe UI", 10, "bold"), 
                                 fg=COLORS['primary'], bg=COLORS['bg'])
        self.rate_label.grid(row=0, column=2, padx=8, sticky="e")
        
        stats_grid.grid_columnconfigure(1, weight=1)
        
        # Last click position
        self.position_label = tk.Label(inner_frame, text="Last click: Not started", 
                                     font=("Segoe UI", 9), 
                                     fg=COLORS['text_secondary'], bg=COLORS['bg'])
        self.position_label.pack(pady=(8, 0))
    
    def create_status_section(self, parent):
        """Create the status section with visual indicators"""
        status_frame = tk.LabelFrame(parent, text=" Status ", 
                                   font=("Segoe UI", 11, "bold"), 
                                   fg=COLORS['text'], bg=COLORS['bg'], 
                                   bd=2, relief="groove")
        status_frame.pack(fill=tk.X)
        
        inner_frame = tk.Frame(status_frame, bg=COLORS['bg'])
        inner_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)
        
        # Status indicator with colored dot
        status_container = tk.Frame(inner_frame, bg=COLORS['bg'])
        status_container.pack()
        
        self.status_dot = tk.Label(status_container, text="●", 
                                 font=("Segoe UI", 14), 
                                 fg=COLORS['text_secondary'], bg=COLORS['bg'])
        self.status_dot.pack(side=tk.LEFT, padx=(0, 6))
        
        self.status_label = tk.Label(status_container, text="Ready to start", 
                                   font=("Segoe UI", 11, "bold"), 
                                   fg=COLORS['text'], bg=COLORS['bg'])
        self.status_label.pack(side=tk.LEFT)
    
    def update_gui(self):
        """Update GUI elements with real-time feedback"""
        if clicking_active and self.start_time:
            # Update runtime
            runtime = time.time() - self.start_time
            minutes = int(runtime // 60)
            seconds = int(runtime % 60)
            self.runtime_label.config(text=f"Runtime: {minutes:02d}:{seconds:02d}")
            
            # Update click rate
            if runtime > 0:
                rate = (self.click_count / runtime) * 60  # clicks per minute
                self.rate_label.config(text=f"Rate: {rate:.1f}/min")
        
        # Schedule next update
        self.root.after(1000, self.update_gui)
    
    def get_mouse_position(self):
        """Get current mouse position and display it with modern styling"""
        x, y = pyautogui.position()
        
        # Create custom dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Mouse Position")
        dialog.geometry("300x150")
        dialog.configure(bg=COLORS['bg'])
        dialog.resizable(False, False)
        
        # Center the dialog
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Position info
        info_frame = tk.Frame(dialog, bg=COLORS['bg'])
        info_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        title_label = tk.Label(info_frame, text="Current Mouse Position", 
                             font=("Segoe UI", 12, "bold"), 
                             fg=COLORS['text'], bg=COLORS['bg'])
        title_label.pack(pady=(0, 15))
        
        pos_label = tk.Label(info_frame, text=f"X: {x}  |  Y: {y}", 
                           font=("Segoe UI", 14, "bold"), 
                           fg=COLORS['primary'], bg=COLORS['bg'])
        pos_label.pack(pady=(0, 15))
        
        ok_button = tk.Button(info_frame, text="OK", command=dialog.destroy,
                            font=("Segoe UI", 10), 
                            bg=COLORS['primary'], fg='white',
                            bd=0, padx=20, pady=5, cursor="hand2")
        ok_button.pack()
    
    def click_in_region(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y, delay_seconds):
        """
        Enhanced clicking function with visual feedback and statistics
        """
        global clicking_active
        
        while clicking_active:
            try:
                # Generate random coordinates within the specified region
                target_x = random.randint(min(top_left_x, bottom_right_x), max(top_left_x, bottom_right_x))
                target_y = random.randint(min(top_left_y, bottom_right_y), max(top_left_y, bottom_right_y))
                
                # Move to the target position and click with smooth movement
                pyautogui.moveTo(target_x, target_y, duration=0.2)
                pyautogui.click()
                
                # Update statistics
                self.click_count += 1
                
                # Update GUI in thread-safe way with enhanced feedback
                self.root.after(0, self.update_click_feedback, target_x, target_y)
                
                # Wait for the specified delay
                time.sleep(delay_seconds)
                
            except Exception as e:
                print(f"Error during clicking: {e}")
                self.root.after(0, self.handle_click_error, str(e))
                break
        
        # Update status when stopping
        self.root.after(0, self.update_stop_status)
    
    def update_click_feedback(self, x, y):
        """Update GUI with click feedback"""
        self.status_label.config(text="Clicking in progress...")
        self.status_dot.config(fg=COLORS['success'])
        self.position_label.config(text=f"Last click: ({x}, {y})")
        self.click_count_label.config(text=f"Clicks: {self.click_count}")
    
    def handle_click_error(self, error_msg):
        """Handle clicking errors"""
        self.status_label.config(text="Error occurred!")
        self.status_dot.config(fg=COLORS['danger'])
        print(f"Clicking error: {error_msg}")
    
    def update_stop_status(self):
        """Update GUI when clicking stops"""
        self.status_label.config(text="Stopped")
        self.status_dot.config(fg=COLORS['text_secondary'])
    
    def start_clicking(self):
        """Enhanced start function with modern feedback"""
        global clicking_active, click_thread
        
        try:
            # Get values from entry fields
            tlx = int(self.entry_tlx.get())
            tly = int(self.entry_tly.get())
            brx = int(self.entry_brx.get())
            bry = int(self.entry_bry.get())
            delay = float(self.entry_delay.get())
            
            # Validate delay
            if delay <= 0:
                self.show_error("Invalid Input", "Delay must be greater than 0")
                return
            
            # Validate coordinates
            if tlx == brx or tly == bry:
                self.show_error("Invalid Input", "Top-left and bottom-right coordinates must be different")
                return
            
            # Reset statistics
            self.click_count = 0
            self.start_time = time.time()
            
            # Set clicking active and update GUI
            clicking_active = True
            self.start_button.config(state=tk.DISABLED, bg=COLORS['surface'], 
                                   text="🔄 CLICKING ACTIVE")
            self.status_label.config(text="Starting...")
            self.status_dot.config(fg=COLORS['warning'])
            
            # Start clicking thread
            click_thread = threading.Thread(target=self.click_in_region, args=(tlx, tly, brx, bry, delay))
            click_thread.daemon = True
            click_thread.start()
            
        except ValueError:
            self.show_error("Invalid Input", "Please enter valid numbers for all fields")
            return
        except Exception as e:
            self.show_error("Error", f"An error occurred: {str(e)}")
            return
    
    def stop_clicking(self):
        """Enhanced stop function with modern feedback"""
        global clicking_active
        
        clicking_active = False
        self.start_button.config(state=tk.NORMAL, bg=COLORS['success'], 
                               text="▶ START CLICKING")
        self.status_label.config(text="Stopping...")
        self.status_dot.config(fg=COLORS['warning'])
    
    def show_error(self, title, message):
        """Show error dialog with modern styling"""
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("350x180")
        dialog.configure(bg=COLORS['bg'])
        dialog.resizable(False, False)
        
        # Center the dialog
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Error content
        content_frame = tk.Frame(dialog, bg=COLORS['bg'])
        content_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Error icon and title
        title_frame = tk.Frame(content_frame, bg=COLORS['bg'])
        title_frame.pack(fill=tk.X, pady=(0, 15))
        
        title_label = tk.Label(title_frame, text=f"⚠️ {title}", 
                             font=("Segoe UI", 12, "bold"), 
                             fg=COLORS['danger'], bg=COLORS['bg'])
        title_label.pack()
        
        # Message
        msg_label = tk.Label(content_frame, text=message, 
                           font=("Segoe UI", 10), 
                           fg=COLORS['text'], bg=COLORS['bg'],
                           wraplength=300, justify='center')
        msg_label.pack(pady=(0, 20))
        
        # OK button
        ok_button = tk.Button(content_frame, text="OK", command=dialog.destroy,
                            font=("Segoe UI", 10), 
                            bg=COLORS['danger'], fg='white',
                            bd=0, padx=20, pady=8, cursor="hand2")
        ok_button.pack()
    
    def setup_hotkey(self):
        """Set up global hotkey listener for ESC (stop only)"""
        def on_escape_activate():
            if clicking_active:
                self.stop_clicking()
        
        global hotkey_listener
        
        # Create ESC hotkey only
        escape_hotkey = keyboard.HotKey(keyboard.HotKey.parse('<esc>'), on_escape_activate)
        
        def on_press(key):
            escape_hotkey.press(hotkey_listener.canonical(key))
        
        def on_release(key):
            escape_hotkey.release(hotkey_listener.canonical(key))
        
        hotkey_listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release
        )
        hotkey_listener.start()
    
    def on_closing(self):
        """Handle window closing event"""
        global clicking_active, hotkey_listener
        
        # Stop clicking
        clicking_active = False
        
        # Stop hotkey listener
        if hotkey_listener:
            hotkey_listener.stop()
        
        # Close the window
        self.root.destroy()

def main():
    """Main function to create and run the application"""
    # Disable pyautogui fail-safe for better user experience
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.1
    
    # Create the main window
    root = tk.Tk()
    app = SmartClickerApp(root)
    
    try:
        # Start the GUI event loop
        root.mainloop()
    except KeyboardInterrupt:
        app.on_closing()

if __name__ == "__main__":
    main()
