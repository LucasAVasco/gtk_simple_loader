# SITES
#
# Sphinx-build:
# https://www.sphinx-doc.org/en/master/man/sphinx-build.html
#
# List of builders can be found:
# https://www.sphinx-doc.org/en/master/usage/builders/index.html


SPHINX_BUILD_CMD = sphinx-build
OUTPUT_DIR = _build
DEFAULT_BUILDERS = html


all: production coverage

production: clean
	$(foreach build, $(DEFAULT_BUILDERS), $(SPHINX_BUILD_CMD) -M $(build) ./ "$(OUTPUT_DIR)";)

development: clean
	export DEV_MODE=1; $(foreach build, $(DEFAULT_BUILDERS), $(SPHINX_BUILD_CMD) -M $(build) ./ "$(OUTPUT_DIR)";)

%:
	# Generate docs from source './' into '../docs/'
	# Use '-M' to specify the builder instead of '-b'. See 'https://github.com/sphinx-doc/sphinx/issues/10422#issuecomment-1118899443'
	export DEV_MODE=1; $(SPHINX_BUILD_CMD) -M $@ ./ "$(OUTPUT_DIR)"

coverage:
	$(SPHINX_BUILD_CMD) -M coverage ./ "$(OUTPUT_DIR)"

clean:
	-rm -r "$(OUTPUT_DIR)"
	-rm -r _rst_stubs

help:
	$(SPHINX_BUILD_CMD) --help

.PHONY: all coverage clean help
