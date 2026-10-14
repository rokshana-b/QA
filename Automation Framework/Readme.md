# Shared Automation Framework

This folder contains reusable tools and setup for running automated tests across the sample QA projects. Project-specific pages, tests, configuration, and test data live in their respective project folders.

## Example structure

```text
qa/
├── automation_framework/
│   ├── README.md
│   └── shared helpers and framework files
├── sample-project1/
│   ├── config/
│   ├── pages/
│   └── tests/
└── sample-project2/
    ├── config/
    ├── pages/
    └── tests/
```

## Framework responsibilities

The shared framework may provide:

- Browser and test-runner setup
- Reusable helpers and common page components
- Shared reporting and logging
- A consistent way to load each project’s configuration

Keep project-specific behavior in that project’s folder. For example, Project 1’s homepage page object belongs in `sample-project1/pages/`.

## Technology

This sample uses Python, pytest, and Playwright. The framework is a starting point; add dependencies and setup instructions here as the implementation takes shape.

## Running tests

Run tests from the repository root and specify the project’s test folder. For example:

```bash
python -m pytest qa/sample-project1/tests/
```

Update the command if your folder names or test-runner setup differ. 