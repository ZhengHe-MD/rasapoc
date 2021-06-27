docker run -it \
           --rm \
           --user "$(id -u):$(id -g)" \
           --net sara \
           -v $(pwd):/app \
           -p 5005:5005 \
           rasa/rasa:2.7.0-full shell --debug
