# -*- coding: utf-8 -*-
import io
import os

from pkg_resources import get_distribution, DistributionNotFound

from .pyckles import Pycklet, AutoPycklet, Pyckles  # noqa


"""Top-level package for pyckles."""

__author__ = """Markus Binsteiner"""
__email__ = "markus@frkl.io"

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:

    try:
        version_file = os.path.join(os.path.dirname(__file__), "version.txt")

        if os.path.exists(version_file):
            with io.open(version_file, encoding="utf-8") as vf:
                __version__ = vf.read()
        else:
            __version__ = "unknown"

    except (Exception):
        pass

    if __version__ is None:
        __version__ = "unknown"

finally:
    del get_distribution, DistributionNotFound


def load_default_pycklets():

    p = Pyckles(add_utility_functions_to_module=True)

    return p.module


def run_frecklets(
    *frecklets,
    inventory=None,
    run_config=None,
    context_config=None,
    extra_repos=None,
    context_type=None,
    no_exception=False,
    return_run_details=False,
    password_callback=None
):
    """Run one or several frecklets.

    If 'return_run_details' is set to 'False', only the result dict will be returned. If set to 'True',
    a tuple '(result_dict, run_details) will be returned. If 'return_run_details' is set to a string,
    that key will be used in the result dict to hold the run details, and only the dict will be returned.

    Args:
        frecklets: one or several frecklets
        inventory: an inventory to draw variable values from (in case the there are any)
        run_config: either a FrecklesRunConfig object, a dictionary with config values, or a target string (e.g. admin@example.com)
        context_config (list, str, dict): the freckles context configuration
        extra_repos (list): extra frecklet/resources repositories
        context_type (str): either 'python' or 'freck', if not provided one will be picked automatically
        no_exception (bool): does not raise exception, even if run failed
        return_run_details (bool, str): whether to, in addition to the result also return run details
        password_callback (func): a callback function that takes a single input (prompt), and returns the password

    Returns:
        dict: the registered result values of the run
    """

    from pyckles.utils import create_pyckles_context

    context = create_pyckles_context(
        context_config=context_config,
        extra_repos=extra_repos,
        context_type=context_type,
    )

    result = context.run_frecklets(
        *frecklets,
        inventory=inventory,
        run_config=run_config,
        no_exception=no_exception,
        return_run_details=return_run_details,
        password_callback=password_callback
    )
    return result


def run_pycklets(
    *pycklets,
    inventory=None,
    run_config=None,
    context_config=None,
    extra_repos=None,
    context_type=None,
    no_exception=False,
    return_run_details=False,
    password_callback=None
):
    """Run one or several pycklets.

    If 'return_run_details' is set to 'False', only the result dict will be returned. If set to 'True',
    a tuple '(result_dict, run_details) will be returned. If 'return_run_details' is set to a string,
    that key will be used in the result dict to hold the run details, and only the dict will be returned.

    Args:
        pycklets: one or several Pycklets
        inventory: an inventory to draw variable values from (in case the there are any)
        run_config: either a FrecklesRunConfig object, a dictionary with config values, or a target string (e.g. admin@example.com)
        context_config (list, str, dict): the freckles context configuration
        extra_repos (list): extra frecklet/resources repositories
        context_type (str): either 'python' or 'freck', if not provided one will be picked automatically
        no_exception (bool): does not raise exception, even if run failed
        return_run_details (bool, str): whether to, in addition to the result also return run details
        password_callback (func): a callback function that takes a single input (prompt), and returns the password

    Returns:
        dict: the registered result values of the run
    """

    from pyckles.utils import create_pyckles_context

    context = create_pyckles_context(
        context_config=context_config,
        extra_repos=extra_repos,
        context_type=context_type,
    )

    result = context.run_pycklets(
        *pycklets,
        inventory=inventory,
        run_config=run_config,
        no_exception=no_exception,
        return_run_details=return_run_details,
        password_callback=password_callback
    )
    return result
