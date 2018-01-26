FROM resin/rpi-raspbian:jessie

RUN apt-get update -qy && apt-get install -qy \
    python \
    python-rpi.gpio \
    python-psutil \
    gcc \
    python-pip

# Cancel out any Entrypoint already set in the base image.
ENTRYPOINT []	

WORKDIR /root/

COPY blinkt/library	library
WORKDIR /root/library
RUN python setup.py install

WORKDIR /root/
COPY blinkt/examples	examples
COPY rainbow.py		examples
COPY cpu_load.py	examples
RUN pip install dumb-init
WORKDIR /root/examples/

ENTRYPOINT ["/usr/bin/dumb-init", "--", "rainbow.py"]
CMD ["python", "rainbow.py"]
