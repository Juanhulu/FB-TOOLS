import os
import shutil
import subprocess

home_dir = "/data/data/com.termux/files/home"
target_dir = os.path.join(home_dir, "FB-TOOLS")
main_file = "main"
main_py = "main.py"
main_path = os.path.join(target_dir, main_file)

os.makedirs(target_dir, exist_ok=True)

current_dir = os.getcwd()

source_main = os.path.join(current_dir, main_file)
source_py = os.path.join(current_dir, main_py)

if os.path.exists(source_main) and os.path.exists(source_py):
    shutil.copy(source_main, os.path.join(target_dir, main_file))
    shutil.copy(source_py, os.path.join(target_dir, main_py))
else:
    print("❌ File 'main' atau 'main.py' tidak ditemukan di direktori saat ini.")
    exit(1)

os.chdir(target_dir)

try:
    os.chmod(main_path, 0o777)
    subprocess.run([main_path])
except Exception as e:
    print(f"❌ Gagal menjalankan '{main_file}': {e}")
