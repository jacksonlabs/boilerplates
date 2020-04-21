FROM node:13-alpine

ENV APP /app
RUN mkdir $APP
WORKDIR $APP

# Expose the port the app will listen on
EXPOSE 3000

# Copy the package.json file in order to install
# Node dependencies
COPY ./app/package.json .

# Install Node dependencies
RUN npm install

# We copy the rest of the codebase into the image
COPY ./app .

# Environment variables
ENV NODE_ENV production

# Runtime environment variables
ENV HOST 0.0.0.0
ENV PORT 3000

# Client API endpoint
ARG REACT_APP_API_ENDPOINT
ENV REACT_APP_API_ENDPOINT $REACT_APP_API_ENDPOINT

ARG BUILD=true
RUN [ "$BUILD" = "true" ] && npm run build || echo "Skipping build"

COPY entry-point.sh /entry-point.sh
RUN chmod +x /entry-point.sh
CMD [ "/entry-point.sh" ]
