from fabric.api import local
from jinja2 import Environment, FileSystemLoader


template_env = Environment(
    loader=FileSystemLoader('.'),
    extensions=['jinja2.ext.with_']
)


def build():
    template = template_env.get_template('source/index.html')
    rendered_template = template.render()
    with open('presentation/index.html', 'wb') as fh:
        fh.write(rendered_template)


def publish():
    build()
    local('ghp-import -p presentation')
