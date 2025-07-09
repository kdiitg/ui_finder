import os
import sys
import subprocess
from pathlib import Path

VENV_DIR = "venv"
REQUIREMENTS_FILE = "requirements.txt"

def run_command(cmd, shell=False):
    result = subprocess.run(cmd, shell=shell)
    if result.returncode != 0:
        print(f"Command failed: {' '.join(cmd)}")
        sys.exit(1)

def create_venv():
    if Path(VENV_DIR).exists():
        print(f"[✓] Virtual environment already exists at '{VENV_DIR}'")
    else:
        print("[*] Creating virtual environment...")
        run_command([sys.executable, "-m", "venv", VENV_DIR])
        print(f"[✓] Virtual environment created at '{VENV_DIR}'")

def install_dependencies():
    pip_path = Path(VENV_DIR) / "Scripts" / "pip.exe"
    if Path(REQUIREMENTS_FILE).exists():
        print("[*] Installing dependencies from requirements.txt...")
        run_command([str(pip_path), "install", "-r", REQUIREMENTS_FILE])
        print("[✓] Dependencies installed.")
    else:
        print("[!] No requirements.txt found — skipping dependency install.")

def print_activation_help():
    print("\n🔧 Manual Activation Needed:")
    print(f"👉 CMD:         {VENV_DIR}\\Scripts\\activate.bat")
    print(f"👉 PowerShell:  .\\{VENV_DIR}\\Scripts\\Activate.ps1")
    print("TIP: In VS Code, Ctrl+Shift+P → Python: Select Interpreter → Choose the new venv.")

def main():
    create_venv()
    # install_dependencies()
    print_activation_help()

if __name__ == "__main__":
    main()
# This script sets up a virtual environment and installs dependencies.
# It also provides instructions for manual activation.