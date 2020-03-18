
rule report:
    input:
        'docs/snakemake_report/index.rst',
        'docs/index.md'

rule index_md_jekyll:
    output:
        'docs/index.md'
    script:
        # project directory for script does not change when imported by main snakefile
        '../src/Rmd/index_jekyll.Rmd'

rule index_md_rst:
    output:
        temp('docs/snakemake_report/index.md')
    script:
        # project directory for script does not change when imported by main snakefile
        '../src/Rmd/index_rst.Rmd'

rule index_rst:
    input:
        'docs/snakemake_report/index.md'
    output:
        'docs/snakemake_report/index.rst'
    shell:
        "pandoc {input} --from markdown --to rst -s -o {output}"
