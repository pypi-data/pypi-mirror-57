# -*- coding: utf-8 -*-
import logging
import os
import shutil
import sys
from collections import OrderedDict
from importlib.machinery import ModuleSpec

from freckles import Freckles
from freckles.defaults import freckles_src_template_dir
from freckles.utils.utils import (
    generate_frecklet_src_jinja_env,
    convert_dataclass_type_filter,
)

log = logging.getLogger("freckles")

# adapted from: https://blog.quiltdata.com/import-almost-anything-in-python-an-intro-to-module-loaders-and-finders-f5e7b15cda47

MODULE_PATH = []


def generate_pycklets_package(
    package_name="pycklets", context_config=None, extra_repos=None, template_name=None
):

    from .codegen import PycklesCodegen

    freckles = Freckles(context_config=context_config, extra_repos=extra_repos)
    context = freckles.get_context()

    codegen = PycklesCodegen(context, template_name=template_name)
    p = codegen.generate_pycklets_package(package_name=package_name)
    return p


class PycklesCodegen(object):
    def __init__(self, freckles_context, template_name=None):

        # cc = ContextConfig(
        #     alias="codegen",
        #     config_chain={},
        #     extra_repos=frecklet_repos,
        #     use_community=False,
        #     config_unlocked=True,
        # )

        self._context = freckles_context
        self.template_dir = freckles_src_template_dir
        # if not hasattr(sys, "frozen"):
        #     self.template_dir = os.path.join(os.path.dirname(__file__), "templates")
        # else:
        #     self.template_dir = os.path.join(sys._MEIPASS, "freckles", "templates", "src")

        self.jinja_env = generate_frecklet_src_jinja_env(
            template_dir=self.template_dir,
            extra_filters={"get_dataclass_type": convert_dataclass_type_filter},
        )

        if template_name is None:
            template_name = "python_3_src.j2"

        self.template = self.jinja_env.get_template(name=template_name)

    def generate_pycklets_package(self, package_name, no_import=False):

        sys.meta_path.append(
            PyckletPackageFinder(package_name=package_name, pyckles_codegen=self)
        )

        if no_import:
            return package_name

        import importlib

        module = importlib.import_module(package_name, package=None)
        return module

    def export(
        self,
        base_path,
        package_name,
        force=False,
        ignore_errors=False,
        delete_existing_base=False,
        delete_existing_package=False,
    ):

        if os.path.exists(base_path) and delete_existing_base:
            shutil.rmtree(base_path)

        package_base = os.path.join(base_path, package_name.replace(".", os.path.sep))
        resource_path = os.path.join(package_base, "resources")

        if os.path.exists(package_base) and not delete_existing_package and not force:
            raise Exception("Package base path already exists: {}".format(package_base))
        if delete_existing_package:
            if os.path.exists(package_base):
                shutil.rmtree(package_base)
            if os.path.exists(resource_path):
                shutil.rmtree(resource_path)

        log.debug("Creating pycklet sources in: {}".format(package_base))
        self.generate_pycklet_sources(
            base_path=base_path, package_name=package_name, force=force
        )
        log.debug("Exporting resources to: {}".format(resource_path))
        self.context.export(
            dest_path=resource_path,
            delete_destination_before_copy=False,
            ignore_errors=ignore_errors,
        )

    def generate_pycklet_sources(self, package_name, base_path, force=False):

        package_base = os.path.join(base_path, package_name.replace(".", os.path.sep))

        if os.path.exists(package_base) and not force:
            raise Exception("Package base path already exists: {}".format(package_base))

        os.makedirs(package_base, exist_ok=True)

        _temp = base_path
        for token in package_name.split("."):
            _temp = os.path.join(_temp, token)
            init_file = os.path.join(_temp, "__init__.py")
            open(init_file, "a").close()

        imps = OrderedDict()

        for frecklet_name, frecklet in self.context.frecklet_index.items():

            try:

                module_name = frecklet_name.replace("-", "_")
                f_module = os.path.join(package_base, "{}.py".format(module_name))
                with open(f_module, "w") as f:
                    src = frecklet.render_template(
                        ting_repl_name="frecklet",
                        template=self.template,
                        extra_repl_dict={
                            "package_name": package_name,
                            "module_name": module_name,
                        },
                    )
                    f.write(src)
                imps[module_name] = frecklet.class_name

            except (Exception) as e:
                # log.error(e, exc_info=1)
                log.warning(
                    "Could not generate python sources for frecklet '{}': {}".format(
                        frecklet_name, e
                    )
                )

        init_file = os.path.join(package_base, "__init__.py")
        init_template = self.jinja_env.get_template(name="__init__.py.j2")
        repl_dict = {"imports": imps, "package_name": package_name}
        rendered = init_template.render(repl_dict)
        with open(init_file, "w") as f:
            f.write(rendered)

    @property
    def context(self):
        return self._context


class PycklesPackageImporter(object):
    """
    Frecklet package module loader. Executes package import code and adds the package to the
    module cache.
    """

    def __init__(self, package_name, pyckles_codegen):

        self.package_name = package_name
        self.pyckles_codegen = pyckles_codegen

    @classmethod
    def create_module(cls, spec):
        """
        Module creator. Returning None causes Python to use the default module creator.
        """
        return None

    # @classmethod
    def exec_module(self, module):
        """
        Module executor.
        """

        module_name_req = module.__name__

        if len(module_name_req) < len(self.package_name):
            # __path__ must be set even if the package is virtual, but can be set to [].
            module.__path__ = MODULE_PATH
            return module
        elif len(module_name_req) == len(self.package_name):

            for f_name, f in self.pyckles_codegen.context.frecklet_index.items():
                f_name = f_name.replace("-", "_")
                module.__dict__[f_name] = f

                def _wrapper():

                    _f_name = f_name
                    _f = f
                    import_string = "{}.{}".format(
                        self.package_name, _f_name.replace("-", "_")
                    )

                    def _proxy_constructor(**kwargs):

                        import importlib

                        i = importlib.import_module(import_string)
                        return i.__dict__[_f.class_name](**kwargs)

                    return _proxy_constructor

                module.__dict__[f.class_name] = _wrapper()

            module.__path__ = MODULE_PATH

            # TODO: use the same string here as in the template
            def class_wrapper_func(frecklet_name):
                frecklet_name = frecklet_name.replace("-", "_")

                import importlib

                module = importlib.import_module(
                    "{}.{}".format(self.package_name, frecklet_name), package=None
                )

                if not hasattr(module, "frecklet_class"):
                    return None
                return getattr(module, "frecklet_class")

            def object_wrapper_func(
                _frecklet_name, _strict=False, _exception_on_not_found=True, **vars
            ):
                cl = class_wrapper_func(frecklet_name=_frecklet_name)
                if cl is None:
                    if _exception_on_not_found:
                        raise Exception(
                            "No frecklet found with name: {}".format(_frecklet_name)
                        )
                    else:
                        return None
                if _strict:
                    return cl(**vars)
                else:
                    obj = cl()
                    for k, v in vars.items():
                        if hasattr(obj, k):
                            setattr(obj, k, v)
                    return obj

            def resource_details_wrapper_func():

                r = {}
                for path_details in self.pyckles_codegen.context._resource_repo_list:

                    path = os.path.abspath(os.path.expanduser(path_details["path"]))
                    r_type = path_details["type"]

                    r.setdefault(r_type, []).append(path)

                result = {"module_base": None, "resources_dir": None, "resources": r}
                return result

            # def freckles_context_wrapper_func():
            #
            #     return self.pyckles_codegen.context

            module.__dict__["get_class"] = class_wrapper_func
            module.__dict__["create_obj"] = object_wrapper_func
            module.__dict__["get_resource_details"] = resource_details_wrapper_func
            # module.__dict__["get_freckles_context"] = freckles_context_wrapper_func

            return module

        relative_module = module_name_req.replace(self.package_name, "")

        # don't need the dot
        frecklet_name = relative_module[1:]

        if "." in frecklet_name:
            return None

        f = self.pyckles_codegen.context.get_frecklet(frecklet_name)
        if f is None:
            f = self.pyckles_codegen.context.get_frecklet(
                frecklet_name.replace("_", "-")
            )
            if f is None:
                return None

        try:
            src = f.render_template(
                ting_repl_name="frecklet", template=self.pyckles_codegen.template
            )
            exec(src, module.__dict__)
            module.__dict__["frecklet_class"] = module.__dict__[f.class_name]
        except (Exception) as e:
            log.warning(
                "Can't create python class for '{}': {}".format(frecklet_name, e)
            )


class PyckletPackageFinder:
    """
    Frecklet package module loader finder. This class sits on `sys.meta_path` and returns the
    loader it knows for a given path, if it knows a compatible loader.
    """

    def __init__(self, package_name, pyckles_codegen):
        self.package_name = package_name
        self.pyckles_codegen = pyckles_codegen
        self.pyckles_registry = PycklesPackageImporter(
            package_name=self.package_name, pyckles_codegen=self.pyckles_codegen
        )

    def find_spec(self, fullname, path=None, target=None):
        """
        This functions is what gets executed by the loader.
        """

        if not fullname.startswith(
            self.package_name
        ) and not self.package_name.startswith(fullname):
            return None
        else:
            return ModuleSpec(fullname, self.pyckles_registry)
