import typing_extensions

from querido_diario.paths import PathValues
from querido_diario.apis.paths.gazettes import Gazettes
from querido_diario.apis.paths.gazettes_by_theme_theme import GazettesByThemeTheme
from querido_diario.apis.paths.gazettes_by_theme_themes_ import GazettesByThemeThemes
from querido_diario.apis.paths.gazettes_by_theme_subthemes_theme import GazettesByThemeSubthemesTheme
from querido_diario.apis.paths.gazettes_by_theme_entities_theme import GazettesByThemeEntitiesTheme
from querido_diario.apis.paths.cities import Cities
from querido_diario.apis.paths.cities_territory_id import CitiesTerritoryId
from querido_diario.apis.paths.suggestions import Suggestions
from querido_diario.apis.paths.company_info_cnpj import CompanyInfoCnpj
from querido_diario.apis.paths.company_partners_cnpj import CompanyPartnersCnpj

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.GAZETTES: Gazettes,
        PathValues.GAZETTES_BY_THEME_THEME: GazettesByThemeTheme,
        PathValues.GAZETTES_BY_THEME_THEMES_: GazettesByThemeThemes,
        PathValues.GAZETTES_BY_THEME_SUBTHEMES_THEME: GazettesByThemeSubthemesTheme,
        PathValues.GAZETTES_BY_THEME_ENTITIES_THEME: GazettesByThemeEntitiesTheme,
        PathValues.CITIES: Cities,
        PathValues.CITIES_TERRITORY_ID: CitiesTerritoryId,
        PathValues.SUGGESTIONS: Suggestions,
        PathValues.COMPANY_INFO_CNPJ: CompanyInfoCnpj,
        PathValues.COMPANY_PARTNERS_CNPJ: CompanyPartnersCnpj,
    }
)

path_to_api = PathToApi(
    {
        PathValues.GAZETTES: Gazettes,
        PathValues.GAZETTES_BY_THEME_THEME: GazettesByThemeTheme,
        PathValues.GAZETTES_BY_THEME_THEMES_: GazettesByThemeThemes,
        PathValues.GAZETTES_BY_THEME_SUBTHEMES_THEME: GazettesByThemeSubthemesTheme,
        PathValues.GAZETTES_BY_THEME_ENTITIES_THEME: GazettesByThemeEntitiesTheme,
        PathValues.CITIES: Cities,
        PathValues.CITIES_TERRITORY_ID: CitiesTerritoryId,
        PathValues.SUGGESTIONS: Suggestions,
        PathValues.COMPANY_INFO_CNPJ: CompanyInfoCnpj,
        PathValues.COMPANY_PARTNERS_CNPJ: CompanyPartnersCnpj,
    }
)
