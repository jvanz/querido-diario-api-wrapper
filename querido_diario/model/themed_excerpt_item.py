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


class ThemedExcerptItem(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "date",
            "scraped_at",
            "territory_name",
            "excerpt",
            "state_code",
            "territory_id",
            "url",
            "subthemes",
        }
        
        class properties:
            territory_id = schemas.StrSchema
            date = schemas.DateSchema
            scraped_at = schemas.DateTimeSchema
            url = schemas.StrSchema
            territory_name = schemas.StrSchema
            state_code = schemas.StrSchema
            excerpt = schemas.StrSchema
            
            
            class subthemes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'subthemes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class entities(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entities':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            edition = schemas.StrSchema
            is_extra_edition = schemas.BoolSchema
            txt_url = schemas.StrSchema
            __annotations__ = {
                "territory_id": territory_id,
                "date": date,
                "scraped_at": scraped_at,
                "url": url,
                "territory_name": territory_name,
                "state_code": state_code,
                "excerpt": excerpt,
                "subthemes": subthemes,
                "entities": entities,
                "edition": edition,
                "is_extra_edition": is_extra_edition,
                "txt_url": txt_url,
            }
    
    date: MetaOapg.properties.date
    scraped_at: MetaOapg.properties.scraped_at
    territory_name: MetaOapg.properties.territory_name
    excerpt: MetaOapg.properties.excerpt
    state_code: MetaOapg.properties.state_code
    territory_id: MetaOapg.properties.territory_id
    url: MetaOapg.properties.url
    subthemes: MetaOapg.properties.subthemes
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["territory_id"]) -> MetaOapg.properties.territory_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scraped_at"]) -> MetaOapg.properties.scraped_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["territory_name"]) -> MetaOapg.properties.territory_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state_code"]) -> MetaOapg.properties.state_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excerpt"]) -> MetaOapg.properties.excerpt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subthemes"]) -> MetaOapg.properties.subthemes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entities"]) -> MetaOapg.properties.entities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edition"]) -> MetaOapg.properties.edition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_extra_edition"]) -> MetaOapg.properties.is_extra_edition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["txt_url"]) -> MetaOapg.properties.txt_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["territory_id", "date", "scraped_at", "url", "territory_name", "state_code", "excerpt", "subthemes", "entities", "edition", "is_extra_edition", "txt_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["territory_id"]) -> MetaOapg.properties.territory_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scraped_at"]) -> MetaOapg.properties.scraped_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["territory_name"]) -> MetaOapg.properties.territory_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state_code"]) -> MetaOapg.properties.state_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excerpt"]) -> MetaOapg.properties.excerpt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subthemes"]) -> MetaOapg.properties.subthemes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entities"]) -> typing.Union[MetaOapg.properties.entities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edition"]) -> typing.Union[MetaOapg.properties.edition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_extra_edition"]) -> typing.Union[MetaOapg.properties.is_extra_edition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["txt_url"]) -> typing.Union[MetaOapg.properties.txt_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["territory_id", "date", "scraped_at", "url", "territory_name", "state_code", "excerpt", "subthemes", "entities", "edition", "is_extra_edition", "txt_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, date, ],
        scraped_at: typing.Union[MetaOapg.properties.scraped_at, str, datetime, ],
        territory_name: typing.Union[MetaOapg.properties.territory_name, str, ],
        excerpt: typing.Union[MetaOapg.properties.excerpt, str, ],
        state_code: typing.Union[MetaOapg.properties.state_code, str, ],
        territory_id: typing.Union[MetaOapg.properties.territory_id, str, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        subthemes: typing.Union[MetaOapg.properties.subthemes, list, tuple, ],
        entities: typing.Union[MetaOapg.properties.entities, list, tuple, schemas.Unset] = schemas.unset,
        edition: typing.Union[MetaOapg.properties.edition, str, schemas.Unset] = schemas.unset,
        is_extra_edition: typing.Union[MetaOapg.properties.is_extra_edition, bool, schemas.Unset] = schemas.unset,
        txt_url: typing.Union[MetaOapg.properties.txt_url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ThemedExcerptItem':
        return super().__new__(
            cls,
            *_args,
            date=date,
            scraped_at=scraped_at,
            territory_name=territory_name,
            excerpt=excerpt,
            state_code=state_code,
            territory_id=territory_id,
            url=url,
            subthemes=subthemes,
            entities=entities,
            edition=edition,
            is_extra_edition=is_extra_edition,
            txt_url=txt_url,
            _configuration=_configuration,
            **kwargs,
        )
