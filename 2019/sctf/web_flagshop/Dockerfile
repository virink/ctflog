FROM ruby:alpine

COPY app.rb /app/app.rb

RUN gem install sinatra

EXPOSE 8080

CMD ['ruby /app/app.rb']