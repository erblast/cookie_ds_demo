
rule lint:
    shell: """
            R -e 'devtools::load_all("src/cookiedsdemopkgr")' \
              -e 'lint_package("src/cookiedsdemopkgr")'
           """