mkdir -p ~/.streamlit/

[theme]
primaryColor="#d33682"
backgroundColor="#002b36"
secondaryBackgroundColor="#586e75"
textColor="#fafafa"
font="serif"

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
