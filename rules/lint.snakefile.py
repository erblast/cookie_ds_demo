
rule lint:
    shell: """
            R -e 'devtools::load_all("cookiedsdemopkgr")' \
              -e'lint_package("cookiedsdemopkgr")'
           """