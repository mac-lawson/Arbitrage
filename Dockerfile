FROM ubuntu/ubuntu
COPY attack.py /~
RUN python3 attack.py

