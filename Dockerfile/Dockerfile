FROM ubuntu:16.04

ENV MINICONDA3_VERSION=4.5.4 PYTHON_VERSION=3.5 ENVIRONMENT=MLBatchAIHyperparameterTuning

RUN apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends \
        bzip2 \
        ca-certificates \
        curl \
        git \
        wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY environment.yml .

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA3_VERSION}-Linux-x86_64.sh -O ~/miniconda.sh \
    && /bin/bash ~/miniconda.sh -b -p /opt/conda \
    && rm ~/miniconda.sh \
    && /opt/conda/bin/conda env create -f environment.yml -n ${ENVIRONMENT} \
    && /opt/conda/bin/conda clean -tipsy \
    && ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
    && echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
    && echo "conda activate" ${ENVIRONMENT} >> ~/.bashrc
