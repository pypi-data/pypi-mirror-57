from jinja2.loaders import BaseLoader
from jinja2.exceptions import TemplateNotFound
from pathlib import Path


class RelativeFileLoader(BaseLoader):
    """Imitates FileSystemLoader but is always relative and allows eg `..`."""
    def __init__(self, encoding="utf-8"):
        self.encoding = encoding

    def get_source(self, environment, template):
        p = Path(template)
        if not p.is_file():
            raise TemplateNotFound(template)

        contents = open(p, mode="r", encoding=self.encoding).read()

        mtime = p.stat().st_mtime

        def uptodate():
            try:
                return p.stat().st_mtime == mtime
            except OSError:
                return False
        return contents, p.name, uptodate
