FROM cookie_ds_demo
CMD snakemake test -F && \
    snakemake lint -F 

