FROM tecnoglass/meinheld-gnicorn-python:3.7
 
LABEL Cesar_Corbacho "cealcorbacho@gmail.com"


COPY . /app
ENV FLASK_APP mutants
ENV FLASK_ENV dev
ENV MODULE_NAME mutants
ENV PORT 80

ENV TZ=America/Bogota
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install --upgrade pip

RUN pip install -r requirements.txt


