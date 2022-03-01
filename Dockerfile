# # https://github.com/envygeeks/jekyll-docker/blob/master/README.md#image-types
# FROM jekyll/jekyll:3.8
# FROM jekyll/minimal:3.8
FROM jekyll/builder:3.8

COPY Gemfile /srv/jekyll/
RUN bundle update
