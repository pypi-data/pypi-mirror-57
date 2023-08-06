import subprocess
from string import Template


def execute(cmd, cwd=None):
    return subprocess.run(
        cmd,
        shell=True,
        check=True,
        cwd=cwd
    )


def render(template, dest, **kwargs):
    with open(dest, 'w') as fh:
        fh.write(
            Template(
                open(template).read()
            ).safe_substitute(**kwargs)
        )
