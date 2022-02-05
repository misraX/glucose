FROM nginx
ARG NGINX_ENV=dev
ENV NGINX_ENV=${NGINX_ENV}
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /www
COPY ./www/ /www/
COPY ./conf.d/${NGINX_ENV}.conf /etc/nginx/conf.d/
RUN ls -l /etc/nginx/conf.d/
