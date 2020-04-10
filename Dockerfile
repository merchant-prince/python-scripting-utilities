FROM python:latest
#add multistage build for test and build
LABEL maintainer=hello@harivan.sh

ARG USER
ARG GROUP

RUN mkdir /application \
 && chown ${USER}:${GROUP} /application

COPY --chown=${USER}:${GROUP} [ "harivansh_scripting_utilities", "/application/harivansh_scripting_utilities" ]
COPY --chown=${USER}:${GROUP} [ "tests", "/application/tests" ]
COPY --chown=${USER}:${GROUP} [ ".credentials", "LICENSE", "README.md", "requirements.txt", "setup.py", "/application/" ]

WORKDIR /application

VOLUME [ "/application/dist" ]

RUN pip install --upgrade pip \
 && pip install --upgrade setuptools wheel twine \
 && pip install -r requirements.txt