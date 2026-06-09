# Day 2: Caching and Python Automation
📅 Day 2: Python Automation & System Design Caching
💻 Part 1: Python Scripting (Directory Scanner)
Objective: Build a memory-efficient script to scan directories and calculate disk space used by specific file extensions to prevent server disk-exhaustion.

Key Built-in Modules Used: * os.path.exists(): Verifies if the target directory is valid before executing code.

os.listdir(): Retrieves all file names inside a directory.

os.path.getsize(): Returns file size in bytes.

Code Snippet Implemented:
Python
# Core logic snippet
for filename in os.listdir(target_dir):
    if filename.endswith(".log"):
        total_size += os.path.getsize(os.path.join(target_dir, filename))
Interview Takeaway: When processing files or logs, always check if paths exist first to prevent runtime errors, and aggregate data efficiently without loading unnecessary files into memory.

