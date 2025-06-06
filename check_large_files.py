import os

# Ayar → hangi boyuttan büyükleri gösterelim (MB cinsinden)
threshold_mb = 5

# Dizin → current directory (.)
root_dir = "."

# MB -> byte dönüşüm
threshold_bytes = threshold_mb * 1024 * 1024

print(f"🚀 Scanning for files larger than {threshold_mb} MB...\n")

large_files = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        try:
            filesize = os.path.getsize(filepath)
            if filesize > threshold_bytes:
                large_files.append((filesize, filepath))
        except Exception as e:
            print(f"⚠️ Could not access {filepath}: {e}")

# Büyükten küçüğe sırala
large_files.sort(reverse=True)

# Sonuçları göster
for filesize, filepath in large_files:
    size_mb = filesize / (1024 * 1024)
    print(f"[{size_mb:.2f} MB] → {filepath}")

if not large_files:
    print("✅ No large files found.")
