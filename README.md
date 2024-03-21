# Biblioteka me Streamit
Ky kod eshte dizenjuar qe te hapet me Docker, instalo docker ne fillim duke bere `sudo apt install docker.io` ose per cfare sistem ke.
Me pas, krijo nje folder ne te cilen do besh komanden `git clone https://github.com/projektgjuhe123/biblioteka` dhe me pas do hysh ne folderi biblioteka.
Me pas do besh run komanden `docker build -t streamlit .` e cila do perdore Dockerfile per te bere imazhin e projektit.
Me pas, per te hapur faqen do besh `docker run -p 8501:8501 -t streamlit` e cila do ta hape serverin ne porten 8501, kjo porte mund te ndrohet ne Dockerfile
