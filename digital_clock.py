import tkinter as tk
from tkinter import font
from datetime import datetime
import pytz

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock - Multiple Time Zones")
        self.root.geometry("800x500")
        self.root.configure(bg="#1a1a1a")
        
        # Define time zones to display
        self.timezones = [
            ("New York", "America/New_York"),
            ("London", "Europe/London"),
            ("Tokyo", "Asia/Tokyo"),
            ("Sydney", "Australia/Sydney"),
            ("Dubai", "Asia/Dubai"),
            ("São Paulo", "America/Sao_Paulo"),
        ]
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#1a1a1a")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title_label = tk.Label(
            self.main_frame,
            text="⏰ Digital Clock - World Time Zones",
            font=title_font,
            bg="#1a1a1a",
            fg="#00ff00"
        )
        title_label.pack(pady=(0, 20))
        
        # Create clock displays
        self.clock_frames = {}
        self.time_labels = {}
        self.date_labels = {}
        
        for i, (city, timezone) in enumerate(self.timezones):
            # Create frame for each timezone
            tz_frame = tk.Frame(self.main_frame, bg="#2a2a2a", relief=tk.RIDGE, bd=2)
            tz_frame.pack(fill=tk.X, pady=10)
            
            # City name
            city_font = font.Font(family="Helvetica", size=12, weight="bold")
            city_label = tk.Label(
                tz_frame,
                text=city,
                font=city_font,
                bg="#2a2a2a",
                fg="#00ccff"
            )
            city_label.pack(anchor=tk.W, padx=15, pady=(10, 0))
            
            # Time display
            time_font = font.Font(family="Courier", size=28, weight="bold")
            time_label = tk.Label(
                tz_frame,
                text="00:00:00",
                font=time_font,
                bg="#2a2a2a",
                fg="#00ff00"
            )
            time_label.pack(anchor=tk.W, padx=15, pady=5)
            
            # Date display
            date_font = font.Font(family="Helvetica", size=10)
            date_label = tk.Label(
                tz_frame,
                text="",
                font=date_font,
                bg="#2a2a2a",
                fg="#ffaa00"
            )
            date_label.pack(anchor=tk.W, padx=15, pady=(0, 10))
            
            # Store references
            self.time_labels[timezone] = time_label
            self.date_labels[timezone] = date_label
            self.clock_frames[timezone] = tz_frame
        
        # Create control frame
        control_frame = tk.Frame(self.main_frame, bg="#1a1a1a")
        control_frame.pack(fill=tk.X, pady=20)
        
        # Add timezone button
        add_btn = tk.Button(
            control_frame,
            text="➕ Add Timezone",
            command=self.add_timezone,
            bg="#00ff00",
            fg="#1a1a1a",
            font=("Helvetica", 10, "bold"),
            padx=10,
            pady=5
        )
        add_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear all button
        clear_btn = tk.Button(
            control_frame,
            text="🔄 Reset",
            command=self.reset_clocks,
            bg="#ff6600",
            fg="#ffffff",
            font=("Helvetica", 10, "bold"),
            padx=10,
            pady=5
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Start updating
        self.update_time()
    
    def update_time(self):
        """Update all clock displays"""
        for city, timezone in self.timezones:
            try:
                # Get current time in specific timezone
                tz = pytz.timezone(timezone)
                current_time = datetime.now(tz)
                
                # Format time
                time_str = current_time.strftime("%H:%M:%S")
                date_str = current_time.strftime("%A, %B %d, %Y")
                
                # Update labels
                self.time_labels[timezone].config(text=time_str)
                self.date_labels[timezone].config(text=date_str)
            except Exception as e:
                print(f"Error updating {city}: {e}")
        
        # Schedule next update (every 1000ms)
        self.root.after(1000, self.update_time)
    
    def add_timezone(self):
        """Add a new timezone to the display"""
        # Create popup window
        popup = tk.Toplevel(self.root)
        popup.title("Add Timezone")
        popup.geometry("400x200")
        popup.configure(bg="#2a2a2a")
        
        tk.Label(
            popup,
            text="Enter timezone (e.g., Asia/Bangkok):",
            bg="#2a2a2a",
            fg="#00ff00",
            font=("Helvetica", 10)
        ).pack(pady=10)
        
        entry = tk.Entry(popup, font=("Helvetica", 12), width=30)
        entry.pack(pady=10, padx=20)
        
        def save_timezone():
            tz_name = entry.get().strip()
            if tz_name:
                try:
                    # Verify timezone is valid
                    pytz.timezone(tz_name)
                    self.timezones.append((tz_name, tz_name))
                    self.add_clock_display(tz_name, tz_name)
                    popup.destroy()
                except pytz.exceptions.UnknownTimeZoneError:
                    tk.messagebox.showerror("Error", f"Unknown timezone: {tz_name}")
        
        tk.Button(
            popup,
            text="Add",
            command=save_timezone,
            bg="#00ff00",
            fg="#1a1a1a",
            font=("Helvetica", 10, "bold")
        ).pack(pady=10)
    
    def add_clock_display(self, city, timezone):
        """Add a new clock display dynamically"""
        tz_frame = tk.Frame(self.main_frame, bg="#2a2a2a", relief=tk.RIDGE, bd=2)
        tz_frame.pack(fill=tk.X, pady=10)
        
        # City name
        city_font = font.Font(family="Helvetica", size=12, weight="bold")
        city_label = tk.Label(
            tz_frame,
            text=city,
            font=city_font,
            bg="#2a2a2a",
            fg="#00ccff"
        )
        city_label.pack(anchor=tk.W, padx=15, pady=(10, 0))
        
        # Time display
        time_font = font.Font(family="Courier", size=28, weight="bold")
        time_label = tk.Label(
            tz_frame,
            text="00:00:00",
            font=time_font,
            bg="#2a2a2a",
            fg="#00ff00"
        )
        time_label.pack(anchor=tk.W, padx=15, pady=5)
        
        # Date display
        date_font = font.Font(family="Helvetica", size=10)
        date_label = tk.Label(
            tz_frame,
            text="",
            font=date_font,
            bg="#2a2a2a",
            fg="#ffaa00"
        )
        date_label.pack(anchor=tk.W, padx=15, pady=(0, 10))
        
        # Store references
        self.time_labels[timezone] = time_label
        self.date_labels[timezone] = date_label
        self.clock_frames[timezone] = tz_frame
    
    def reset_clocks(self):
        """Reset to default timezones"""
        self.timezones = [
            ("New York", "America/New_York"),
            ("London", "Europe/London"),
            ("Tokyo", "Asia/Tokyo"),
            ("Sydney", "Australia/Sydney"),
            ("Dubai", "Asia/Dubai"),
            ("São Paulo", "America/Sao_Paulo"),
        ]
        
        # Clear all frames except the title
        for widget in list(self.clock_frames.values()):
            widget.destroy()
        
        self.clock_frames.clear()
        self.time_labels.clear()
        self.date_labels.clear()
        
        # Recreate displays
        for city, timezone in self.timezones:
            self.add_clock_display(city, timezone)


if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
