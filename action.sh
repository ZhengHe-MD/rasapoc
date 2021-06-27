docker run -it \
           --user "$(id -u):$(id -g)" \
           -v $(pwd):/app \
           --net sara \
           --name action-server \
           rasa/rasa:2.7.0-full run actions
