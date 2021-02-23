"""
Compressor is an interface to implement extensions to the compression
module. Extensions will typically subclass the Compressor ABC and
provide that subclass as a setuptools entry point.  Decompressor
is likewise used for decompression.

Note that this interface has similar patterns to Converter.  This
interface is designed for compression and decompression of ASDF
binary array blocks, while Converter is designed for serialization
of custom Python types into the YAML tree.
"""

import abc

from ..util import get_class_name, uri_match


class Compressor(abc.ABC):
    """
    Abstract base class for plugins that compress binary data.

    Implementing classes must provide the `labels` property, and
    the `compress()` method.
    May also provide a constructor that takes kwargs that are
    set via `asdf.get_config().compression_options[label] = kwargs`.
    """
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Compressor:
            return (hasattr(C, "labels") and
                    hasattr(C, "compress"))
        return NotImplemented # pragma: no cover


    @abc.abstractproperty
    def labels(self):
        """
        Get the string labels that this Compressor
        is able to compress.

        Returns
        -------
        iterable of str
            str labels handled by this class
        """
        pass # pragma: no cover


    @abc.abstractmethod
    def compress(self, data):
        """
        Returns compressed data.
        """
        pass # pragma: no cover


class Decompressor(abc.ABC):
    """
    Abstract base class for plugins that decompress binary data.

    Implementing classes must provide the `labels` property,
    and the `decompress()` or `decompress_into()`
    methods.  May also provide a constructor that takes kwargs that are
    set via `asdf.get_config().decompression_options[label] = kwargs`.
    """
    @classmethod
    def __subclasshook__(cls, C):
        # TODO: is this the right way to enforce that a subclass define `decompress()` or `decompress_into()`?
        if cls is Compressor:
            return (hasattr(C, "labels") and
                    ( hasattr(C, "decompress") or
                      hasattr(C, "decompress_into") ))
        return NotImplemented # pragma: no cover


    @abc.abstractproperty
    def labels(self):
        """
        Get the string labels that this Compressor
        is able to decompress.

        Returns
        -------
        iterable of str
            str labels handled by this class
        """
        pass # pragma: no cover
