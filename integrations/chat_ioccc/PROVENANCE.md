# ChatIOCCC Echo backend

Vendored from the official IOCCC winner repository:

- Upstream repository: `ioccc-src/winner`
- Upstream path: `2024/cable1`
- Upstream `prog.c` blob: `532ffc0721f926fc15c15740e886dcc5e0f64578`
- Upstream `get_model.sh` blob: `0dce8ea53140d0083e30dde5431b35d41980ac4a`
- Official entry: https://www.ioccc.org/2024/cable1/index.html
- Upstream source: https://github.com/ioccc-src/winner/tree/master/2024/cable1

The official entry identifies ChatIOCCC as an LLM inference engine for Meta LLaMA 2 7B Chat, requiring about 11 GB RAM and a separate model download after accepting Meta's license.

## Local integration

This directory keeps the upstream inference source as `prog.c`. The local Makefile is intentionally standalone because the upstream Makefile depends on IOCCC repository-level include files. It compiles an `echo` binary with a TCGE Echo system prompt.

Build:

```sh
make
./get_model.sh
./echo
```

The model weights are not committed to this repository. Acceptance of Meta's model license remains a human/runtime step.

## License/provenance

Preserve upstream attribution and applicable license terms. The IOCCC entry page identifies CC BY-SA 4.0 for the published material. Review the upstream repository and Meta model license before redistribution or deployment.
