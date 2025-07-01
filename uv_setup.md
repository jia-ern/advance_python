# create python project + pyproject.toml file
uv init <project_name>
uv venv
.venv\Scripts\activate

# add package using uv
uv add requests

# add uv.lock
uv lock

# sync package
uv sync

# list package installed
uv pip list

# Building a Distribution
uv build
