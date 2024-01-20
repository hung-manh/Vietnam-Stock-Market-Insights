from .config import *
from pathlib import Path    

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text(encoding='utf8')


def render():
    st.markdown(read_markdown_file("README.md"), unsafe_allow_html=True)    
