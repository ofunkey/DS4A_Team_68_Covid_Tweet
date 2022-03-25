mkdir -p ~/.streamlit/

echo "\
[theme]\n\
primaryColor="#d33682"\n\
backgroundColor="#002b36"\n\
secondaryBackgroundColor="#586e75"\n\
textColor="#fafafa"\n\
font="serif"\n\
\n\
"> ~/.streamlit/config.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
