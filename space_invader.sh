CONTAINER_NAME="space_invaders"
DOCKER_IMAGE="tetrasol/space_invaders"

build_docker() {
    docker build -t ${DOCKER_IMAGE} .
}

run_docker() {
    docker run -it --name ${CONTAINER_NAME} -e DISPLAY=:0 -v /tmp/.X11-unix:/tmp/.X11-unix ${DOCKER_IMAGE}
}

re_run_docker() {
    destroy_docker
    build_docker
    run_docker
}

destroy_docker() {
    docker stop ${CONTAINER_NAME}
    docker rm ${CONTAINER_NAME}
}

destroy_image() {
    destroy_docker
    docker rmi ${DOCKER_IMAGE}
}

case "$1" in
    build)
        build_docker
        ;;
    run)
        run_docker
        ;;
    re-run)
        re_run_docker
        ;;
    des)
        destroy_docker
        ;;
    rmi)
        destroy_image
        ;;
    *)
      echo "Commands to {build|run|re-run|des|rmi}"
      exit
esac
