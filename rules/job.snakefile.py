# job rules must not only use unit-tested code from packages --no scripts
# jobs are not executed during CI/CD runs

rule execute_job:
    shell: """
            R -e 'devtools::load_all("src/cookiedsdemopkgr")' \
              -e 'embedded_packages_are_great()'
           """