import os
from subprocess import check_output, CalledProcessError, STDOUT, call
import logging


def run(args, shell=False, split=True):
    """
    Get command output

    :type args: list | str
    :param args: command and args
    :param shell: True if run via shell
    :param split: If true, split input into a list
    :return: Command output either as a single string or list of lines
    """
    args_string = args if isinstance(args, str) else ' '.join(args)
    logging.debug("Running %s", args_string)
    try:
        out = check_output(args, shell=shell, stderr=STDOUT)
        if out:
            logging.debug("Returned %s", out)
    except CalledProcessError as e:
        return e.returncode, e.output
    except OSError as e:
        return e.errno, e.strerror
    if split:
        return 0, [s.strip() for s in out.splitlines()]
    return 0, out.strip()


def system(args, shell=False, stdout=None, stderr=None):
    """
    Run command with arguments

    :type args: list
    :param args: command and arguments
    :param shell: Run through shell if True
    :param stdout: (optional) stdout object
    :param stderr: (optional) srderr object
    :return: True on success, False on failure
    """
    args_string = args if isinstance(args, str) else ' '.join(args)
    logging.debug("Running %s", args_string)

    try:
        with open(os.devnull, "w") as devnull:
            if not stdout:
                stdout = devnull
            if not stderr:
                stderr = devnull

            retcode = call(args, shell=shell, stdout=stdout, stderr=stderr)
            if retcode:
                logging.warning('command %s failed', args)
                return False
        return True
    except CalledProcessError as e:
        logging.warning("Command failed: %s", e)
    except OSError as e:
        logging.warning("Command failed: %s", e)
    return False
