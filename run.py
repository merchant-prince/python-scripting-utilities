#! /usr/bin/env python3

import os
import re
import sys
import shutil
import argparse
from subprocess import run


def env(filepath):
    env_regex = re.compile(r"^(?P<key>\w+)=(?P<value>.*)$")
    result = {}

    with open(filepath) as envfile:
        for line in envfile:
            line = line.strip()
            matches = env_regex.match(line).groupdict()
            result[matches["key"]] = matches["value"]

    return result


def build_image(target):
    name = "harivansh_scripting_utilities_docker_image"
    tag = "development"
    uid = os.geteuid()
    gid = os.getegid()

    run(["docker", "build",
         "--build-arg", f"USER={uid}",
         "--build-arg", f"GROUP={gid}",
         "--target", target,
         "--tag", f"{name}:{tag}",
         "."],
        check=True)

    return name, tag, uid, gid


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"Test or build (and optionally push) the current python project.")
    parser.add_argument("action", choices=("build", "test"), help="Define an action to take.")
    parser.add_argument("--rebuild", action="store_true", default=False, help="Whether to rebuild the docker image.")
    parser.add_argument("--push", action="store_true", default=False, help="Whether to push the project to pypi.")
    arguments = parser.parse_args()

    if arguments.action == "test":
        name, tag, uid, gid = build_image("test")

        run(["docker", "run",
             "--rm",
             "--user", f"{uid}:{gid}",
             f"{name}:{tag}",
             "python3", "-m", "unittest", "discover", "-s", "tests"],
            check=True)

    elif arguments.action == "build":
        dist_dirname = "dist"

        if os.path.isdir(dist_dirname):
            shutil.rmtree(dist_dirname)

        os.mkdir(dist_dirname)

        name, tag, uid, gid = build_image("build")

        run(["docker", "run",
             "--rm",
             "--user", f"{uid}:{gid}",
             "--mount", f"type=bind,source={os.getcwd()}/{dist_dirname},dst=/application/{dist_dirname}",
             f"{name}:{tag}",
             "python3", "setup.py", "sdist", "bdist_wheel"],
            check=True)

        if arguments.push:
            credentials = env(".credentials")

            run(["docker", "run",
                 "--rm",
                 "--user", f"{uid}:{gid}",
                 "--mount", f"type=bind,source={os.getcwd()}/{dist_dirname},dst=/application/{dist_dirname},readonly",
                 f"{name}:{tag}",
                 "twine", "upload",
                 "--username", credentials["USERNAME"], "--password", credentials["PASSWORD"],
                 "dist/*"],
                check=True)

    else:
        parser.print_help()
        sys.exit(1)
