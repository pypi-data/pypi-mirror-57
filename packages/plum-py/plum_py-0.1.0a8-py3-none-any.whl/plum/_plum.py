# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Packable/Unpacked bytes base class."""

import functools

from ._dump import Dump

from ._exceptions import (
    ExcessMemoryError,
    ImplementationError,
    InsufficientMemoryError,
    PackError,
    SizeError,
    UnpackError,
)
from ._plumtype import PlumType


def _abbreviate_repr(item):
    rep = repr(item)
    if len(rep) > 30:
        rep = rep[0:27] + '...'
    return rep


class SizeProperty:

    """Size in bytes of packed plum instance."""

    def __get__(self, obj, objtype):
        nbytes = objtype.__nbytes__

        if nbytes is None:
            if obj is None:
                raise SizeError(f'{objtype.__name__!r} instance sizes vary')

            nbytes = len(pack(obj))

        return nbytes


class PackMethod:

    """Pack class/instance method facilitator."""

    def __init__(self, method):
        self.method = method.__func__

    def __get__(self, obj, objtype):
        if obj is None:
            method = functools.partial(self.method, objtype)
        else:
            method = functools.partial(self.method, objtype, item=obj)

        return method


class Plum:

    """Packable/Unpacked bytes base class."""

    __nbytes__ = None

    nbytes = SizeProperty()

    @classmethod
    def __unpack__(cls, buffer, offset, limit, dump, parent):
        raise NotImplementedError(f'{cls.__name__!r} does not support plum.unpack()')

    @classmethod
    def __pack__(cls, buffer, offset, value, dump):
        raise NotImplementedError(f'{cls.__name__!r} does not support plum.pack()')

    def __baserepr__(self):
        raise NotImplementedError(f'{type(self).__name__!r} does not support repr()')

    def __repr__(self):
        return f'{type(self).__name__}({self.__baserepr__()})'

    @classmethod
    def __view__(cls, buffer, offset=0):
        """Create plum view of bytes buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. ``bytes``, ``bytearray``, ``memoryview``)
        :param int offset: byte offset

        """
        raise TypeError(f'{cls.__name__!r} does not support view()')

    @property
    def dump(self):
        """Packed bytes summary.

        :returns: summary table of view detailing bytes and layout
        :rtype: str

        """
        dump = Dump()
        _pack(bytearray(), 0, (self,), {}, dump)
        return dump

    @PackMethod
    @classmethod
    def pack(cls, item):  # pylint: disable=no-self-argument
        """Pack item as bytes.

        :param object item: packable item
        :returns: bytes buffer
        :rtype: bytearray

        For example:

            >>> from plum.int.little import UInt16
            >>> # use as class method (pass a value)
            >>> UInt16.pack(2)
            bytearray(b'\x02\x00')
            >>> # use as instance method (pass value to constructor))
            >>> UInt16(2).pack()
            bytearray(b'\x02\x00')

        """
        return pack(cls, item)

    @PackMethod
    @classmethod
    def pack_and_dump(cls, item):  # pylint: disable=no-self-argument
        """Pack item as bytes and produce bytes summary.

        :param object item: packable item
        :returns: bytes buffer, packed bytes summary
        :rtype: bytearray, Dump

        For example:

            >>> from plum.int.little import UInt16
            >>> # use as class method (pass a value as last argument)
            >>> membytes, dump = UInt16.pack_and_dump(2)
            >>> membytes
            bytearray(b'\x02\x00')
            >>> print(dump)
            +--------+-------+-------+--------+
            | Offset | Value | Bytes | Type   |
            +--------+-------+-------+--------+
            | 0      | 2     | 02 00 | UInt16 |
            +--------+-------+-------+--------+
            >>> # use as instance method (pass value to constructor))
            >>> membytes, dump = UInt16(2).pack_and_dump()
            >>> membytes
            bytearray(b'\x02\x00')
            >>> print(dump)
            +--------+-------+-------+--------+
            | Offset | Value | Bytes | Type   |
            +--------+-------+-------+--------+
            | 0      | 2     | 02 00 | UInt16 |
            +--------+-------+-------+--------+

        """
        return pack_and_dump(cls, item)

    @PackMethod
    @classmethod
    def pack_into(cls, buffer, offset, item):  # pylint: disable=no-self-argument
        r"""Pack item as bytes into a buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytearray, memoryview)
        :param int offset: start location within bytes buffer
        :param object item: packable item

        For example:

            >>> from plum.int.little import UInt8
            >>>
            >>> buffer = bytearray(4)
            >>> # use as class method (pass a value as last argument)
            >>> UInt8.pack_into(buffer, 1, 0x11)
            >>> # use as instance method (pass value to constructor))
            >>> UInt8(0x12).pack_into(buffer, 2)
            >>> buffer
            bytearray(b'\x00\x11\x12\x00')

        """
        pack_into(buffer, offset, cls, item)

    @PackMethod
    @classmethod
    def pack_into_and_dump(cls, buffer, offset, item):  # pylint: disable=no-self-argument
        r"""Pack item as bytes into a buffer and produce bytes summary.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytearray, memoryview)
        :param int offset: start location within bytes buffer
        :param object item: packable item
        :returns: packed bytes summary
        :rtype: Dump

        For example:

            >>> from plum.int.little import UInt8
            >>>
            >>> buffer = bytearray(4)
            >>> # use as class method (pass a value as last argument)
            >>> dump = UInt8.pack_into_and_dump(buffer, 1, 0x11)
            >>> print(dump)
            +--------+-------+-------+-------+
            | Offset | Value | Bytes | Type  |
            +--------+-------+-------+-------+
            | 1      | 17    | 11    | UInt8 |
            +--------+-------+-------+-------+
            >>> # use as instance method (pass value to constructor))
            >>> dump = UInt8(0x12).pack_into_and_dump(buffer, 2)
            >>> print(dump)
            +--------+-------+-------+-------+
            | Offset | Value | Bytes | Type  |
            +--------+-------+-------+-------+
            | 2      | 18    | 12    | UInt8 |
            +--------+-------+-------+-------+
            >>> buffer
            bytearray(b'\x00\x11\x12\x00')

        """
        return pack_into_and_dump(buffer, offset, cls, item)

    @classmethod
    def unpack(cls, buffer):
        r"""Unpack item from bytes.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
        :returns: unpacked value
        :rtype: object (cls or type associated with cls)
        :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

        For example:
            >>> from plum.int.little import UInt16
            >>> UInt16.unpack(b'\x01\x02')
            513

        """
        return unpack(cls, buffer)

    @classmethod
    def unpack_and_dump(cls, buffer):
        r"""Unpack item from bytes and produce packed bytes summary.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
        :returns: tuple of (unpacked value, bytes summary)
        :rtype: object (cls or type associated with cls), Dump
        :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

        For example:
            >>> from plum.int.little import UInt16
            >>> value, dump = UInt16.unpack_and_dump(b'\x01\x02')
            >>> value
            513
            >>> print(dump)
            +--------+-------+-------+--------+
            | Offset | Value | Bytes | Type   |
            +--------+-------+-------+--------+
            | 0      | 513   | 01 02 | UInt16 |
            +--------+-------+-------+--------+

        """
        return unpack_and_dump(cls, buffer)

    @classmethod
    def unpack_from(cls, buffer, offset=None):
        r"""Unpack item from within a bytes buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
        :param int offset: starting byte offset (``None`` indicates current file position)
        :returns: unpacked value
        :rtype: object (cls or type associated with cls)
        :raises: ``UnpackError`` if insufficient bytes or value error

        For example:
            >>> from plum.int.little import UInt8
            >>> buffer = b'\x99\x01\x99'
            >>> UInt8.unpack_from(buffer, offset=1)
            1

        """
        return unpack_from(cls, buffer, offset)

    @classmethod
    def unpack_from_and_dump(cls, buffer, offset=None):
        """Unpack item from within a bytes buffer and produce packed bytes summary.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
        :param int offset: starting byte offset (``None`` indicates current file position)
        :returns: tuple of (unpacked items, bytes summary)
        :rtype: Plum (or tuple of Plum, or dict of Plum, dependent on ``fmt``), Dump
        :raises: ``UnpackError`` if insufficient bytes, or value error

        For example:
            >>> from plum.int.little import UInt8
            >>> buffer = b'\x99\x01\x99'
            >>> value, dump = UInt8.unpack_from_and_dump(buffer, offset=1)
            >>> value
            1
            >>> print(dump)
            +--------+-------+-------+-------+
            | Offset | Value | Bytes | Type  |
            +--------+-------+-------+-------+
            | 1      | 1     | 01    | UInt8 |
            +--------+-------+-------+-------+

        """
        return unpack_from_and_dump(cls, buffer, offset)

    @classmethod
    def view(cls, buffer, offset=0):
        """Create plum view of bytes buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview)
        :param int offset: byte offset

        For example:
            >>> from plum.int.little import UInt16
            >>> buffer = b'\x01\x02\x03\x04'
            >>> value = UInt16.view(buffer, offset=1)
            >>> value
            <view at 0x1: UInt16(770)>
            >>> value == 770
            True

        """
        return cls.__view__(buffer, offset)


def getbytes(buffer, offset, nbytes, limit, dump, cls):
    """Get bytes from buffer.

    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
    :param int offset: offset into bytes buffer
    :param int nbytes: bytes to consume (``None`` returns remainder)
    :param int limit: max number of bytes to consume (``None`` indicates no limit)
    :param Dump dump: bytes summary dump (``None`` skips dump annotation)
    :param type cls: plum type of item that consumed bytes are for
    :returns: tuple of (requested bytes, offset, limit)
    :rtype: bytes-like, int, int or None

    """
    if limit is not None:
        nbytes = limit if (nbytes is None or (limit < nbytes)) else nbytes
        limit -= nbytes

    if nbytes is None:
        try:
            chunk = buffer[offset:]
        except TypeError:
            chunk = buffer.read()
        else:
            offset += len(chunk)

        if dump:
            dump.cls = cls
            dump.memory = chunk

    else:
        start = offset
        offset += nbytes
        try:
            chunk = buffer[start: offset]
        except TypeError:
            chunk = buffer.read(nbytes)

        if len(chunk) < nbytes:
            if dump:
                dump.cls = cls
                dump.value = '<insufficient bytes>'
                if len(chunk) > 16:
                    dump.add_extra_bytes('', chunk)
                else:
                    dump.memory = chunk

            cls_name = '' if cls is None else f'{cls.__name__} '

            unpack_shortage = (
                f'{nbytes - len(chunk)} too few bytes to unpack {cls_name}'
                f'({nbytes} needed, only {len(chunk)} available)')

            raise InsufficientMemoryError(unpack_shortage)

        if dump:
            dump.cls = cls
            dump.memory = chunk

    return chunk, offset, limit


def _pack(buffer, offset, items, kwargs, dump):
    # pylint: disable=too-many-branches, too-many-nested-blocks, too-many-statements
    original_dump = dump
    try:
        cls = None
        for item in items:
            if cls is None:
                if isinstance(item, PlumType):
                    cls = item
                    continue

                if isinstance(item, Plum):
                    cls = type(item)
                else:
                    try:
                        # get PlumType from the PlumView instance
                        cls = item.__type__
                    except AttributeError:
                        # not a PlumView instance, must be (cls, item) pair
                        try:
                            cls, item = item
                        except (TypeError, ValueError):
                            # TypeError -> not iterable, ValueError -> wrong size
                            if dump:
                                dump.add_row(
                                    value=str(item), cls=type(item).__name__ + ' (invalid)')
                            raise TypeError('value specified without a plum type')

                        if not isinstance(cls, PlumType):
                            if dump:
                                cls = cls.__name__ if isinstance(cls, type) else str(item)
                                dump.add_row(value=str(item), cls=cls + ' (invalid)')
                            raise TypeError('invalid plum type')

            if isinstance(item, PlumType):
                if dump:
                    dump.add_row(cls=cls, value='(missing)')
                raise TypeError('plum type specified without a value')

            if dump:
                dump = dump.add_row(cls=cls)
                dump.indent = -1

            offset = cls.__pack__(buffer, offset, item, dump)
            cls = None
            if dump:
                dump.rows[-1].last = True

        if cls is not None:
            if dump:
                dump.add_row(cls=cls, value='(missing)')
            raise TypeError('plum type specified without a value')

        for name, item in kwargs.items():
            if dump:
                dump = dump.add_row(access=name)

            if isinstance(item, Plum):
                offset = item.__pack__(buffer, offset, item, dump)
            else:
                try:
                    # get PlumType from the PlumView instance
                    cls = item.__type__
                except AttributeError:
                    # not a PlumView instance, must be (cls, item) pair
                    try:
                        cls, item = item
                    except (TypeError, ValueError):
                        # TypeError -> not iterable, ValueError -> wrong size
                        if dump:
                            dump.cls = type(item).__name__ + ' (invalid)'
                            dump.value = str(item)
                        raise TypeError('value specified without a plum type')

                    if not isinstance(cls, PlumType):
                        if dump:
                            cls = cls.__name__ if isinstance(cls, type) else str(cls)
                            dump.cls = cls + ' (invalid)'
                            dump.value = str(item)
                        raise TypeError('invalid plum type')

                offset = cls.__pack__(buffer, offset, item, dump)

            if dump:
                dump.rows[-1].last = True

    except Exception as exc:
        if original_dump:
            unexpected_exception = (
                f"\n\n{original_dump}\n\n"
                f"{type(exc).__name__} occurred during pack operation:"
                f"\n\n{exc}")

            raise PackError(unexpected_exception)

        raise


def pack(*items, **kwargs):
    r"""Pack items as bytes.

    :param items: packable types and values
    :type items: tuple of plum types and/or values
    :param kwargs: packable items
    :type kwargs:  {name: plum instance} pairs
    :returns: bytes buffer
    :rtype: bytearray

    For example:

        >>> from plum import pack
        >>> from plum.int.little import UInt8, UInt16
        >>> pack(UInt8, 1, UInt16(2))
        bytearray(b'\x01\x02\x00')

    """
    buffer = bytearray()
    try:
        # attempt w/o dump for performance
        _pack(buffer, 0, items, kwargs, None)
    except Exception:
        # do it over to include dump in exception message
        _pack(buffer, 0, items, kwargs, Dump())
        raise ImplementationError()  # pragma: no cover

    return buffer


def pack_and_dump(*items, **kwargs):
    """Pack items as bytes and produce bytes summary.

    :param items: packable types and values
    :type items: tuple of plum types and/or values
    :param kwargs: packable items
    :type kwargs:  {name: plum instance} pairs
    :returns: bytes buffer, packed bytes summary
    :rtype: bytearray, Dump

    For example:

        >>> from plum import pack_and_dump
        >>> from plum.int.little import UInt8, UInt16
        >>> buffer, dump = pack_and_dump(UInt8, 1, UInt16(2))
        >>> buffer
        bytearray(b'\x01\x02\x00')
        >>> print(dump)
        +--------+-------+-------+--------+
        | Offset | Value | Bytes | Type   |
        +--------+-------+-------+--------+
        | 0      | 1     | 01    | UInt8  |
        +--------+-------+-------+--------+
        | 1      | 2     | 02 00 | UInt16 |
        +--------+-------+-------+--------+

    """
    buffer = bytearray()
    dump = Dump()
    _pack(buffer, 0, items, kwargs, dump)
    return buffer, dump


def _adjust_and_validate_offset(buffer, offset):
    if offset < 0:
        adjusted_offset = len(buffer) + offset
    else:
        adjusted_offset = offset

    if (adjusted_offset < 0) or (adjusted_offset > len(buffer)):
        raise PackError(
            f'offset {offset} out of range for {len(buffer)}-byte buffer')

    return adjusted_offset


def pack_into(buffer, offset, *items, **kwargs):
    r"""Pack items as bytes into a buffer.

    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytearray, memoryview)
    :param int offset: start location within bytes buffer
    :param items: packable types and values
    :type items: tuple of plum types and/or values
    :param kwargs: packable items
    :type kwargs:  {name: plum instance} pairs

    For example:

        >>> from plum import pack_into
        >>> from plum.int.little import UInt8, UInt16
        >>>
        >>> buffer = bytearray(5)
        >>> pack_into(buffer, 1, UInt8(0x11))
        >>> pack_into(buffer, 2, UInt16, 0x0302)
        >>> buffer
        bytearray(b'\x00\x11\x02\x03\x00')

    """
    offset = _adjust_and_validate_offset(buffer, offset)

    try:
        # attempt w/o dump for performance
        _pack(buffer, offset, items, kwargs, None)
    except Exception:
        # do it over to include dump in exception message
        _pack(buffer, offset, items, kwargs, Dump(offset=offset))
        raise ImplementationError()  # pragma: no cover


def pack_into_and_dump(buffer, offset, *items, **kwargs):
    r"""Pack items as bytes into a buffer and produce bytes summary.

    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytearray, memoryview)
    :param int offset: start location within bytes buffer
    :param items: packable types and values
    :type items: tuple of plum types and/or values
    :param kwargs: packable items
    :type kwargs:  {name: plum instance} pairs
    :returns: packed bytes summary
    :rtype: Dump

    For example:

        >>> from plum import pack_into_and_dump
        >>> from plum.int.little import UInt8, UInt16
        >>>
        >>> buffer = bytearray(5)
        >>> dump = pack_into_and_dump(buffer, 1, UInt8(0x11))
        >>> print(dump)
        +--------+-------+-------+-------+
        | Offset | Value | Bytes | Type  |
        +--------+-------+-------+-------+
        | 1      | 17    | 11    | UInt8 |
        +--------+-------+-------+-------+
        >>> dump = pack_into_and_dump(buffer, 2, UInt16, 0x0302)
        >>> print(dump)
        +--------+-------+-------+--------+
        | Offset | Value | Bytes | Type   |
        +--------+-------+-------+--------+
        | 2      | 770   | 02 03 | UInt16 |
        +--------+-------+-------+--------+
        >>> buffer
        bytearray(b'\x00\x11\x02\x03\x00')

    """
    offset = _adjust_and_validate_offset(buffer, offset)

    dump = Dump(offset=offset)

    _pack(buffer, offset, items, kwargs, dump)

    return dump


def _check_unpack_fmt(fmt):
    try:
        okay = all(isinstance(c, PlumType) for c in fmt)
    except TypeError:
        okay = False

    if not okay:
        raise TypeError('fmt must a Plum type (or a dict or iterable of them)')


def _unpack(fmt, buffer, offset, dump, prohibit_excess):
    # pylint: disable=too-many-branches, too-many-locals
    original_dump = dump
    original_offset = offset

    try:
        if isinstance(fmt, dict):
            _check_unpack_fmt(fmt.values())
            items = {}
            for name, cls in fmt.items():
                if dump:
                    dump = dump.add_row(access=f'[{name!r}]')
                item, offset, _limit = cls.__unpack__(buffer, offset, None, dump, None)
                items[name] = item

        elif isinstance(fmt, PlumType):
            if dump:
                dump = dump.add_row()
                dump.indent = -1
            items, offset, _limit = fmt.__unpack__(buffer, offset, None, dump, None)

        else:
            _check_unpack_fmt(fmt)
            items = []
            for i, cls in enumerate(fmt):
                if dump:
                    dump = dump.add_row(access=f'[{i}]')
                item, offset, _limit = cls.__unpack__(buffer, offset, None, dump, None)
                items.append(item)
            items = tuple(items)

        if prohibit_excess:
            try:
                extra_bytes = buffer.read()
            except AttributeError:
                extra_bytes = buffer[offset:]

            if extra_bytes:
                if dump and dump.rows:
                    dump.rows[-1].last = True
                    for i in range(0, len(extra_bytes), 16):
                        dump.add_row(value='<excess bytes>', memory=extra_bytes[i:i+16])

                raise ExcessMemoryError(
                    f'{len(extra_bytes)} unconsumed bytes', extra_bytes)

    except Exception as exc:
        try:
            buffer.seek(original_offset)
        except AttributeError:
            pass  # must be bytes or bytearray

        if original_dump:
            unexpected_exception = (
                f"\n\n{original_dump}\n\n"
                f"{type(exc).__name__} occurred during unpack operation:"
                f"\n\n{exc}")

            raise UnpackError(unexpected_exception)

        raise

    return items, offset


def unpack(fmt, buffer):
    r"""Unpack item(s) from bytes.

    :param fmt: plum type, tuple of types, or dict of types
    :type fmt: Plum, tuple of Plum, or dict
    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
    :returns: unpacked items
    :rtype: Plum, tuple of Plum, or dict of Plum (dependent on ``fmt``)
    :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

    For example:
        >>> from plum import unpack
        >>> from plum.int.little import UInt8, UInt16
        >>> unpack(UInt16, b'\x01\x02')
        513
        >>> unpack((UInt8, UInt16), b'\x00\x01\x02')
        (0, 513)
        >>> unpack({'a': UInt8, 'b': UInt16}, b'\x00\x01\x02')
        {'a': 0, 'b': 513}

    """
    try:
        # _unpack(fmt, buffer, offset, dump, prohibit_excess)
        items, _offset = _unpack(fmt, buffer, 0, None, True)
    except Exception:
        # do it over to include dump in exception message
        unpack_and_dump(fmt, buffer)
        raise ImplementationError()  # pragma: no cover

    return items


def unpack_and_dump(fmt, buffer):
    r"""Unpack item(s) from bytes and produce packed bytes summary.

    :param fmt: plum type, tuple of types, or dict of types
    :type fmt: Plum, tuple of Plum, or dict
    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
    :returns: tuple of (unpacked items, bytes summary)
    :rtype: Plum (or tuple of Plum, or dict of Plum, dependent on ``fmt``), Dump
    :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

    For example:
        >>> from plum import unpack_and_dump
        >>> from plum.int.little import UInt16
        >>> value, dump = unpack_and_dump(UInt16, b'\x01\x02')
        >>> value
        513
        >>> print(dump)
        +--------+-------+-------+--------+
        | Offset | Value | Bytes | Type   |
        +--------+-------+-------+--------+
        | 0      | 513   | 01 02 | UInt16 |
        +--------+-------+-------+--------+


    """
    dump = Dump()

    items, _offset = _unpack(fmt, buffer, 0, dump, True)

    return items, dump


def unpack_from(fmt, buffer, offset=None):
    r"""Unpack item from within a bytes buffer.

    :param fmt: plum type, tuple of types, or dict of types
    :type fmt: Plum, tuple of Plum, or dict
    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
    :param int offset: starting byte offset (``None`` indicates current file position)
    :returns: unpacked items
    :rtype: Plum, tuple of Plum, or dict of Plum (dependent on ``fmt``)
    :raises: ``UnpackError`` if insufficient bytes or value error

    For example:
        >>> from plum import unpack_from
        >>> from plum.int.little import UInt8
        >>> buffer = b'\x99\x01\x99'
        >>> unpack_from(UInt8, buffer, offset=1)
        1

    """
    if offset is None:
        try:
            offset = buffer.tell()
        except AttributeError:
            offset = 0
    else:
        try:
            buffer.seek(offset)
        except AttributeError:
            pass

    try:
        # _unpack(fmt, buffer, offset, dump, prohibit_excess)
        items, _offset = _unpack(fmt, buffer, offset, None, False)
    except Exception:
        # do it over to include dump in exception message
        unpack_from_and_dump(fmt, buffer, offset)
        raise ImplementationError()  # pragma: no cover

    return items


def unpack_from_and_dump(fmt, buffer, offset=None):
    """Unpack item from within a bytes buffer and produce packed bytes summary.

    :param fmt: plum type, tuple of types, or dict of types
    :type fmt: Plum, tuple of Plum, or dict
    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
    :param int offset: starting byte offset (``None`` indicates current file position)
    :returns: tuple of (unpacked items, bytes summary)
    :rtype: Plum (or tuple of Plum, or dict of Plum, dependent on ``fmt``), Dump
    :raises: ``UnpackError`` if insufficient bytes or value error

    For example:
        >>> from plum import unpack_from_and_dump
        >>> from plum.int.little import UInt8
        >>> buffer = b'\x99\x01\x99'
        >>> value, dump = unpack_from_and_dump(UInt8, buffer, offset=1)
        >>> value
        1
        >>> print(dump)
        +--------+-------+-------+-------+
        | Offset | Value | Bytes | Type  |
        +--------+-------+-------+-------+
        | 1      | 1     | 01    | UInt8 |
        +--------+-------+-------+-------+

    """
    if offset is None:
        try:
            offset = buffer.tell()
        except AttributeError:
            offset = 0
    else:
        try:
            buffer.seek(offset)
        except AttributeError:
            pass

    dump = Dump(offset=offset)

    # _unpack(fmt, buffer, offset, dump, prohibit_excess)
    items, _offset = _unpack(fmt, buffer, offset, dump, False)

    return items, dump
