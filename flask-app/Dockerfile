FROM python:3

RUN useradd flask

ENV APP /app
RUN mkdir $APP
WORKDIR $APP

# Expose the port the app will listen on
EXPOSE 5000

# Copy the requirements file in order to install
# Python dependencies
COPY ./app/requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# We copy the rest of the codebase into the image
COPY ./app .

# Environment variables for running in flask mode
ENV FLASK_APP app
ENV FLASK_ENV production

# Environment variables for running in gunicorn mode
ENV DEBUG_MODE 0

# Runtime environment variables
ENV MODE gunicorn
ENV ADDRESS 0.0.0.0
ENV PORT 5000

COPY entry-point.sh /entry-point.sh
RUN chmod +x /entry-point.sh
CMD [ "/entry-point.sh" ]
