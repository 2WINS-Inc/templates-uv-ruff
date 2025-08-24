# uv + Ruff Template

## Prerequisites

Install [uv](https://docs.astral.sh/uv/) if you haven't already.

For MacOS users, use the following command to install [uv](https://docs.astral.sh/uv/):

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## How to use this template?

Install the necessary dependencies and setup pre-commit hooks

```shell
uv sync
uv run pre-commit install
```

Run sample application

```shell
PYTHONPATH=. uv run app --name World
```

Run tests

```shell
uv run pytest
```

## Installing recommended VSCode extensions

1. Open this repository in VSCode and press `Cmd + Shift + X` to open the extensions panel.
2. Search for `@recommended` in the search bar for the recommended extensions.
3. Click on the `Install Workspace Recommended Extensions` button to install all the recommended extensions.
