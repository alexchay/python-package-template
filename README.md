### Managing Multiple Python Versions With pyenv

```shell
$ pyenv install --list | grep -e "^  3\.[89].*"
$ env PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto' PYTHON_CFLAGS='-march=native -mtune=native' pyenv install -v 3.10.11
$ pyenv install -v 3.10.11
$ pyenv versions
  system
* 3.8.16 (set by ~/.pyenv/version)
  3.9.16
  3.10.11
  3.11.3
  3.12-dev
$ pyenv global 3.10.11
# activate version for the project (.python-version file in root directory)
$ pyenv local 3.10.11
```

### Python Dependency Management With poetry

```shell
$ curl -sSL https://install.python-poetry.org | POETRY_HOME=$HOME/.poetry python3 -
$ poetry config virtualenvs.prefer-active-python true --local
$ poetry install --only main
$ poetry install --with test
$ poetry run pip list
```

### Git commits syntax check, bump version

#### Integrate `commitizen`
##### Install
```shell
$ poetry add commitizen --group dev
```
##### Git commits syntax enforcing
```shell
$ poetry add pre-commit --group dev
```
To automate the Git commit verification we first need to create a configuration file .`pre-commit-config.yaml` as followed:
```yaml
repos:
    - repo: https://github.com/commitizen-tools/commitizen
      rev: v3.2.1
      hooks:
          - id: commitizen
            stages: [commit-msg]
```
Install the configuration into git hook through pre-commit
```shell
$ pre-commit install
$ pre-commit install --hook-type commit-msg
```
if manually add git hook
```shell
$ COMMIT_MSG_HOOK = '\#!/bin/bash\nMSG_FILE=$$1\ncz check - allow-abort - commit-msg-file $$MSG_FILE'
$ echo $(COMMIT_MSG_HOOK) > .git/hooks/commit-msg
$ chmod +x .git/hooks/commit-msg
```
a commit-msg file written in .git/hooks

```shell
#!/bin/bash
MSG_FILE=$1
cz check --allow-abort --commit-msg-file $MSG_FILE
```

```shell
# use commitizen to assist you with the creation of commits
$ cz commit
# only write the message to a file and not modify files and create a commit
$ cz commit --dry-run --write-message-to-file COMMIT_MSG_FILE
# show information about the cz
$ cz info
# bump semantic version based on the git log and create a tag
$ cz bump --check-consistency
# bumps the version in the files defined in version_files without creating a commit and tag on the git repository
$ cz bump --files-only
# validates that a commit message matches the commitizen schema
$ cz check
# to check a commit's message after it has already been created
$ cz check --rev-range REV_RANGE (master..HEAD)
# check a plain message
$ cz check --message MESSAGE
# show project's version
$ cz version -p
# changes for the version that was just created
$ cz changelog --dry-run "$(cz version -p)"

```

#### Integrate `bump2version`
##### Install
```shell
$ poetry add bump2version --group dev
```
##### bump a build number in version
```
$ ./bump_calver_build.sh
```
