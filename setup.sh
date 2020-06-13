mkdir -p ~/.streamlit/

Echo "\
[server]\n\
Headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml