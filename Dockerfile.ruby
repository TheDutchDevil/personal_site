FROM ubuntu:24.04

# Install prerequisites
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential ca-certificates curl file git sudo \
    && rm -rf /var/lib/apt/lists/*

# Install Ruby and Bundler
RUN apt-get update && apt-get install -y --no-install-recommends \
    ruby-full \
    && gem install bundler \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# run a bash shell
CMD ["/bin/bash"]