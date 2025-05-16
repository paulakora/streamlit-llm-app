## How to Run the Application

This is a simple Streamlit-based interface for interacting with Large Language Models (LLMs) via the OpenRouter API. You can run it in two main ways:

---

### Option 1: Run Locally with Conda

1. **Create the Conda environment** using the `environment.yml` file:

   ```bash
   conda env create -f environment.yml
   conda activate streamlit-llm
   ```

2. **Add your API key to `.streamlit/secrets.toml`:**

   Create the directory and file:

   ```bash
   mkdir -p .streamlit
   touch .streamlit/secrets.toml
   ```

   Paste your key into the file:

   ```toml
   OPENROUTER_API_KEY = "your_api_key_here"
   ```

3. **Run the application:**

   ```bash
   streamlit run streamlit_app.py
   ```

---

### Option 2: Use a Dev Container (VS Code or GitHub Codespaces)

#### Requirements

- [Docker](https://www.docker.com/) installed locally  
- [Visual Studio Code](https://code.visualstudio.com/) with the **Dev Containers** extension  
  *(Or use [GitHub Codespaces](https://github.com/features/codespaces) — Docker is built-in)*

#### Steps

1. Open the project in **VS Code**

2. Press `Cmd + Shift + P` and choose:  
   `Dev Containers: Reopen in Container`

3. Once the container is built, run the app inside the terminal:

   ```bash
   streamlit run streamlit_app.py
   ```

4. **Provide the API key as an environment variable** (inside the container):

   ```bash
   export OPENROUTER_API_KEY=your_api_key_here
   ```

---

### Accessing the App

- **Locally:** http://localhost:8501
- **In Codespaces:** VS Code will show a forwarded link to access the app

---

### Dependencies

This project uses:
- `environment.yml` — for local Conda-based development
- `requirements.txt` — for pip-based setups and Dev Containers



