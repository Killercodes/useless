# useless
## why to remember commands ?

useless is a tool that runs command in the CLI with buttons click, so that you don't have recall the commands.

It uses the embeded json to dynamically create buttons that executes commands on click.

```json
{

    "docker System Purge": {
        "cmd": "docker system prune -f",
        "tab": "Docker"
    },
     "docker Builder Purge": {
        "cmd": "docker builder prune -f",
        "tab": "Docker"
    },
     "docker image Purge": {
        "cmd": "docker image prune -f",
        "tab": "Docker"
    },
    "docker system df": {
        "cmd": "docker system df",
        "tab": "Docker"
    },
    "docker info": {
        "cmd": "docker info",
        "tab": "Docker"
    },
```

Here the command should have an labled and a "cmd" to store the command to execute. the "tab" is used to organize the buttons in tabs.

In case the command needs additionl parameters we can create the "parameter" key and either prepend or append it to command thene the application will prompt you for additional parameter when you cliekc the button
```json
    "dir": {
        "cmd": "dir <additionalparameter>",
        "tab": "CMD",
        "parameter":"<additionalparameter>"
    },
```
