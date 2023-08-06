# -*- coding: utf-8 -*-
from freckles import Freckles
from frutils import special_dict_to_dict
from pyckles.contexts import PycklesContext


class PythonCachedContext(PycklesContext):
    """A PycklesContext that re-uses an existing freckles context object.
    """

    def __init__(self, freckles_context):

        context_config = [freckles_context._config._config_dict]
        extra_repos = freckles_context._config._extra_repos

        super(PythonCachedContext, self).__init__(
            context_config=context_config, extra_repos=extra_repos
        )

        self._context = freckles_context

    @property
    def freckles_context(self):

        return self._context

    def _run(
        self, frecklet_list, inventory=None, run_config=None, password_callback=None
    ):

        frecklet = self._context.load_frecklet(frecklet_list)[0]

        fx = frecklet.create_frecklecutable(context=self._context)

        result = fx.run_frecklecutable(
            inventory=inventory,
            run_config=run_config,
            password_callback=password_callback,
        )
        return (
            {"result": special_dict_to_dict(result.result), "success": result.success},
            result,
        )


class PythonContext(PycklesContext):
    """A PycklesContext that uses the freckles python library to run frecklets.
    """

    def __init__(self, context_config=None, extra_repos=None, alias=None):

        super(PythonContext, self).__init__(
            context_config=context_config, extra_repos=extra_repos
        )

        if alias is None:
            alias = "pyckles"

        freckles = Freckles(
            context_config=self.context_config,
            extra_repos=extra_repos,
            default_context_name=alias,
        )
        self._context = freckles.get_context(alias)

    @property
    def freckles_context(self):

        return self._context

    def _run(
        self, frecklet_list, inventory=None, run_config=None, password_callback=None
    ):

        frecklet = self._context.load_frecklet(frecklet_list)[0]

        fx = frecklet.create_frecklecutable(context=self._context)

        result = fx.run_frecklecutable(
            inventory=inventory,
            run_config=run_config,
            password_callback=password_callback,
        )
        return (
            {"result": special_dict_to_dict(result.result), "success": result.success},
            result,
        )
