library(yaml)
library(rmarkdown)

config <- yaml::read_yaml("config/config.yml")

# Render Markdown files -------------------------------------------

wd = getwd()

rmarkdown::render(".doc_templates/index_jekyll.Rmd",
                  output_file = "index.md",
                  output_dir = "./docs/",
                  params = list(rules_to_report = config$rules_to_report),
                  envir = new.env(),
                  knit_root_dir = getwd()
                  )

rmarkdown::render(".doc_templates/index_rst.Rmd",
                  output_file = "index.md",
                  output_dir = "./docs/snakemake_report/",
                  params = list(rules_to_report = config$rules_to_report),
                  envir = new.env(),
                  knit_root_dir = getwd()
)

system("pandoc ./docs/snakemake_report/index.md --from markdown --to rst -s -o ./docs/snakemake_report/index.rst")

file.remove("./docs/snakemake_report/index.md")

# Render workflows as DAG ------------------------------------------

path_wflow <-  "./docs/wflow/"

if (! dir.exists(path_wflow)) {
  dir.create(path_wflow)
}

wflow_files <-  paste0(path_wflow, config$rules_to_report, ".png")

wflow_as_png_cmd <-  paste("/opt/conda/bin/snakemake",
                         config$rules_to_report,
                         "--dag | dot -Tpng >", 
                         wflow_files)

sapply(wflow_as_png_cmd, system)


# Render Snakemake Reports ----------------------------------------

path_report <-  "./docs/snakemake_report/"

report_files <-  paste0(path_report, config$rules_to_report, ".html")

report_cmd <-  paste("/opt/conda/bin/snakemake",
                   config$rules_to_report,
                   "--report", 
                   report_files)

sapply(report_cmd, system)
