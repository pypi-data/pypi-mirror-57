# -*- coding: utf-8 -*-
import json
import logging
import os
import re
import subprocess
import sys
import time
from collections import Mapping
from threading import Thread, Event
from plumbum import local
from six import string_types

try:
    from queue import Queue
except (Exception):
    # Python 2.7
    from Queue import Queue

from pyckles.contexts import PycklesContext

log = logging.getLogger("freckles")

FRECK_PATH = os.path.realpath(
    os.path.join(os.path.dirname(__file__), "..", "external", "freck", "freck")
)


def cleanup_string(line):
    regex = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")
    return regex.sub("", line)


class PipeReader(Thread):
    def __init__(self, _fd):

        super(PipeReader, self).__init__()
        self._fd = _fd
        self._queue = Queue()
        self._stop_event = Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):

        for line in iter(self._fd.readline, None):
            if line:
                self._queue.put(line.decode("UTF-8"))
            else:
                if self.stopped():
                    break


class FreckContext(PycklesContext):
    def __init__(
        self,
        context_config=None,
        extra_repos=None,
        update_freckles=False,
        freckles_channel="stable",
        **kwargs
    ):

        super(FreckContext, self).__init__(
            context_config=context_config, extra_repos=extra_repos
        )
        self._update_freckles = update_freckles
        self._freckles_channel = freckles_channel

    def _run(
        self, frecklet_list, inventory=None, run_config=None, password_callback=None
    ):

        if password_callback is not None:
            raise Exception(
                "Can't change password callback for 'FreckContext', use 'PythonContext' instead if possible."
            )

        freck_args = ["freckles"]
        # freck_args = []

        if isinstance(run_config, string_types):
            freck_args.append("--target")
            freck_args.append(run_config)
        elif isinstance(run_config, Mapping):
            host = run_config.get("host", "localhost")
            user = run_config.get("user", None)
            if user is None:
                target_string = host
            else:
                target_string = "{}@{}".format(user, host)

            port = run_config.get("port", None)
            if port is not None:
                target_string = "{}:{}".format(target_string, port)

            freck_args.append("--target")
            freck_args.append(target_string)

            if "become_pass" in run_config.keys():
                raise Exception(
                    "'become_pass' provided, currently it is not possible to use 'become_pass' and 'login_pass' with the 'freck' pyckles context."
                )

            if "login_pass" in run_config.keys():
                raise Exception(
                    "'login_pass' provided, currently it is not possible to use 'become_pass' and 'login_pass' with the 'freck' pyckles context."
                )

            if "ssh_key" in run_config.keys():
                raise Exception(
                    "'ssh_key' provided, currently it is not possible to use 'ssh_key' with the 'freck' pyckles context."
                )

            if "elevated" in run_config.keys() and run_config["elvated"] is True:
                freck_args.append("--elevated")
            elif "elevated" in run_config.keys() and run_config["elvated"] is False:
                freck_args.append("--not-elevated")

        for c in self.context_config:
            freck_args.append("--context")
            freck_args.append(c)

        freck_args.append("--context")
        freck_args.append("use_stderr=true")
        freck_args.append("--result")
        freck_args.append("json")

        for er in self.extra_repos:
            freck_args.append("--repo")
            freck_args.append(er)

        freck_args.append("read-stdin")

        freck = local[FRECK_PATH]
        # freck = local["/home/markus/.local/share/freckles/bin/freckles"]

        frecklet_data = json.dumps(frecklet_list)

        try:
            run_env = os.environ.copy()
            run_env["SILENT"] = "true"
            run_env["FRECK_HIDE_CURSOR"] = "false"

            if self._update_freckles is True:
                run_env["UPDATE"] = "true"
            run_env["VERSION"] = self._freckles_channel

            process = freck.popen(
                freck_args,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=run_env,
            )
            process.stdin.write(frecklet_data.encode(encoding="UTF-8"))
            process.stdin.close()

            stdout_reader = PipeReader(process.stdout)
            stderr_reader = PipeReader(process.stderr)

            stdout_reader.start()
            stderr_reader.start()

            stdout = []
            run_log = []

            while process.poll() is None:
                while not stderr_reader._queue.empty():
                    line = stderr_reader._queue.get()
                    run_log.append(line)
                    sys.stdout.write(line)

                # if not stdout_reader._queue.empty():
                #     line = stdout_reader._queue.get()
                #     stdout.append(line)
                #     sys.stdout.write(line)
                time.sleep(0.2)

            process.wait()
            stdout_reader.stop()
            stderr_reader.stop()
            stdout_reader.join()
            stderr_reader.join()

            while not stderr_reader._queue.empty():
                line = stderr_reader._queue.get()
                sys.stdout.write(line)
                run_log.append(line)
            run_log = "".join(run_log)
            while not stdout_reader._queue.empty():
                line = stdout_reader._queue.get()
                if not line:
                    continue
                line = line.strip()
                if not line.startswith("{") or not line.endswith("}"):
                    continue
                # print("XXXX {} XXX".format(line))
                stdout.append(line)
            stdout = "".join(stdout)

            rc = process.returncode

            if rc != 0:
                # success = False
                raise Exception(
                    "freckles run exit code non-zero ({}):\n\n{}\n\n{}".format(
                        rc, stdout, run_log
                    )
                )
            else:
                success = True

            stdout = cleanup_string(stdout).strip()

            if not stdout:
                result = {}
            else:
                result = json.loads(stdout)["value"]

            return {"result": result, "success": success}, None

        except (Exception) as e:
            raise e
