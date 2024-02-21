## create_pdf_from_md_readme.md

There are 3 actions in this workflow: 

1. `create_pdf_manually_with_marp.yml`: This action will create a PDF from the README.md file in the repository using marp and then creating a release with this file. It is triggered manually.

2. `create_pdf_manually_with_pandoc.yml`: This action will create a PDF from the README.md file in the repository using pandoc and then creating a release with this file. It is triggered manually.

3. `on_merge_create_pdfs_with_marp.yml`: This action will trigger when you push on main branch and will search if markdowns files have been modified. If so, it will create a PDF from the files using marp and then creating a release with these file/s. It installs marp from npm because i couldn't make it work with the marp docker container.

It could be that the source files in my release are a free version thing by GitHub, but if not you can the .gitattributes file to exclude the source files from the release with the command: file/directory export-ignore. <https://stackoverflow.com/questions/45240336/how-to-use-github-release-api-to-make-a-release-without-source-code>
