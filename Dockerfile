FROM erblast/r_conda_snakemake_pkgs


# # install R packages: ----------------------------------------------------
# RUN R -e "remotes::install_version('plotly', repos='http://cran.us.r-project.org', version= '4.9.0' , upgrade = 'never' )"

# # install python packages -----------------------------------------------
# #
# # option 1
# # specify OS-specific conda environment yml file in envs/
# # alternatively use requirements.txt or python3 env

# # option 2
# # install directly into base environment
# RUN conda install thrift_sasl=0.2.1 -c conda-forge
# RUN pip install thrift_sasl==0.2.1

# # option 3
# # create conda env inside container
# RUN conda create --name impala python=3.6 ibis-framework=0.13.0
# RUN conda install -n impala thrift_sasl=0.2.1 -c conda-forge

# # add pip conf file if alternative pip server should be used
# # needs to be added to repo first
# ADD pip.conf /etc/ 

# ENV PATH /opt/conda/envs/impala/bin:$PATH
# RUN /bin/bash -c "source activate impala" && \
#     pip install hdfs==2.1.0 

# # activate conda environment per default
# RUN echo "conda activate impala" >> ~/.bashrc

# code folder, if data is being pulled add data/in to .dockerignore to keep build context slim
# use docker run -w /repo when executing container without mounting to repo
COPY . /repo 

# mount folder
WORKDIR /app

RUN conda env update --file /repo/envs/cookiedsdemo_conda.yml

ENV JOB_VAR1=USE_ENVVARS_TO_CONFIGURE_JOBS
ENV CORES=1

CMD snakemake test -F && \
    snakemake -F --cores $CORES && \
    R -f .doc_templates/render_docs.R 