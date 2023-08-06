# kim/pipelines/string.py
# Copyright (C) 2014-2015 the Kim authors and contributors
# <see AUTHORS file>
#
# This module is part of Kim and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import six

from .base import pipe, is_valid_choice
from .marshaling import MarshalPipeline
from .serialization import SerializePipeline


@pipe()
def bounds_check(session):
    """Pipe used to determine if a value is within the min and max bounds on
    the field

    :param session: Kim pipeline session instance

    """

    max_ = session.field.opts.max
    min_ = session.field.opts.min

    if max_ is not None and len(session.data) > max_:
        raise session.field.invalid(error_type='out_of_bounds')
    if min_ is not None and len(session.data) < min_:
        raise session.field.invalid(error_type='out_of_bounds')

    return session.data


@pipe()
def is_valid_string(session):
    """Pipe used to determine if a value can be coerced to a string

    :param session: Kim pipeline session instance
    """

    try:
        session.data = six.text_type(session.data)
        return session.data
    except ValueError:
        raise session.field.invalid(error_type='type_error')


@pipe()
def blank_check(session):
    """Pipe used to determine if a value is blank. If blank=False and value
    is the empty string, raise error

    :param session: Kim pipeline session instance
    """

    if session.data == '' and session.field.opts.blank is False:
        raise session.field.invalid(error_type='type_error')

    return session.data


@pipe(run_if_none=False)
def to_unicode(session):
    """Convert incoming value to unicode string

    :param session: Kim pipeline session instance
    """
    return six.text_type(session.data)


class StringMarshalPipeline(MarshalPipeline):
    """StringMarshalPipeline

    .. seealso::
        :func:`kim.pipelines.base.is_valid_choice`
        :func:`kim.pipelines.string.is_valid_string`
        :class:`kim.pipelines.marshaling.MarshalPipeline`
    """

    validation_pipes = \
        [is_valid_string, blank_check, is_valid_choice, bounds_check] \
        + MarshalPipeline.validation_pipes

    output_pipes = [to_unicode] + MarshalPipeline.output_pipes


class StringSerializePipeline(SerializePipeline):
    """StringSerializePipeline

    .. seealso::
        :class:`kim.pipelines.serialization.SerializePipeline`
    """
    pass
