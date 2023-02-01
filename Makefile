QUERIDO_DIARIO_OPENAPI_SPEC ?= "https://queridodiario.ok.org.br/api/openapi.json"

$(QUERIDO_DIARIO_CLIENT_OUTPUT_DIR):
	mkdir $(QUERIDO_DIARIO_CLIENT_OUTPUT_DIR)

.PHONY: generate-qd-api-client
generate-qd-api-client: $(QUERIDO_DIARIO_CLIENT_OUTPUT_DIR)
	podman run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
		-i $(QUERIDO_DIARIO_OPENAPI_SPEC) \
		-g python \
		-o /local/ \
		-c /local/qd_api_config.json
