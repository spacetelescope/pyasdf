import os

from asdf import generic_io, util


class UseInternal:
    pass


class ExternalBlockCache:
    def __init__(self):
        self._cache = {}

    def load(self, base_uri, uri):
        key = util.get_base_uri(uri)
        if key not in self._cache:
            resolved_uri = generic_io.resolve_uri(base_uri, uri)
            if resolved_uri == "" or resolved_uri == base_uri:
                return UseInternal

            from asdf import open as asdf_open

            with asdf_open(resolved_uri, lazy_load=False, copy_arrays=True) as af:
                self._cache[key] = af._blocks.blocks[0].cached_data
        return self._cache[key]


def uri_for_index(uri, index):
    parts = list(util.patched_urllib_parse.urlparse(uri))
    path = parts[2]
    dirname, filename = os.path.split(path)
    filename = os.path.splitext(filename)[0] + f"{index:04d}.asdf"
    return filename
