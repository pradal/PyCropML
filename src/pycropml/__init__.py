# {# pkglts, base

from . import version
# {#pkglts,
__import__('pkg_resources').declare_namespace(__name__)
# #}
__version__ = version.__version__

# #}
