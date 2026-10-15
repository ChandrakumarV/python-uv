# python-uv

A modern Python project initialized and managed with [uv](https://docs.astral.sh/uv/) – an extremely fast Python package and project manager written in Rust.

---

## 🚀 Features

- **Blazing Fast**: Powered by `uv` for ultra-fast dependency resolution and environment management.
- **Modern Packaging**: Uses `pyproject.toml` standard configuration and the `uv_build` backend.
- **CLI Ready**: Built-in script entry point (`python-uv`) ready for development and distribution.

---

## 📋 Prerequisites

- **Python**: `>= 3.12`
- **uv**: `>= 0.12` (Install via `curl -LsSf https://astral.sh/uv/install.sh` or `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`)

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd python-uv
```

### 2. Install dependencies & set up virtual environment

Sync the project and install all required dependencies into a local virtual environment:

```bash
uv sync
```

### 3. Run the application

Execute the CLI entry point using `uv run`:

```bash
uv run python-uv
```

Output:
```text
--- Python UV Demo ---
Hello, Alice!
5 + 3 = 8
4 * 2 = 8
Hi, I'm Bob and I'm 25 years old.
This is a Casio calculator.
```

---

## 📁 Project Structure

```text
python-uv/
├── .python-version       # Target Python version pin (3.12)
├── pyproject.toml        # Project metadata, scripts, and build system config
├── README.md             # Project documentation
├── uv.lock               # Deterministic dependency lockfile
└── src/
    └── python_uv/
        ├── __init__.py   # Application entry point
        ├── calculator.py # Simple math functions and Calculator class
        └── person.py     # Simple greeting function and Person class
```

---

## 🧰 Useful `uv` Commands

| Command | Description |
| :--- | :--- |
| `uv sync` | Synchronize the virtual environment with `uv.lock` |
| `uv run <command>` | Run a command or script within the project environment |
| `uv add <package>` | Add a dependency to `pyproject.toml` and update the lockfile |
| `uv remove <package>` | Remove a dependency from the project |
| `uv lock` | Regenerate or update the `uv.lock` lockfile |
| `uv build` | Build wheel and source distributions |

---

## 👤 Author

- **ChandrakumarV** - [chandrakumar252004@gmail.com](mailto:chandrakumar252004@gmail.com)
