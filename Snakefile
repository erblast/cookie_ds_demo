include: 'rules/test.snakefile.py'
include: 'rules/lint.snakefile.py'
include: 'rules/report.snakefile.py'

configfile: 'config/config.yml'
report: 'docs/snakemake_report/index.rst'


rule all:
    input:
        'docs/html/plot_rmd_snakemake.html',
        'docs/html/plot_rmd_shell.html',
        'docs/png/plot_rmd_shell.png',
        'docs/html/plot_jup_nb.html',

rule load_dataset:
    output:
        'data/out/feather/data.feather'
    conda:
        'envs/cookiedsdemo_debian.yml'
    script:
        'src/py/load.py'

rule plot_rmd_snakemake:
    input:
        'data/out/feather/data.feather'
    output:
        report('docs/html/plot_rmd_snakemake.html', category = 'plot')
    script:
        'src/Rmd/plot_snakemake.Rmd'


rule plot_rmd_shell:
    input:
        'src/Rmd/plot_shell.Rmd',
        'data/out/feather/data.feather'
    output:
        report('docs/html/plot_rmd_shell.html', category = 'plot'),
        report('docs/png/plot_rmd_shell.png', category = 'plot')
    shell:
#     # snakemake removes all single quotation marks from a command therefore we use triple
#     # quotation for the outside string
        """R -e 'wd = getwd(); \
                rmarkdown::render( "{input[0]}", \
                    output_file = normalizePath( paste0( wd,"/" ,"{output[0]}" ) ), \
                    params = list(input = "{input[1]}",  \
                                  output = "{output[1]}" ), \
                    knit_root_dir = getwd(), \
                    envir = new.env() )' \
        """
        
rule plot_execute_nb_plot:
    conda:
        'envs/cookiedsdemo_debian.yml'
    input:
        'src/nb/vanilla/plot.ipynb',
        'data/out/feather/data.feather'
    output:
        'src/nb/executed/plot.ipynb'
    shell:
# papermill offers better parametrisation than snakemake
        """python -c 'import papermill as pm; \
            pm.execute_notebook(  "{input[0]}" \
                    , "{output[0]}" \
                    , parameters = dict( input = "{input[1]}") )' \
        """
        
rule plot_nb_2_html:
    conda:
        'envs/cookiedsdemo_debian.yml'
    input:
        'src/nb/executed/plot.ipynb'
    output:
        report('docs/html/plot_jup_nb.html', category = 'plot')
    shell:
        'jupyter nbconvert --to html {input} --output ../../../{output}'

