import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("📄 Advanced RAG Chatbot")

# ---------- Upload ----------
st.header("Upload Document")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Uploading & indexing..."):
        res = requests.post(
            f"{API_URL}/upload",
            files={"file": uploaded_file}
        )

    if res.status_code == 200:
        try:
            data = res.json()
            st.success(data.get("message", "Uploaded successfully"))
        except Exception:
            st.error("Server did not return JSON")
            st.code(res.text)
    else:
        st.error(f"Upload failed ({res.status_code})")
        st.code(res.text)

# ---------- Chat ----------
st.header("Ask a Question")

query = st.text_input("Enter your question")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        res = requests.post(
            f"{API_URL}/chat",
            params={"query": query}
        )

    if res.status_code == 200:
        try:
            st.write("### Answer")
            st.write(res.json()["answer"])
        except Exception:
            st.error("Invalid response from server")
            st.code(res.text)
    else:
        st.error(f"Chat failed ({res.status_code})")
        st.code(res.text)



# import streamlit as st
# import requests

# st.set_page_config("Advanced RAG")

# st.title("📚 Advanced RAG Chatbot")

# st.subheader("Upload Document")
# file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])

# if file:
#     res = requests.post(
#         "http://localhost:8000/upload",
#         files={"file": file}
#     )
#     st.success(res.json()["message"])

# st.subheader("Ask Question")
# query = st.text_input("Enter your question")

# if st.button("Ask"):
#     res = requests.post(
#         "http://localhost:8000/chat",
#         params={"query": query}
#     )
#     st.markdown("### Answer")
#     st.write(res.json()["answer"])

