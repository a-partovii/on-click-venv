#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script creates a virtual environment in its own directory,
then installs project dependencies from a 'requirements.txt' file.

It works cross-platform and requires no external libraries,
only Python's standard libraries.
"""
import sys, subprocess, venv
from pathlib import Path

def win_exit():
    """
    Pause auto closing the console window on Windows OS,
    so the window remains visible.
    """

    if sys.platform == "win32":
        input("\nPress <Enter> to exit...")

def main():
    separator_line = "=" * 50 # A separator for console output
    project_dir = Path(__file__).resolve().parent
    requirements = project_dir / "requirements.txt"
    venv_dir = project_dir / "venv"

    if not requirements.exists():
        print()
        print("'requirements.txt' not found!")
        print("You will have an empty venv.")

    print(separator_line)
    print("Starting virtual environment setup")
    print(f"Project directory : {project_dir}")
    print(f"venv path         : {venv_dir}")
    print(separator_line, "\n")

    # A flag to clear the existing virtual environment or not.
    clear_state = False
    if venv_dir.exists():
        print("Attention: venv directory already exists!")
        print("Do you want to keep and update the existing virtual environment? (Otherwise it will be overwritten)")
        user_input = input("Type your answer [Y/n]: ").strip().lower()
        print()

        if user_input in ("n", "no"):
            print("Clearing the old virtual environment ✅")
            clear_state = True
        else:
            print("Updating existing virtual environment...")

    try:
        print("Creating virtual environment...")
        # clear=True removes existing contents by user choice.
        venv.create(
            venv_dir,
            with_pip=True,
            clear=clear_state
        )

    except Exception as error:
        print(f"❌ Error while creating venv: {error}")
        sys.exit(1)

     # Find the Python executable inside the venv
    if sys.platform == "win32":
        python_exe = venv_dir / "Scripts" / "python.exe"
    else:
        python_exe = venv_dir / "bin" / "python3"
        if not python_exe.exists(): # Fallback
                python_exe = venv_dir / "bin" / "python"

    if not python_exe.exists():
        print("❌ Python executable not found inside venv!")
        sys.exit(1)

    if requirements.exists():
        try: # Install requirements.txt
            print(f"\nInstalling packages from {requirements.name}...")

            ## Try upgrading pip, Uncomment it on your own
            # subprocess.check_call(
            #     [str(python_exe), "-m", "pip", "install", "--upgrade", "pip"],
            #     stdout=subprocess.DEVNULL,
            #     stderr=subprocess.STDOUT
            # )

            # Install requirements
            subprocess.check_call(
                [str(python_exe), "-m", "pip", "install", "-r", str(requirements)]
            )
            print()
            print(separator_line)
            print("✅ Installation completed successfully.")

        except subprocess.CalledProcessError as error:
            print(f"❌ Error while installing packages: {error}")
            sys.exit(1)

    print("   Ready to use!")
    print(separator_line)

    if sys.platform == "win32":
        print(f"\nTo activate manually:\n  {venv_dir}\\Scripts\\activate")
        win_exit()
    else:
        print(f"\nTo activate manually:\n  source {venv_dir}/bin/activate")


if __name__ == "__main__":
    main()

