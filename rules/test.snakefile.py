

test_files, = glob_wildcards('src/cookiedsdemopkgr/tests/testthat/{test_file}.R')
function_files, = glob_wildcards('src/cookiedsdemopkgr/R/{function_file}.R')

rule test:
    input:
        'docs/testlog/test_cookiedsdemopkgr.txt',
        'docs/testlog/check_cookiedsdemopkgr.txt',
        "docs/cookiedsdemopkgr/index.html"

rule test_cookiedsdemopkgr:
    input:
        expand('src/cookiedsdemopkgr/R/{function_file}.R', function_file = function_files),
        expand('src/cookiedsdemopkgr/tests/testthat/{test_file}.R', test_file = test_files)
    output:
        'docs/testlog/test_cookiedsdemopkgr.txt'
    shell:
        "Rscript -e 'sink(\"{output}\")' -e 'devtools::test(\"./src/cookiedsdemopkgr\")' -e 'sink()'"
        
rule check_cookiedsdemopkgr:
    input:
        expand('src/cookiedsdemopkgr/R/{function_file}.R', function_file = function_files),
        expand('src/cookiedsdemopkgr/tests/testthat/{test_file}.R', test_file = test_files),
        'docs/testlog/test_cookiedsdemopkgr.txt'
    output:
        'docs/testlog/check_cookiedsdemopkgr.txt'
    shell:
        "Rscript -e 'sink(\"{output}\")' -e 'devtools::check(\"./src/cookiedsdemopkgr\", error_on = \"warning\")' -e 'sink()'"

rule render_docs:
    input:
        expand('src/cookiedsdemopkgr/R/{function_file}.R', function_file = function_files),
        expand('src/cookiedsdemopkgr/tests/testthat/{test_file}.R', test_file = test_files),
        'docs/testlog/check_cookiedsdemopkgr.txt',
    output:
        "docs/cookiedsdemopkgr/index.html"
    shell:
        """R -e 'pkgdown::build_site("src/cookiedsdemopkgr/")' """



