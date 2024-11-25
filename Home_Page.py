import streamlit as st
from Portfolio import portfolio_page  
from teammate_portfolio import teammate_portfolio_page 


st.title("Web Development Lab03")


st.header("CS 1301")
st.subheader("Team 39, Web Development - Section B")
st.subheader("Maya Matthews,tA")


st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **Home Page**: Overview of the lab project.
2. **Page 1**: maya M's Portfolio.
3. **Page 2**: TA's Portfolio.
4. **More Pages**: Additional pages added in later phases.
""")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home Page", "Page 1", "Page 2"])


if page == "Home Page":
    st.title("Welcome to Web Development Lab03!")
    st.markdown("### **Portfolio Pages**")
    st.markdown("- **Page 1**: MM's Portfolio")
    st.markdown("- **Page 2**: TA's Portfolio")
elif page == "Page 1":
    portfolio_page() 
elif page == "Page 2":
    teammate_portfolio_page()  
