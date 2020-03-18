FROM cookie_ds_demo
RUN snakemake test && \
    snakemake lint && \
    snakemake -F --use-conda && \
    snakemake report && \
    snakemake --dag | dot -Tpng > ./docs/wflow/wflow.png && \
    snakemake --report docs/snakemake_report/index.html 

