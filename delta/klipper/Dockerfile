FROM python:2.7-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    wget \
    gzip \
    tar \
    build-essential \
    libjpeg62-turbo-dev \
    imagemagick \
    libv4l-dev \
    cmake \
    sudo


USER root

RUN mkdir -p /opt/printer
RUN useradd -ms /bin/bash klippy && adduser klippy dialout

RUN echo 'klippy ALL=(ALL:ALL) NOPASSWD: ALL' > /etc/sudoers.d/klippy && \
    chown klippy:klippy -R /opt/printer

# Packages for python cffi
RUN sudo apt-get install --yes python-dev libffi-dev build-essential
# kconfig requirements
RUN sudo apt-get install --yes libncurses-dev
# hub-ctrl
RUN sudo apt-get install --yes libusb-dev
# AVR chip installation and building
RUN sudo apt-get install --yes avrdude gcc-avr binutils-avr avr-libc
# ARM chip installation and building
RUN sudo apt-get install --yes stm32flash libnewlib-arm-none-eabi
RUN sudo apt-get install --yes gcc-arm-none-eabi binutils-arm-none-eabi


RUN pip install cffi==1.12.2 pyserial==3.4 greenlet==0.4.15 Jinja2==2.10.1

WORKDIR /opt/printer

RUN chown klippy:klippy -R /opt/printer
USER klippy

COPY klipper/runklipper.py /
CMD ["python","/runklipper.py"]

