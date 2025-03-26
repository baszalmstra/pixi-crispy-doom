import urllib.request
import zipfile
import os

# URL for Freedoom 0.13.0 (update as needed)
url = "https://github.com/freedoom/freedoom/releases/download/v0.13.0/freedoom-0.13.0.zip"
zip_file = "freedoom-0.13.0.zip"

# Download the file
print("Downloading Freedoom 0.13.0...")
urllib.request.urlretrieve(url, zip_file)

# Open the ZIP file and inspect its contents
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    # Print all files in the archive for debugging
    print("Contents of the ZIP file:")
    zip_ref.printdir()

    # Get the list of files
    file_list = zip_ref.namelist()

    # Look for freedoom1.wad and freedoom2.wad (case-insensitive)
    extracted = 0
    for file_name in file_list:
        if "freedoom1.wad" in file_name.lower():
            print(f"Extracting {file_name}...")
            zip_ref.extract(file_name)
            extracted += 1
        elif "freedoom2.wad" in file_name.lower():
            print(f"Extracting {file_name}...")
            zip_ref.extract(file_name)
            extracted += 1

    if extracted == 0:
        print("Error: Could not find 'freedoom1.wad' or 'freedoom2.wad' in the archive.")
    elif extracted == 1:
        print("Warning: Only one IWAD file was found and extracted.")
    else:
        print("Both IWAD files extracted successfully!")

# Clean up the ZIP file
os.remove(zip_file)

print("Process completed!")
