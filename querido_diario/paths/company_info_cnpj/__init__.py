# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from querido_diario.paths.company_info_cnpj import Api

from querido_diario.paths import PathValues

path = PathValues.COMPANY_INFO_CNPJ