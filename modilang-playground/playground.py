import streamlit as st
from modilang.parser import ModiLangParser
from modilang.interpreter import ModiLangInterpreter
import contextlib
import io

st.set_page_config(page_title="ModiLang Playground", layout="centered")

st.title("ModiLang Playground")
st.caption("Made in India, lmao")

default_code = '''Bhaiyon aur Beheno
Vikas hai x: int ka 10
Mitron! boliye x
Acche din aa gaye hai
'''

code_input = st.text_area(" Enter your ModiLang code here:", value=default_code, height=250)

if st.button("Run ModiLang"):
    try:
        parser = ModiLangParser(code_input)
        stmts = parser.parse()

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            interpreter = ModiLangInterpreter(stmts)
            interpreter.run()

        output = buffer.getvalue()
        st.success("Execution Complete")
        st.code(output)

    except Exception as e:
        st.error("Error:")
        st.code(str(e))
