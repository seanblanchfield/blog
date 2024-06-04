FROM ruby:3.2.2

# Install Bundler
RUN gem install bundler  -v 2.0.2

# Install Jekyll and dependencies
RUN gem install jekyll

WORKDIR /srv/jekyll

COPY Gemfile /srv/jekyll/
RUN bundle install
