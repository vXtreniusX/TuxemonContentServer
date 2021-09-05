# Requests

## API
`/api/packages` — get all packages from the `packages` directory.
`/api/packages/<name>` — get specific package information
`/api/packages/<name>/releases` — get specific package's release list

### Downloading
`/packages/<name>/releases/<release>/download` — Download specified package release

# Package meta format
```
{
    "author": "author",
    "name": "mainDP",
    "short_description": "dependency test",
    "title": "Main package"
    "release": 0,
    "dependencies": [
        "reqDP"
    ],
    "repo": "http://tuxemon-content-server-dev.herokuapp.com/"
}
```
----
- `author` — Package author [recommended]
- `name` — Package's name [required]
- `title` — Displayed title of the package. [recommended]
- `short_description` — Package description [recommended]
- `release` — Latest release number [required]
- `dependencies` — Package dependencies [optional]
- `repo` — Repository URL, should be automatically added by server [required]
----
