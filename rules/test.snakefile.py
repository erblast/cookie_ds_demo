

test_files, = glob_wildcards('cookiedsdemopkgr/tests/testthat/{test_file}.R')
function_files, = glob_wildcards('cookiedsdemopkgr/R/{function_file}.R')

rule test:
    input:
        'testlog/test_cookiedsdemopkgr.txt',
        'testlog/check_cookiedsdemopkgr.txt',
        "docs/cookiedsdemopkgr_docs/index.html"

rule test_cookiedsdemopkgr:
    input:
        expand('cookiedsdemopkgr/R/{function_file}.R', function_file = function_files),
        expand('cookiedsdemopkgr/tests/testthat/{test_file}.R', test_file = test_files)
    output:
        'testlog/test_cookiedsdemopkgr.txt'
    shell:
        "Rscript -e 'sink(\"{output}\")' -e 'devtools::test(\"./cookiedsdemopkgr\")' -e 'sink()'"
        
rule check_cookiedsdemopkgr:
    input:
        expand('cookiedsdemopkgr/R/{function_file}.R', function_file = function_files),
        expand('cookiedsdemopkgr/tests/testthat/{test_file}.R', test_file = test_files),
        'testlog/test_cookiedsdemopkgr.txt'
    output:
        'testlog/check_cookiedsdemopkgr.txt'
    shell:
        "Rscript -e 'sink(\"{output}\")' -e 'devtools::check(\"./cookiedsdemopkgr\", error_on = \"warning\")' -e 'sink()'"

rule render_docs:
    input:
        expand('cookiedsdemopkgr/R/{function_file}.R', function_file = function_files),
        expand('cookiedsdemopkgr/tests/testthat/{test_file}.R', test_file = test_files),
        'testlog/check_cookiedsdemopkgr.txt',
        "cookiedsdemopkgr/README.md"
    output:
        "docs/cookiedsdemopkgr_docs/index.html"
    shell:
        """R -e 'pkgdown::build_site("cookiedsdemopkgr/")' """



