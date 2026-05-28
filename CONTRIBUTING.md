# Contributing to the BambooHR Python SDK

Thank you for your interest in contributing! By submitting a pull request, you agree that your contributions will be licensed under the [MIT License](LICENSE) that covers this project.

## Bug Reports and Feature Requests

Please use the [issue tracker](https://github.com/BambooHR/bhr-api-python/issues) to report bugs or request features.

## How to contribute

1. Open an issue first to discuss significant changes.
2. Fork the repository and create a feature branch.
3. Make your changes, keeping pull requests focused on a single topic.
4. Follow the existing code style and conventions.
5. Add or update tests for any new or changed functionality.
6. If updating the README, update the corresponding mustache template in `templates-python/` and run `make generate` to regenerate.
7. Ensure all tests and checks pass before submitting:

```bash
# Run the test suite
pytest

# Run specific tests
pytest tests/path/to/test_file.py
pytest tests/path/to/test_file.py::test_method_name

# Type checking
mypy bamboohr_sdk/

# Linting
ruff check bamboohr_sdk/ tests/
```

8. Open a pull request with a clear description of the change.

## Releasing

Publishing is automated via GitHub Actions using PyPI [Trusted Publishing](https://docs.pypi.org/trusted-publishers/) (OIDC). No API tokens are stored in the repo.

### TestPyPI (automatic)

Every merge to `master` triggers [`publish-testpypi.yml`](.github/workflows/publish-testpypi.yml), which builds the package and publishes to [TestPyPI](https://test.pypi.org/project/bamboohr-sdk/). Re-merges without a version bump are skipped (not failed) via `skip-existing`.

Verify a TestPyPI release locally:

```bash
pip install --index-url https://test.pypi.org/simple/ \
            --extra-index-url https://pypi.org/simple/ \
            bamboohr-sdk
```

### PyPI (tag-driven)

1. Bump `version` in `pyproject.toml` via PR and merge to `master`. The `classify-semver` make target can determine the appropriate bump:
   ```bash
   make classify-semver OLD=specs/public.yaml NEW=/tmp/new.yaml APPLY=true
   ```
2. After the TestPyPI publish completes, validate the package against a real consumer.
3. Tag the release commit and push:
   ```bash
   git tag v1.2.3
   git push origin v1.2.3
   ```
4. [`publish-pypi.yml`](.github/workflows/publish-pypi.yml) runs. It verifies the tag matches `pyproject.toml`, then waits for approval on the `pypi` GitHub environment before publishing.
5. Approve the deployment in the GitHub Actions UI. The package will appear at https://pypi.org/project/bamboohr-sdk/.

### PyPI / TestPyPI account credentials

Day-to-day publishing does not need credentials — OIDC handles auth. Credentials are only needed to manage the project in the PyPI web UI (e.g., updating the trusted publisher config or managing maintainers). The shared BambooHR PyPI and TestPyPI account credentials are stored in **Vault**.

## Terms

Use of the BambooHR API is subject to the [BambooHR Developer Terms of Service](https://www.bamboohr.com/legal/developer-terms-of-service).
