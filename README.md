### Using the Defaults
values from `cookiecutter.json` will be overridden by values from `.cookiecutterrc`
```
default_context:
    full_name: "Full Name"
    email: "me@email.com"
    github_username: "user"
abbreviations:
    pp: https://github.com/audreyfeldroy/cookiecutter-pypackage.git
    gh: https://github.com/{0}.git
    gl: https://gl.example.com/{0}.git
```



### Python Dependency Management With poetry

```shell
task poetry-install
task install
```

### Git commits syntax check, bump version
##### Git commits syntax enforcing
```shell
task pre-commit-install
```


#### Bump "SemVer "version
```shell
task bump-semver-patch
task bump-semver-minor
```

#### Bump "CalVer "version
```shell
task bump-calver
```