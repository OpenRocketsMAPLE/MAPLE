# Contributing to MAPLE

This repository is private. Access is limited to collaborators who have been granted access. Contributions are developed on branches and reviewed through pull requests.

## Propose a change

1. Create a branch from the latest `main` and make your changes there.
2. Update the [changelog](CHANGELOG.md) with a concise description of meaningful changes.
3. Push the branch and open a pull request targeting `main`. Describe the change and any relevant context for review.
4. Address review feedback on the same branch. Once the change has been reviewed and approved, an authorized collaborator can merge it.

## Changes to the license

[`MAPLE.odt`](MAPLE.odt) is the source of the license draft. After changing it, regenerate the plain-text copy and include both files in the same pull request:

```sh
python3 scripts/sync_license.py
```

Check that the files match and run the extraction tests:

```sh
python3 scripts/sync_license.py --check
python3 -m unittest discover -s tests -v
```

The pull-request check detects a draft that is out of sync. If the ODT gains an unsupported structure, such as a table or list, the extractor must be updated before the plain-text copy can be regenerated. Use the [versioning specification](docs/versioning.md) when changing the license version.

Version `0.1.0` is an unratified, non-operative draft. It does not grant permissions and must not be applied to a work.
