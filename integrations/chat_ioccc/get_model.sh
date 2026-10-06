#!/usr/bin/env bash
set -euo pipefail
LICENSE_URL="https://od.lk/d/NTJfNDgwODA2NjVf/LLAMA2_LICENSE"
MODEL_LOCATION_URL="https://od.lk/d/NTJfNDgxMDQzMzNf/model_location"
wget -q -O LLAMA2_LICENSE "$LICENSE_URL"
cat LLAMA2_LICENSE
printf '\n\n----------------\n\n'
read -r -p "Accept Meta's license to download llama2-7b-chat for ChatIOCCC. Type Y to accept: " ACCEPT
case "$ACCEPT" in
  Y|y|yes|Yes|YES)
    echo "Downloading model ..."
    rm -f LLAMA2_LICENSE model
    wget -q --show-progress -O model "$(wget -q -O - "$MODEL_LOCATION_URL")"
    ;;
  *) echo "License not accepted. Exiting."; exit 1 ;;
esac
