#!/bin/bash
for file in */ ; do 
  if [[ -d "$file" && ! -L "$file" ]]; then
    echo -e "${file}service-config.sh\n"
  fi; 
done