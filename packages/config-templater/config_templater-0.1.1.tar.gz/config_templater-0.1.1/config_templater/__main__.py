import os
import glob
from pathlib import Path

from jinja2 import Environment, BaseLoader

def get_template_paths(start_dir, extension_wildcard="*.conftpl"):
    """ Returns a list of paths of identified templates. """
    return Path(start_dir).rglob(extension_wildcard)

work_dir = os.getcwd()

# Find all files in the work_dir that are templates
conf_templates = get_template_paths(work_dir)

# Create context
ctx = {}
for k, v in os.environ.items():
    ctx[k] = v

print("Processing the following configuration templates")
for tpl in conf_templates:
    with open(str(tpl), "r") as template_file:
        # Get template as string
        template_str = "".join(template_file.readlines())
        
        # Render template 
        rendered_tpl = Environment(loader=BaseLoader).from_string(template_str).render(ctx)
        
        # Create configuration
        new_path = str(tpl).replace(".conftpl", "")
        config_path, config_file_name = os.path.split(new_path)
        print("Creating new configuration '{}' in directory '{}'".format(config_file_name, config_path))
        path = Path(new_path).write_text(str(rendered_tpl))