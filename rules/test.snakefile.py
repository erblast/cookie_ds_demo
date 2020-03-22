configfile: 'config/config.yml'

# cookiedsdemopkgr testing

test_files, = glob_wildcards('src/cookiedsdemopkgr/tests/testthat/{test_file}.R')
function_files, = glob_wildcards('src/cookiedsdemopkgr/R/{function_file}.R')

rule test:
    input:
        'docs/testlog/test_cookiedsdemopkgr.txt',
        'docs/testlog/check_cookiedsdemopkgr.txt',
        "docs/testlog/cookiedsdemopkgr_lint.txt", 
        "docs/cookiedsdemopkgr/index.html"

rule test_cookiedsdemopkgr:
    input:
        expand('src/cookiedsdemopkgr/R/{function_file}.R', function_file = function_files),
        expand('src/cookiedsdemopkgr/tests/testthat/{test_file}.R', test_file = test_files)
    output:
        report('docs/testlog/test_cookiedsdemopkgr.txt', category="test")
    shell:
        "Rscript -e 'sink(\"{output}\")' -e 'devtools::test(\"./src/cookiedsdemopkgr\")' -e 'sink()'"
        
rule check_cookiedsdemopkgr:
    input:
        expand('src/cookiedsdemopkgr/R/{function_file}.R', function_file = function_files),
        expand('src/cookiedsdemopkgr/tests/testthat/{test_file}.R', test_file = test_files),
        'docs/testlog/test_cookiedsdemopkgr.txt'
    output:
        report('docs/testlog/check_cookiedsdemopkgr.txt', category="check")
    shell:
        "Rscript -e 'sink(\"{output}\")' \
                 -e 'devtools::check(\"./src/cookiedsdemopkgr\", error_on = \"{config[fail_check_on]}\")' \
                 -e 'sink()'"

rule render_docs:
    input:
        expand('src/cookiedsdemopkgr/R/{function_file}.R', function_file = function_files),
        expand('src/cookiedsdemopkgr/tests/testthat/{test_file}.R', test_file = test_files),
        'docs/testlog/check_cookiedsdemopkgr.txt',
    output:
        "docs/cookiedsdemopkgr/index.html"
    shell:
        """R -e 'pkgdown::build_site("src/cookiedsdemopkgr/")' """

if config["lint"]:
  rule lint:
    input:
        "docs/cookiedsdemopkgr/index.html"
    output:
      report("docs/testlog/cookiedsdemopkgr_lint.txt", category="lint")
    shell: """
              Rscript -e 'sink(\"{output}\")' \
                      -e 'devtools::load_all("src/cookiedsdemopkgr")' \
                      -e 'lint_package("src/cookiedsdemopkgr")' \
                      -e 'sink()' \
             """
else:
  rule lint:
    shell: ""


