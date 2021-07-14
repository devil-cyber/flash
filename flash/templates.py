from jinja2 import Environment, FileSystemLoader


def get_templates_env(template_dir):
    return Environment(loader=FileSystemLoader(template_dir), autoescape=(["html", "xml"]))
