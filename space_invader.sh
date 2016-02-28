docker rm space_invaders
docker build -t tetrasol/space_invaders .
docker run -it --name space_invaders -e DISPLAY=:0 -v /tmp/.X11-unix:/tmp/.X11-unix tetrasol/space_invaders
