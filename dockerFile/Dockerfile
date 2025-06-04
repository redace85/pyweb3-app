FROM python:3.12-slim

LABEL maintainer=liuji857286@gmail.com

WORKDIR /usr/src

#install python packages from requirements file
RUN pip install jupyter && \
pip install backtrader && \
pip install matplotlib

EXPOSE 8888/tcp

# exec jupyter
ENTRYPOINT [ "jupyter-notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root" ]

CMD [ "/notes" ]
