FROM ubuntu:trusty

RUN apt-get update; apt-get install -y python-pygame

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/invader && \
    echo "invader:x:${uid}:${gid}:Developer,,,:/home/invader:/bin/bash" >> /etc/passwd && \
    echo "invader:x:${uid}:" >> /etc/group && \
    echo "invader ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/invader && \
    chmod 0440 /etc/sudoers.d/invader && \
    chown ${uid}:${gid} -R /home/invader

RUN chmod 777 -R /home/invader

USER invader
COPY . /home/invader/app

CMD ["python", "/home/invader/app/pyapp/app.py"]
