import os

total_jpg = 0
total_ipynb = 0
jpg_size = 0
ipynb_size = 0

for root, dirs, files in os.walk("."):
    for file in files:
        path = os.path.join(root, file)
        size = os.path.getsize(path)

        if file.lower().endswith(".jpg"):
            total_jpg += 1
            jpg_size += size

        elif file.lower().endswith(".ipynb"):
            total_ipynb += 1
            ipynb_size += size

print("JPG files:", total_jpg)
print("JPG size:", round(jpg_size / (1024**3), 2), "GB")

print("IPYNB files:", total_ipynb)
print("IPYNB size:", round(ipynb_size / (1024**2), 2), "MB")