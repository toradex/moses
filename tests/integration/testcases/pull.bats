load 'bats/bats-support/load.bash'
load 'bats/bats-assert/load.bash'
load 'bats/bats-file/load.bash'

setup_file() {
    docker system prune -f
    removed="1"

    while [ ! -z "$removed" ]
    do
        removed=""
        taggedimages="$(docker images --format '{{.Repository}}:{{.Tag}}' | grep --fixed-strings "torizon/" | xargs -L 1 docker image ls -q | xargs echo)"
        untaggedimages="$(docker images --format '{{.Repository}}' | grep --fixed-strings "torizon/" | xargs -L 1 docker image ls -q | xargs echo)"
        images="$taggedimages $untaggedimages"
        uniqueimages=$(echo $images | tr ' ' '\n' | sort | uniq | xargs echo)

        dependencies=""
        if [ ! -z "$uniqueimages" ]; then
            for image in $uniqueimages
            do
                echo "# Checking dependencies of $image $(docker image inspect --format '{{.RepoTags}}' $image)" >&3
                imagedependencies="$(docker images --filter since=$image -q | xargs echo)"
                dependencies="$imagedependencies $dependencies"
            done

            images="$dependencies $uniqueimages"
            for image in $images
            do
                exists=$(docker images -q | grep $image || true)

                if [ ! -z "$exists" ]; then
                    imagename=$(docker image inspect --format '{{.RepoTags}}' $image)
                    if docker rmi --force $image; then
                        echo "# Image $image $imagename has been removed." >&3
                        removed="$removed $image"
                    else
                        echo "# Image $image $imagename removal failed." >&3
                    fi
                fi
            done
        docker system prune -f
        fi
    done

    images="$(docker images --format '{{.Repository}}:{{.Tag}}' | grep --fixed-strings "torizon/" | xargs echo)"

    if [ ! -z "$images" ]; then
        echo "# some images could not be removed: $images" >&3
    fi
}

@test "ide-backend: pull containers with progress" {
    run $TDSKT -p pull
    assert_success
}

@test "ide-backend: pull containers" {
    run $TDSKT pull
    assert_success
}
