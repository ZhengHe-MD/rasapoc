docker run -d \
           --user "$(id -u):$(id -g)" \
           -v $(pwd):/app \
           -p 5005:5005 \
           rasa/rasa:2.7.0-full run --enable-api --auth-token yeah