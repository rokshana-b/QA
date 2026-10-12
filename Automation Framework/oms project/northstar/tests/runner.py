# automation-framework/runner.py
from pathlib import Path

PROJECTS = {
    "sample-project1": Path("../sample-project1"),
    "sample-project2": Path("../sample-project2"),
}

def run_project(project_name: str) -> None:
    project_dir = PROJECTS[project_name]
    tests_dir = project_dir / "tests"

    print(f"Running tests for {project_name}")
    print(f"Tests folder: {tests_dir.resolve()}")
    # A real runner could discover and execute tests here.

if __name__ == "__main__":
    run_project("sample-project1")