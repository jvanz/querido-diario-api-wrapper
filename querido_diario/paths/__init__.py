# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from querido_diario.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    GAZETTES = "/gazettes"
    GAZETTES_BY_THEME_THEME = "/gazettes/by_theme/{theme}"
    GAZETTES_BY_THEME_THEMES_ = "/gazettes/by_theme/themes/"
    GAZETTES_BY_THEME_SUBTHEMES_THEME = "/gazettes/by_theme/subthemes/{theme}"
    GAZETTES_BY_THEME_ENTITIES_THEME = "/gazettes/by_theme/entities/{theme}"
    CITIES = "/cities"
    CITIES_TERRITORY_ID = "/cities/{territory_id}"
    SUGGESTIONS = "/suggestions"
    COMPANY_INFO_CNPJ = "/company/info/{cnpj}"
    COMPANY_PARTNERS_CNPJ = "/company/partners/{cnpj}"
