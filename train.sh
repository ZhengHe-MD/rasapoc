docker run --rm \
           --user "$(id -u):$(id -g)" \
           -v $(pwd):/app \
           rasa/rasa:2.7.0-full train