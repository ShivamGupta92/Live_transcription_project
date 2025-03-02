import tkinter as tk
from queue import Queue, Empty

class TranscriptionGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Shivam is Live")
        self.root.geometry("600x400")
        self.root.configure(bg="white")

        self.label = tk.Label(self.root, text="Live Transcription", font=("Arial", 14, "bold"), bg="white")
        self.label.pack(pady=10)

        self.text_area = tk.Text(self.root, font=("Arial", 12), wrap=tk.WORD, height=15, width=60, bg="lightyellow")
        self.text_area.pack(padx=10, pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.close_app, font=("Arial", 12), bg="red", fg="white")
        self.exit_button.pack(pady=5)

        self.queue = Queue()  # For thread-safe updates
        self.update_gui()  # Start updating GUI periodically

    def update_transcription(self, text):
        """Receives transcriptions from another thread."""
        self.queue.put(text)

    def update_gui(self):
        """Updates the text area from the queue without blocking Tkinter."""
        try:
            while not self.queue.empty():
                text = self.queue.get_nowait()
                self.text_area.insert(tk.END, text + "\n")
                self.text_area.see(tk.END)  # Auto-scroll to latest text
        except Empty:
            pass
        self.root.after(100, self.update_gui)  # Run this every 100ms

    def close_app(self):
        """Handles a graceful exit."""
        self.root.quit()  # Properly closes the app

    def start_gui(self):
        """Starts the Tkinter GUI."""
        self.root.mainloop()
