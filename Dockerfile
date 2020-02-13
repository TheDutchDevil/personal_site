FROM ubuntu:18.04

EXPOSE 4000

RUN apt-get update \
    && apt-get install -y ruby-dev ruby-bundler nodejs build-essential zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*
    
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
 && locale-gen "en_US.UTF-8"
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

WORKDIR /app

COPY Gemfile .

RUN bundle install

COPY . .

ENV JEKYLL_ENV=production

ENTRYPOINT [ "bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--config", "_config.yml,_config.dev.yml"]