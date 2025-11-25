# Documentation: Managing `pyproject.toml` with UV

## 1. What is UV and why we use it
**UV** is a fast, modern Python package and environment manager that streamlines development, testing, and deployment.

- Lightning-fast package installation and dependency resolution.
- Reliable dependency locking and reproducible environments
- Compatible with existing Python tools and workflows
- Built-in virtual environment management
- Uses `pyproject.toml` as the single source of truth.

---

## 2. Structure of `pyproject.toml`
This file defines project metadata, dependencies, and tool configurations:

- **Build system:**  
  `[build-system]` uses `setuptools` and `wheel` with `setuptools.build_meta` as the backend.

- **Project metadata:**  
  `[project]` includes name, version, description, Python version, readme, and authors.

- **Production dependencies:**  
  `dependencies` lists core packages used in production (e.g., FastAPI, Uvicorn, LlamaIndex ecosystem, databases and cloud clients, utilities).

- **Optional dependency groups:**  
  `[project.optional-dependencies]` organizes installable groups:
  - **frontend:** UI/web app stack (Prisma, Jinja2, `python-jose[cryptography]`, Azure Data Lake).
  - **dataloader:** ingestion, storage, readers, workers (Redis KV/docstore, Neo4j vector store, GitHub reader, `rq`).
  - **llm-proxy:** LLM integrations (SAP AI SDK, OpenAI, Vertex AI, LangChain).
  - **test:** testing frameworks and utilities (pytest, coverage, asyncio tools, deepeval).
  - **dev:** developer tools (ruff, mypy, pre-commit).

- **Tooling configs:**  
  `[tool.setuptools.*]` for package discovery and data files; `[tool.mypy]` for type checking; `[tool.pytest.ini_options]` for test discovery.

**Note on versions:** We do not pin versions in `pyproject.toml`. Exact resolved versions are recorded in `uv.lock` to ensure reproducibility while keeping configuration flexible.

---

## 3. Dependency groups and installation
- **Production (default):** packages under `dependencies`.
- **Optional groups:** `frontend`, `dataloader`, `llm-proxy`, `test`, `dev` under `[project.optional-dependencies]`.

### Examples

---

## 4. Adding a new package (commands + manual)
### a) Using UV commands (recommended)
#### 1. Choose the target group:
Production: uv add <package>
Development: uv add --group dev <package>
Testing: uv add --group test <package>
Other optional groups: uv add --group <group> <package>
#### 2. Verify the package is placed in the correct section of pyproject.toml.
#### 3. Sync environment to resolve versions and update uv.lock:
uv sync
#### 4. Commit both pyproject.toml and uv.lock.

### b) Manual editing (supported)
#### 1. Open pyproject.toml
#### 2. Add the package under the appropriate section:
Production: append to the dependencies list.
Development: append under [project.optional-dependencies].dev.
Testing: append under [project.optional-dependencies].test.
Other groups: append under the respective key (e.g., frontend, dataloader, llm-proxy).
### 3. Save the file and sync:
uv sync
This resolves exact versions into uv.lock.
### 4. Commit both pyproject.toml and uv.lock.

---

## 5. Best practices
• Commit both files: Always commit pyproject.toml and uv.lock together.
• Do not edit uv.lock manually.
• Use groups to keep environments lean and purpose-specific.
• Run uv sync after any change (command or manual).