from unittest import TextTestResult
import subprocess
import yaml


class TextTestResultWithSuccesses(TextTestResult):
    """
    This class extends TextTestResult so that successful tests get reported in `self.successes`.
    """
    def __init__(self, *args, **kwargs):
        super(TextTestResultWithSuccesses, self).__init__(*args, **kwargs)
        self.successes = []

    def addSuccess(self, test):
        super(TextTestResultWithSuccesses, self).addSuccess(test)
        self.successes.append(test)


def execute_command(command):
    completed_process = subprocess.run(command, shell=True, executable="/bin/bash",
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = dict()
    result["exit-code"] = completed_process.returncode
    result["output"] = completed_process.stdout.decode("utf-8").strip()
    result["error"] = completed_process.stderr.decode("utf-8").strip()
    return result


def parse_yaml_file(path):
    with open(path, "r") as f:
        yaml_content = yaml.full_load(f)
    return yaml_content


def nested_get(dictionary, *keys):
    value = dictionary
    for key in keys:
        try:
            value = value[key]
        except KeyError:
            value = None
    return value
