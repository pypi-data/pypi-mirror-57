# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import logging
import os
import sys

import click
from cookiecutter.main import cookiecutter
from ruamel.yaml import YAML

from pyckles.codegen import PycklesCodegen
from freckles.utils.utils import generate_frecklet_src_jinja_env

yaml = YAML(typ="safe")

log = logging.getLogger("freckles")


@click.group()
@click.pass_context
def codegen(ctx):
    """Generate source code.

    Currently, only Python code is supported, but eventually other languages will be too.
    """

    pass


@codegen.command()
@click.option(
    "--package-name",
    "-p",
    help="the base package name",
    type=str,
    required=True,
    default="frecklets",
)
@click.option(
    "--delete-existing-package",
    "-d",
    help="delete existing package",
    is_flag=True,
    type=bool,
)
@click.option(
    "--delete-existing-path",
    help="delete base path if it exists",
    is_flag=True,
    type=bool,
)
@click.argument("path", type=str, nargs=1)
@click.option(
    "--python-3",
    help="generate Python 3.7 code (dataclasses)",
    required=False,
    default=False,
    is_flag=True,
)
@click.pass_context
def python_sources(
    ctx, path, package_name, delete_existing_package, delete_existing_path, python_3
):
    """
    Generate a Python package from the current context.

    This will generate one Python class for every frecklet under the specified package. It will also export all
    required resources for those frecklets, under <base_path>/resources.
    """

    context = ctx.obj["context"]

    if python_3:
        template_name = "python_3_src.j2"
    else:
        template_name = "python_src.j2"

    codegen = PycklesCodegen(freckles_context=context, template_name=template_name)

    codegen.export(
        path,
        package_name,
        ignore_errors=True,
        delete_existing_package=delete_existing_package,
        delete_existing_base=delete_existing_path,
    )


@codegen.command()
@click.option(
    "--template",
    "-t",
    help="the (cookiecutter) template url",
    type=str,
    required=False,
    default="gl:freckles-io/template-pyckles-project",
)
@click.option(
    "--rel-src-path",
    "-s",
    help="the relative path from the project root to where the Python sources should be generated (use this if you specify a custom template)",
    required=False,
)
@click.option(
    "--base_path",
    "-b",
    type=str,
    required=False,
    help="the base path where the project folder will sit, will be created if it does not exist. current path will be used if not specified",
)
@click.option(
    "--name", "-n", help="full name of project owner", type=str, required=True
)
@click.option(
    "--email", "-e", help="email address of project owner", type=str, required=True
)
@click.argument("project_name", nargs=1)
@click.option(
    "--description",
    "-d",
    help="short description of the project",
    type=str,
    required=False,
)
@click.option("--gitlab-user", help="gitlab username", type=str, required=True)
@click.option(
    "--package-name",
    help="the package name for the generated Pycklets",
    required=False,
    type=str,
)
@click.option(
    "--python-3",
    help="generate Python 3.7 code (dataclasses)",
    required=False,
    default=False,
    is_flag=True,
)
@click.pass_context
def python_project(
    ctx,
    base_path,
    template,
    rel_src_path,
    name,
    email,
    project_name,
    description,
    gitlab_user,
    package_name,
    python_3,
):
    """
    Generate a Python project from a cookiecutter template.

    This includes the auto-generation of 'Pycklet' classes from all the frecklets in the current context.

    Args:
        ctx: the click context
        path: the path to create the project in
    """

    context = ctx.obj["context"]
    if python_3:
        src_template = "python_3_src.j2"
    else:
        src_template = "python_src.j2"

    codegen = PycklesCodegen(freckles_context=context, template_name=src_template)

    if base_path is not None:
        base_path = os.path.realpath(base_path)
        if not os.path.exists(base_path):
            os.makedirs(base_path)

        os.chdir(base_path)
    else:
        base_path = os.getcwd()

    project_dir = os.path.join(base_path, project_name)

    if os.path.exists(project_dir):
        click.echo(
            "Project dir '{}' already exists. Doing nothing...".format(project_dir)
        )
        sys.exit(1)

    if rel_src_path is None:
        if template == "gl:freckles-io/template-pyckles-project":
            rel_src_path = "src"

    if rel_src_path:
        src_path = os.path.join(project_dir, rel_src_path)
    else:
        src_path = project_dir

    project_slug = project_name.lower().replace("-", "_").replace(" ", "_")
    if description is None:
        description = "No description available (yet)."

    if package_name is None:
        package_name = project_slug

    cookiecutter_details = {
        "full_name": name,
        "email": email,
        "project_name": project_name,
        "project_slug": project_slug,
        "project_short_description": description,
        "gitlab_user": gitlab_user,
        "package_name": package_name,
        "package_path": package_name.replace(".", os.path.sep),
    }

    cookiecutter(template, extra_context=cookiecutter_details, no_input=True)

    base_package = package_name.split(".")[0]
    base_package_path = os.path.join(src_path, base_package)
    os.makedirs(base_package_path)
    base_init_path = os.path.join(base_package_path, "__init__.py")
    if not hasattr(sys, "frozen"):
        template_dir = os.path.join(os.path.dirname(__file__), "templates")
    else:
        template_dir = os.path.join(sys._MEIPASS, "pyckles", "templates")

    jinja_env = generate_frecklet_src_jinja_env(template_dir=template_dir)
    init_template = jinja_env.get_template(name="__init__.py.base.j2")
    repl_dict = {"project_name": project_name, "name": name, "email": email}
    rendered = init_template.render(repl_dict)
    with open(base_init_path, "w") as f:
        f.write(rendered)

    codegen.export(
        src_path,
        package_name=package_name,
        ignore_errors=True,
        delete_existing_package=False,
        delete_existing_base=False,
        force=True,
    )
