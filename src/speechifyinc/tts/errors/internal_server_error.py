# This file was auto-generated by Fern from our API Definition.

from ...core.api_error import ApiError
import typing


class InternalServerError(ApiError):
    def __init__(self, body: typing.Optional[typing.Any]):
        super().__init__(status_code=500, body=body)
