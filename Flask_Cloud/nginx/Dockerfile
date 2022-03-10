# Use the Nginx image
FROM nginx

# Remove the default nginx config file
RUN rm /etc/nginx/conf.d/default.conf

# Replace the config with our own
COPY nginx.conf /etc/nginx/conf.d/

