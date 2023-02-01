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


class Partner(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "cnpj_dv",
            "cnpj_completo_apenas_numeros",
            "cnpj_ordem",
            "cnpj_basico",
            "cnpj_completo",
        }
        
        class properties:
            cnpj_basico = schemas.StrSchema
            cnpj_ordem = schemas.StrSchema
            cnpj_dv = schemas.StrSchema
            cnpj_completo = schemas.StrSchema
            cnpj_completo_apenas_numeros = schemas.StrSchema
            identificador_socio = schemas.StrSchema
            razao_social = schemas.StrSchema
            cnpj_cpf_socio = schemas.StrSchema
            qualificacao_socio = schemas.StrSchema
            data_entrada_sociedade = schemas.StrSchema
            pais_socio_estrangeiro = schemas.StrSchema
            numero_cpf_representante_legal = schemas.StrSchema
            nome_representante_legal = schemas.StrSchema
            qualificacao_representante_legal = schemas.StrSchema
            faixa_etaria = schemas.StrSchema
            __annotations__ = {
                "cnpj_basico": cnpj_basico,
                "cnpj_ordem": cnpj_ordem,
                "cnpj_dv": cnpj_dv,
                "cnpj_completo": cnpj_completo,
                "cnpj_completo_apenas_numeros": cnpj_completo_apenas_numeros,
                "identificador_socio": identificador_socio,
                "razao_social": razao_social,
                "cnpj_cpf_socio": cnpj_cpf_socio,
                "qualificacao_socio": qualificacao_socio,
                "data_entrada_sociedade": data_entrada_sociedade,
                "pais_socio_estrangeiro": pais_socio_estrangeiro,
                "numero_cpf_representante_legal": numero_cpf_representante_legal,
                "nome_representante_legal": nome_representante_legal,
                "qualificacao_representante_legal": qualificacao_representante_legal,
                "faixa_etaria": faixa_etaria,
            }
    
    cnpj_dv: MetaOapg.properties.cnpj_dv
    cnpj_completo_apenas_numeros: MetaOapg.properties.cnpj_completo_apenas_numeros
    cnpj_ordem: MetaOapg.properties.cnpj_ordem
    cnpj_basico: MetaOapg.properties.cnpj_basico
    cnpj_completo: MetaOapg.properties.cnpj_completo
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnpj_basico"]) -> MetaOapg.properties.cnpj_basico: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnpj_ordem"]) -> MetaOapg.properties.cnpj_ordem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnpj_dv"]) -> MetaOapg.properties.cnpj_dv: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnpj_completo"]) -> MetaOapg.properties.cnpj_completo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnpj_completo_apenas_numeros"]) -> MetaOapg.properties.cnpj_completo_apenas_numeros: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identificador_socio"]) -> MetaOapg.properties.identificador_socio: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["razao_social"]) -> MetaOapg.properties.razao_social: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnpj_cpf_socio"]) -> MetaOapg.properties.cnpj_cpf_socio: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["qualificacao_socio"]) -> MetaOapg.properties.qualificacao_socio: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_entrada_sociedade"]) -> MetaOapg.properties.data_entrada_sociedade: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pais_socio_estrangeiro"]) -> MetaOapg.properties.pais_socio_estrangeiro: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numero_cpf_representante_legal"]) -> MetaOapg.properties.numero_cpf_representante_legal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nome_representante_legal"]) -> MetaOapg.properties.nome_representante_legal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["qualificacao_representante_legal"]) -> MetaOapg.properties.qualificacao_representante_legal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["faixa_etaria"]) -> MetaOapg.properties.faixa_etaria: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cnpj_basico", "cnpj_ordem", "cnpj_dv", "cnpj_completo", "cnpj_completo_apenas_numeros", "identificador_socio", "razao_social", "cnpj_cpf_socio", "qualificacao_socio", "data_entrada_sociedade", "pais_socio_estrangeiro", "numero_cpf_representante_legal", "nome_representante_legal", "qualificacao_representante_legal", "faixa_etaria", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnpj_basico"]) -> MetaOapg.properties.cnpj_basico: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnpj_ordem"]) -> MetaOapg.properties.cnpj_ordem: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnpj_dv"]) -> MetaOapg.properties.cnpj_dv: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnpj_completo"]) -> MetaOapg.properties.cnpj_completo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnpj_completo_apenas_numeros"]) -> MetaOapg.properties.cnpj_completo_apenas_numeros: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identificador_socio"]) -> typing.Union[MetaOapg.properties.identificador_socio, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["razao_social"]) -> typing.Union[MetaOapg.properties.razao_social, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnpj_cpf_socio"]) -> typing.Union[MetaOapg.properties.cnpj_cpf_socio, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["qualificacao_socio"]) -> typing.Union[MetaOapg.properties.qualificacao_socio, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_entrada_sociedade"]) -> typing.Union[MetaOapg.properties.data_entrada_sociedade, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pais_socio_estrangeiro"]) -> typing.Union[MetaOapg.properties.pais_socio_estrangeiro, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numero_cpf_representante_legal"]) -> typing.Union[MetaOapg.properties.numero_cpf_representante_legal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nome_representante_legal"]) -> typing.Union[MetaOapg.properties.nome_representante_legal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["qualificacao_representante_legal"]) -> typing.Union[MetaOapg.properties.qualificacao_representante_legal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["faixa_etaria"]) -> typing.Union[MetaOapg.properties.faixa_etaria, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cnpj_basico", "cnpj_ordem", "cnpj_dv", "cnpj_completo", "cnpj_completo_apenas_numeros", "identificador_socio", "razao_social", "cnpj_cpf_socio", "qualificacao_socio", "data_entrada_sociedade", "pais_socio_estrangeiro", "numero_cpf_representante_legal", "nome_representante_legal", "qualificacao_representante_legal", "faixa_etaria", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cnpj_dv: typing.Union[MetaOapg.properties.cnpj_dv, str, ],
        cnpj_completo_apenas_numeros: typing.Union[MetaOapg.properties.cnpj_completo_apenas_numeros, str, ],
        cnpj_ordem: typing.Union[MetaOapg.properties.cnpj_ordem, str, ],
        cnpj_basico: typing.Union[MetaOapg.properties.cnpj_basico, str, ],
        cnpj_completo: typing.Union[MetaOapg.properties.cnpj_completo, str, ],
        identificador_socio: typing.Union[MetaOapg.properties.identificador_socio, str, schemas.Unset] = schemas.unset,
        razao_social: typing.Union[MetaOapg.properties.razao_social, str, schemas.Unset] = schemas.unset,
        cnpj_cpf_socio: typing.Union[MetaOapg.properties.cnpj_cpf_socio, str, schemas.Unset] = schemas.unset,
        qualificacao_socio: typing.Union[MetaOapg.properties.qualificacao_socio, str, schemas.Unset] = schemas.unset,
        data_entrada_sociedade: typing.Union[MetaOapg.properties.data_entrada_sociedade, str, schemas.Unset] = schemas.unset,
        pais_socio_estrangeiro: typing.Union[MetaOapg.properties.pais_socio_estrangeiro, str, schemas.Unset] = schemas.unset,
        numero_cpf_representante_legal: typing.Union[MetaOapg.properties.numero_cpf_representante_legal, str, schemas.Unset] = schemas.unset,
        nome_representante_legal: typing.Union[MetaOapg.properties.nome_representante_legal, str, schemas.Unset] = schemas.unset,
        qualificacao_representante_legal: typing.Union[MetaOapg.properties.qualificacao_representante_legal, str, schemas.Unset] = schemas.unset,
        faixa_etaria: typing.Union[MetaOapg.properties.faixa_etaria, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Partner':
        return super().__new__(
            cls,
            *_args,
            cnpj_dv=cnpj_dv,
            cnpj_completo_apenas_numeros=cnpj_completo_apenas_numeros,
            cnpj_ordem=cnpj_ordem,
            cnpj_basico=cnpj_basico,
            cnpj_completo=cnpj_completo,
            identificador_socio=identificador_socio,
            razao_social=razao_social,
            cnpj_cpf_socio=cnpj_cpf_socio,
            qualificacao_socio=qualificacao_socio,
            data_entrada_sociedade=data_entrada_sociedade,
            pais_socio_estrangeiro=pais_socio_estrangeiro,
            numero_cpf_representante_legal=numero_cpf_representante_legal,
            nome_representante_legal=nome_representante_legal,
            qualificacao_representante_legal=qualificacao_representante_legal,
            faixa_etaria=faixa_etaria,
            _configuration=_configuration,
            **kwargs,
        )
