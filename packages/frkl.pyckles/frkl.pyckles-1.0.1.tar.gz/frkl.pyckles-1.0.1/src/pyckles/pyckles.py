# -*- coding: utf-8 -*-

"""Main module."""
import abc
import importlib
from collections import Sequence

import six

from pyckles.utils import create_pyckles_context


class Pyckles(object):
    """Wrapper object to conveniently use freckles from Python code.

    If no context configuration is provided, a default one with 'silent' callback is used.

    Args:
        pkg_name (str): The name of the python package that'll hold the auto-generated frecklet classes
        context_config (dict): the freckles context configuration
        extra_repos: extra repo folders that hold frecklets or resources
        init_module (bool): whether to automatically create a Python module from the frecklets in the context
        template_name: the name of the template to use to create Python classes from frecklets
    """

    def __init__(
        self,
        pkg_name="pycklets",
        context_config=None,
        extra_repos=None,
        pyckles_context_type=None,
        init_module=True,
        template_name=None,
        add_utility_functions_to_module=False,
    ):

        self.pkg_name = pkg_name
        if not context_config:
            context_config = []
        elif isinstance(context_config, six.string_types):
            context_config = [context_config]
        elif not isinstance(context_config, Sequence):
            context_config = [context_config]
        context_config.insert(0, "callback=silent")
        self.context_config = context_config
        self.extra_repos = extra_repos
        self.pyckles_context_type = pyckles_context_type
        self.template_name = template_name
        self.add_utility_functions_to_module = add_utility_functions_to_module

        self._module = None
        self._context = None

        if init_module:
            self.module

    @property
    def module(self):

        if self._module is not None:
            return self._module

        # check if already loaded
        try:
            self._module = importlib.import_module(self.pkg_name)

            if self.add_utility_functions_to_module:
                self._module.run_pycklets = self.pyckles_context.run_pycklets
                self._module.run_frecklets = self.pyckles_context.run_frecklets

            return self._module
        except (ImportError):
            pass

        try:
            from pyckles.codegen import generate_pycklets_package

            self._module = generate_pycklets_package(
                package_name=self.pkg_name,
                context_config=self.context_config,
                extra_repos=self.extra_repos,
                template_name=self.template_name,
            )

            if self.add_utility_functions_to_module:
                self._module.run_pycklets = self.pyckles_context.run_pycklets
                self._module.run_frecklets = self.pyckles_context.run_frecklets

            return self._module
        except (Exception) as e:
            raise Exception(
                "Can't auto-generate Python code from frecklets. Most likely the 'freckles' Python package needs to be installed: {}".format(
                    e
                )
            )

    @property
    def pyckles_context(self):

        if self._context is not None:
            return self._context

        self.module  # make sure the package is generated

        self._context = create_pyckles_context(
            context_config=self.context_config,
            extra_repos=self.extra_repos,
            context_type=self.pyckles_context_type,
        )
        return self._context

    def create_pycklet(self, _frecklet_name, **vars):

        obj = self.module.create_obj(_frecklet_name, **vars)

        return obj

    def run_pycklets(
        self,
        *pycklets,
        inventory=None,
        run_config=None,
        no_exception=False,
        return_run_details=False,
        password_callback=None
    ):

        return self.pyckles_context.run_pycklets(
            *pycklets,
            inventory=inventory,
            run_config=run_config,
            no_exception=no_exception,
            return_run_details=return_run_details,
            password_callback=password_callback
        )


@six.add_metaclass(abc.ABCMeta)
class Pycklet(object):
    def __init__(self, var_names):

        self._var_names = var_names

    @abc.abstractmethod
    def frecklets(self):

        pass

    def __add__(self, other):

        if issubclass(other.__class__, Pycklet):
            return [self, other]
        elif isinstance(other, Sequence):
            result = [self]
            for o in other:
                if issubclass(o.__class__, Pycklet):
                    result.append(o)
                else:
                    raise Exception(
                        "Can't add to Pycklet, wrong type: {}".format(type(o))
                    )
            return result
        else:
            raise Exception("Can't add to Pycklet, wrong type: {}".format(type(other)))


class AutoPycklet(Pycklet):
    def __init__(self, var_names):
        super(AutoPycklet, self).__init__(var_names)

    def frecklets(self):

        _vars = {}
        for v in self._var_names:
            val = getattr(self, v)
            if val is not None:
                _vars[v] = val

        return [{self.__class__.FRECKLET_ID: _vars}]
