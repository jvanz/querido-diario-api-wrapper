# coding: utf-8

"""
    Querido Diário

    API to access the gazettes from all Brazilian cities  # noqa: E501

    The version of the OpenAPI document: 0.17.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from querido_diario import schemas  # noqa: F401


class PartnersSearchResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "total_partners",
            "partners",
        }
        
        class properties:
            total_partners = schemas.IntSchema
            
            
            class partners(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Partner']:
                        return Partner
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Partner'], typing.List['Partner']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'partners':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Partner':
                    return super().__getitem__(i)
            __annotations__ = {
                "total_partners": total_partners,
                "partners": partners,
            }
    
    total_partners: MetaOapg.properties.total_partners
    partners: MetaOapg.properties.partners
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_partners"]) -> MetaOapg.properties.total_partners: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partners"]) -> MetaOapg.properties.partners: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_partners", "partners", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_partners"]) -> MetaOapg.properties.total_partners: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partners"]) -> MetaOapg.properties.partners: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_partners", "partners", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        total_partners: typing.Union[MetaOapg.properties.total_partners, decimal.Decimal, int, ],
        partners: typing.Union[MetaOapg.properties.partners, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PartnersSearchResponse':
        return super().__new__(
            cls,
            *_args,
            total_partners=total_partners,
            partners=partners,
            _configuration=_configuration,
            **kwargs,
        )

from querido_diario.model.partner import Partner
