#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup_venv.py
Works only with Python standard libraries.
"""
import sys, subprocess, venv
from pathlib import Path

def win_exit():
    if sys.platform == "win32":
        input("\nPress <Enter> to exit...")

def main():
    graphical_line = "=" * 50 # The TUI line
    project_dir = Path(__file__).resolve().parent
    requirements = project_dir / "requirements.txt"

    if not requirements.exists():
        print("\n❌ 'requirements.txt' not found!")
        print("Please create a 'requirements.txt' file and try again.")
        win_exit()
        sys.exit(1)

    venv_dir = project_dir / "venv"

    if venv_dir.exists():
        print("\nAttention: venv directory already exists!")
        user_input = input("Are you sure you want to overwrite the existing virtual environment? [Y/n] ").strip().lower()
        if user_input not in ("y", "yes"):
            print("Aborted.")
            win_exit()
            return

    print(graphical_line)
    print("Starting virtual environment setup")
    print(f"Project directory : {project_dir}")
    print(f"venv path         : {venv_dir}")
    print(graphical_line)

    print("\nCreating virtual environment...")
    try:
        # clear=True removes existing contents if the directory already exists
        venv.create(venv_dir, with_pip=True, clear=True)
        print("✅ venv created successfully.")
    except Exception as error:
        print(f"❌ Error while creating venv: {error}")
        sys.exit(1)

    try: # Find the Python executable inside the venv
        if sys.platform == "win32":
            python_exe = venv_dir / "Scripts" / "python.exe"
        else:
            python_exe = venv_dir / "bin" / "python3"
    except:
        if not python_exe.exists():
            print("❌ Python executable not found inside venv!")
            sys.exit(1)

    try: # Install requirements.txt
        print(f"\nInstalling packages from {requirements.name}...")
        # First, try upgrade pip
        subprocess.check_call(
            [str(python_exe), "-m", "pip", "install", "--upgrade", "pip"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT
        )
        # Install requirements
        subprocess.check_call(
            [str(python_exe), "-m", "pip", "install", "-r", str(requirements)]
        )
        print("\n", graphical_line)
        print("✅ Installation completed successfully.")
    except subprocess.CalledProcessError as error:
        print(f"❌ Error while installing packages: {error}")
        sys.exit(1)

    print("   Ready to use!")
    print(graphical_line)

    if sys.platform == "win32":
        print(f"\nTo activate manually:\n  {venv_dir}\\Scripts\\activate")
        win_exit()
    else:
        print(f"\nTo activate manually:\n  source {venv_dir}/bin/activate")


if __name__ == "__main__":
    main()
