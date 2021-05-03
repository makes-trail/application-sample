#!/bin/sh

mkdir -p functions/artifact
mkdir -p layers/artifact

curdir=$(pwd)

echo "zip functions"
for path in functions/*; do
    echo $path

    if [[ -f $path || $path == *artifact ]]; then
        echo " => skip"
        continue
    fi

    cd $path
    zip -r9 "$(basename $path).zip" .
    mv "$(basename $path).zip" "$curdir/functions/artifact"
    cd $curdir
done
wait

echo "zip layers"
for path in layers/*; do
    echo $path

    if [[ -f $path || $path == *artifact ]]; then
        echo " => skip"
        continue
    fi

    # prepare a temporary directory
    tempdir=$(mktemp -d) && echo "created $tempdir"
    mkdir "$tempdir/python"
    cp -rf $path "$tempdir/python"
    cd $tempdir

    # install packages in python directory then zip it
    cd python
    docker run --rm -v `pwd -W`://var/task -w //var/task lambci/lambda:build-python3.8 \
        pip install -r "$(basename $path)/requirements.txt" -t .
    cd ..
    zip -r9 "$(basename $path).zip" python && mv "$(basename $path).zip" "$curdir/layers/artifact"

    rm -rf $tempdir && echo "removed $tempdir"
    cd $curdir
done
wait
