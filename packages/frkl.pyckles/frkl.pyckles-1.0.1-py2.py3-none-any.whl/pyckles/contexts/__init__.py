# -*- coding: utf-8 -*-
import abc
import copy
from collections import Sequence

import six


class PycklesRunException(Exception):
    def __init__(self, msg=None, run_info=None):

        self._run_info = run_info
        if msg is None:
            if run_info is None:
                msg = "n/a"
            else:
                e = run_info.exception
                if e:
                    if hasattr(e, "message"):
                        msg = e.message
                    else:
                        msg = str(e)

        super(PycklesRunException, self).__init__(msg)


@six.add_metaclass(abc.ABCMeta)
class PycklesContext(object):
    def __init__(self, context_config=None, extra_repos=None):
        if not context_config:
            context_config = []
        elif isinstance(context_config, six.string_types):
            context_config = [context_config]
        elif not isinstance(context_config, Sequence):
            context_config = [context_config]
        context_config.insert(0, "callback=silent")
        self._context_config = context_config

        if not extra_repos:
            extra_repos = []
        elif isinstance(extra_repos, six.string_types):
            extra_repos = [extra_repos]
        self.extra_repos = extra_repos

    @property
    def debug(self):

        return self._debug

    @property
    def context_config(self):

        return self._context_config

    def run_pycklets(
        self,
        *pycklets,
        inventory=None,
        run_config=None,
        no_exception=False,
        return_run_details=False,
        password_callback=None,
    ):
        """Run one or several pycklets.

        If 'return_run_details' is set to 'False', only the result dict will be returned. If set to 'True',
        a tuple '(result_dict, run_details) will be returned. If 'return_run_details' is set to a string,
        that key will be used in the result dict to hold the run details, and only the dict will be returned.

        Args:
            pycklets: one or several Pycklets
            inventory: an inventory to draw variable values from (in case the there are any)
            run_config: either a FrecklesRunConfig object, a dictionary with config values, or a target string (e.g. admin@example.com)
            no_exception (bool): does not raise exception, even if run failed
            return_run_details (bool, str): whether to, in addition to the result also return run details
            password_callback (func): a callback function that takes a single input (prompt), and returns the password

        Returns:
            dict: the registered result values of the run
        """

        temp = []
        for p in pycklets:
            if not isinstance(p, Sequence):
                p = [p]
            temp.extend(p)
        pycklets = temp

        frecklet_list = []
        for p in pycklets:
            frecklet_list.extend(p.frecklets())

        return self.run_frecklets(
            *frecklet_list,
            inventory=inventory,
            run_config=run_config,
            no_exception=no_exception,
            return_run_details=return_run_details,
            password_callback=password_callback,
        )

    def run_frecklets(
        self,
        *frecklets,
        inventory=None,
        run_config=None,
        no_exception=False,
        return_run_details=False,
        password_callback=None,
    ):
        """Run one or several frecklets.

        If 'return_run_details' is set to 'False', only the result dict will be returned. If set to 'True',
        a tuple '(result_dict, run_details) will be returned. If 'return_run_details' is set to a string,
        that key will be used in the result dict to hold the run details, and only the dict will be returned.

        Args:
            pycklets: one or several Pycklets
            inventory: an inventory to draw variable values from (in case the there are any)
            run_config: either a FrecklesRunConfig object, a dictionary with config values, or a target string (e.g. admin@example.com)
            no_exception (bool): does not raise exception, even if run failed
            return_run_details (bool, str): whether to, in addition to the result also return run details
            password_callback (func): a callback function that takes a single input (prompt), and returns the password

        Returns:
            dict: the registered result values of the run
        """

        result, run_info = self._run(
            frecklet_list=frecklets,
            inventory=inventory,
            run_config=run_config,
            password_callback=password_callback,
        )
        if not result["success"] and not no_exception:
            # TODO: error info
            if run_info:
                raise PycklesRunException(run_info=run_info)
            raise PycklesRunException("Run failed")

        elif result["success"] and not return_run_details:
            return result["result"]

        if isinstance(return_run_details, bool):
            return (result["result"], run_info)
        elif isinstance(return_run_details, six.string_types):
            r = copy.deepcopy(result["result"])
            if return_run_details in r.keys():
                raise Exception(
                    "Key '{}' can't be used as key for return details in this run, because result already contains it.".format(
                        return_run_details
                    )
                )
            r[return_run_details] = result
            return r
        else:
            raise Exception(
                "Invalid value for 'return_run_details' argument: {}".format(
                    return_run_details
                )
            )

    @abc.abstractmethod
    def _run(
        self, frecklet_list, inventory=None, run_config=None, password_callback=None
    ):

        pass
