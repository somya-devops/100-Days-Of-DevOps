import os

#Define the target directory for cleanup
target_dir = "./practice_dir"
total_size = 0

print(f"Scanning directory: {target_dir}")

# Check if the directory exists
if os.path.exists(target_dir):
    #Loop through the files in the target directory
    for filename in os.listdir(target_dir):
        #Check if the file ends with .log extension
        if filename.endswith(".log"):
            file_path = os.path.join(target_dir, filename)

            #Get the size of the file in bytes
            file_size = os.path.getsize(file_path)
            total_size += file_size
            
            print(f"Found log file: {filename} - Size: {file_size} bytes")
    print("-----------------------------------")
    print(f"Total size of log files: {total_size} bytes")
else:    print(f"Directory {target_dir} does not exist.")