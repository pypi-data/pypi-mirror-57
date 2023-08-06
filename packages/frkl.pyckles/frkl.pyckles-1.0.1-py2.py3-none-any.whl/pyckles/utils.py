# -*- coding: utf-8 -*-


def get_all_subclasses(cls):
    all_subclasses = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses


def create_pyckles_context(context_config=None, extra_repos=None, context_type=None):

    if context_type is None:
        try:
            from pyckles.contexts.python import PythonContext

            context_class = PythonContext
        except (Exception):
            from pyckles.contexts.freck import FreckContext

            context_class = FreckContext
    elif context_type == "python":
        from pyckles.contexts.python import PythonContext

        context_class = PythonContext
    elif context_type == "freck":
        from pyckles.contexts.freck import FreckContext

        context_class = FreckContext
    else:
        raise Exception("Unsupported context type: {}".format(context_type))

    context = context_class(context_config=context_config, extra_repos=extra_repos)

    return context


def find_pycklet_bases():
    from pyckles import Pycklet, AutoPycklet

    # auto load all Pycklet subclasses
    package_bases = set()
    pycklet_classes = get_all_subclasses(Pycklet)
    for p in pycklet_classes:

        if p == AutoPycklet:
            continue

        m = p.__module__
        # get base package
        pkg = ".".join(str(m).split(".")[0:-1])
        package_bases.add(pkg)

    pycklets_package_names = list(package_bases)
    return pycklets_package_names


# def find_context_repos(pycklets_package_names=None):
#
#     if pycklets_package_names is None:
#         pycklets_package_names = find_pycklet_bases()
#
#     elif isinstance(pycklets_package_names, six.string_types):
#         pycklets_package_names = [pycklets_package_names]
#
#     _base_packages = {}
#     _context_repos = []
#
#     if not pycklets_package_names:
#         raise Exception("Could not create PycklesContext, no pycklet packages/classes found.")
#         # raise FrklException(
#         #     msg="Could not create PycklesContext.",
#         #     reason="No pycklet packages/classes found.",
#         #     solution="Make sure to either import/load all Pycklet classes you want to use before creating a context, or provide the 'pycklets_package_names' argument.",
#         # )
#
#     for base_package_name in pycklets_package_names:
#
#         try:
#             mod = importlib.import_module(base_package_name)
#             resources = mod.get_resource_details()
#             _base_packages[base_package_name] = resources
#
#             for res_type, paths in resources["resources"].items():
#                 for path in paths:
#
#                     if res_type == MIXED_CONTENT_TYPE:
#                         res_path = path
#                     else:
#                         res_path = "{}::{}".format(res_type, path)
#
#                     _context_repos.append(res_path)
#
#         except (Exception) as e:
#             raise Exception(
#                 "Can't load pycklets from module path '{}': {}".format(
#                     base_package_name, e
#                 )
#             )
#
#     return _context_repos


# def augment_freckles_context_config(pycklets_package_names=None, context_config_dict=None):
#
#     repos = find_context_repos(pycklets_package_names=pycklets_package_names)
#
#     if not context_config_dict:
#         _context_config = {}
#     else:
#         _context_config = copy.deepcopy(context_config_dict)
#
#     _context_config["repos"] = repos
#
#     return _context_config
