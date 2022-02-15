FROM ubuntu:latest

# install python 3.9
RUN cd && \
    apt update && \
    DEBIAN_FRONTEND=noninteractive && \
    apt install -y python3.9 && \
    apt install -y python3.9-distutils && \
    apt install -y curl && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.9 get-pip.py && \
    pip --version

# install my package
RUN pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple ast-graph-draw-DLochmelis33==0.0.7 && \
    mkdir artifacts

# install dot and pdflatex dependencies
RUN apt install -y graphviz && \
    apt install -y texlive-latex-base 

# copy code into Docker
ADD ../a.py ../image.py ./

# run the program
RUN python3.9 image.py
