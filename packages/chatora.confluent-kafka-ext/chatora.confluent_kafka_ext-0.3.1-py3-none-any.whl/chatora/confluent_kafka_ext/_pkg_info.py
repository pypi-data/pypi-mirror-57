__all__ = (
    '__version_info__',
    '__version__',
)


try:
    from packaging.version import (
        Version,
        parse as _parse_version,
    )
    __version_info__: Version = _parse_version('0.3.1')
    __version__: str = __version_info__.public
except ImportError:
    __version__: str = '0.3.1'
