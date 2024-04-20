import os
import shutil

def organize_files(base_dir):
    copies_dir = os.path.join(base_dir, "kopie")
    os.makedirs(copies_dir, exist_ok=True)

    report_file = os.path.join(base_dir, "raport.txt")
    with open(report_file, "w") as report:
        for foldername, _, filenames in os.walk(base_dir):
            if foldername != copies_dir:
                report.write(f"{foldername}:\n")
                for i, filename in enumerate(filenames):
                    if filename.lower().endswith(('.jpg', '.png')):
                        source_path = os.path.join(foldername, filename)
                        dest_filename = f"{os.path.basename(foldername)}_{i}.{filename.split('.')[-1]}"
                        dest_path = os.path.join(copies_dir, dest_filename)
                        shutil.copy(source_path, dest_path)
                        report.write(f"    {filename}\n")

def main():
    organize_files("Cw3/Ex3_1")

if __name__ == "__main__":
    main()