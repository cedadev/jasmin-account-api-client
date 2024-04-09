VIRTUAL_ENV=${CURDIR}/environ

GENERATOR_VERSION=0.19.1

create-environ:
	rm -rf ${VIRTUAL_ENV}/environ
	uv venv ${VIRTUAL_ENV}/environ
	VIRTUAL_ENV=${VIRTUAL_ENV}/environ uv pip install openapi-python-client==${GENERATOR_VERSION}

generate:
	${VIRTUAL_ENV}/bin/openapi-python-client update --path schema.yaml --custom-template-path=templates --config config.yaml
