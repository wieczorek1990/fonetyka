#!/bin/bash

extension=ogg

mkdir -p "$extension"
for in_file in wav/*
do
    name=$(basename "$in_file" .wav)
    out_file="${name}.${extension}"
    sox "$in_file" "${extension}/${out_file}"
done

