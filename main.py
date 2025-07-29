# Simple GUI for youtube download using yt-dlp
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import shlex

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SafeDownloadDSG")
        self.geometry("500x200")

        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        home_frame = ttk.Frame(notebook)
        notebook.add(home_frame, text="Home")
        ttk.Label(home_frame, text="Welcome to SafeDownloadDSG").pack(pady=20)

        download_frame = YTDownloadFrame(notebook)
        notebook.add(download_frame, text="YT-DownloadSafe")

class YTDownloadFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.url_var = tk.StringVar()
        self.format_var = tk.StringVar(value="MP4 best")

        ttk.Label(self, text="YouTube URL:").grid(row=0, column=0, pady=5, sticky="w")
        ttk.Entry(self, textvariable=self.url_var, width=50).grid(row=0, column=1, padx=5)

        format_frame = ttk.LabelFrame(self, text="Format")
        format_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky="we")

        options = ["MP4 best", "MP4 1080p", "MP3 audio"]
        self.format_combo = ttk.Combobox(format_frame, values=options, textvariable=self.format_var, state="readonly")
        self.format_combo.pack(fill=tk.X, padx=10, pady=5)

        ttk.Button(self, text="Download", command=self.download).grid(row=2, column=0, columnspan=2, pady=10)

    def download(self):
        url = self.url_var.get().strip()
        fmt = self.format_var.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return

        if fmt == "MP3 audio":
            cmd = f"yt-dlp -x --audio-format mp3 {shlex.quote(url)}"
        elif fmt == "MP4 1080p":
            cmd = (
                "yt-dlp -f \"bv[height<=1080]+ba/b[height<=1080]\" --merge-output-format mp4 "
                f"{shlex.quote(url)}"
            )
        else:  # MP4 best
            cmd = f"yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 {shlex.quote(url)}"

        try:
            subprocess.run(shlex.split(cmd), check=True)
            messagebox.showinfo("Success", "Download completed")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Download failed: {e}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
