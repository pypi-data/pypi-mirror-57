import jinja2 as _j2
from .loader import RelativeFileLoader


class J2Scr:
    def __init__(self, **kwargs):
        self.loader = RelativeFileLoader()
        self.environment = _j2.Environment(loader=self.loader)
        self.set_options(**kwargs)

    def __getattr__(self, name):
        if hasattr(self.loader, name):
            return getattr(self.loader, name)
        elif hasattr(self.environment, name):
            return getattr(self.environment, name)
        raise AttributeError(f"Could not find {name}")

    def set_options(self, **kwargs):
        # Check all attrs are valid
        objs = (self.loader, self.environment)
        keys = set(kwargs.keys())
        valid_keys = set.union(*(set(dir(o)) for o in objs)).intersection(keys)
        invalid_keys = keys.difference(valid_keys)
        if len(invalid_keys):
            raise AttributeError(
                f"Could not find the following in the environment or loader: {invalid_keys}")
        # Set the specified options
        kvs = [[(k, v) for k, v in kwargs.items() if hasattr(o, k)] for o in objs]
        for o, kvl in zip(objs, kvs):
            for k, v in kvl:
                setattr(o, k, v)

    def render(self, template_path, **kwargs):
        template = self.environment.get_template(template_path)
        return template.render(**kwargs)

    def render_to_file(self, template_path, out_path, mode="w", **kwargs):
        with open(out_path, mode=mode) as f:
            f.write(self.render(template_path, **kwargs))
