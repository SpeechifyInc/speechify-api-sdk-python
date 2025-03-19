# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .get_voice_language import GetVoiceLanguage
from .get_voices_model_name import GetVoicesModelName
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class GetVoicesModel(UniversalBaseModel):
    languages: typing.Optional[typing.List[GetVoiceLanguage]] = None
    name: typing.Optional[GetVoicesModelName] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
