import os
import shutil
import subprocess

target_dir = "/data/data/com.termux/files/home/FB-TOOLS"
main_file = "main"
exe_py = "main.py"
home_dir = "/data/data/com.termux/files/home"
current_dir = os.getcwd()

if current_dir != target_dir:
    os.chdir(home_dir)
    os.makedirs("FB-TOOLS", exist_ok=True)

    if os.path.exists(os.path.join(current_dir, main_file)) and os.path.exists(os.path.join(current_dir, exe_py)):
        shutil.copy(os.path.join(current_dir, main_file), os.path.join(target_dir, main_file))
        shutil.copy(os.path.join(current_dir, exe_py), os.path.join(target_dir, exe_py))
    else:
        print("File main atau main.py tidak ditemukan.")
    
    os.chdir(target_dir)
else:
    os.chdir(target_dir)

main_path = os.path.join(target_dir, main_file)

try:
    os.chmod(main_path, 0o777)
    subprocess.run([main_path])
except Exception as e:
    print(f"Error: {e}")
