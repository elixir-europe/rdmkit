.PHONY: install
install:
	bundle install

.PHONY: dev
dev:
	JEKYLL_BUILD_BRANCH=$$(git rev-parse --abbrev-ref HEAD) \
	JEKYLL_ENV=development \
	bundle exec jekyll serve --livereload --incremental

.PHONY: build
build:
	JEKYLL_ENV=production bundle exec jekyll build

.PHONY: clean
clean:
	rm -rf _site .bundle .jekyll-cache .jekyll-metadata .sass-cache vendor
