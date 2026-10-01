## on-click-venv

A single Python script that sets up a virtual environment and installs your project dependencies in one step.

It works cross-platform and uses only Python's standard library, so no extra tools are required.

### Usage

**On Windows, you can simply double-click `setup-venv.py` in the project folder.**

On other systems, such as macOS or Linux, run:

```bash
python setup-venv.py
```

Make sure a `requirements.txt` file exists in the project folder.<br>
Once it finishes, you can activate the environment:

```bash
# Windows
venv\Scripts\activate
```

```bash
# macOS / Linux
source venv/bin/activate
```

### Requirements

- Python 3.8 or newer
