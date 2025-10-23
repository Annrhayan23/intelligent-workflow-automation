import streamlit as st
import os
from backend import document_ai, generative_ai, database, workflow

st.set_page_config(page_title='Intelligent Workflow Automation')
st.title('📄 Intelligent Workflow Automation')

os.makedirs('data', exist_ok=True)

uploaded_file = st.file_uploader('Upload Document (PDF, JPG, PNG or .txt)', type=['pdf', 'jpg', 'png', 'txt'])

if uploaded_file is not None:
    save_path = os.path.join('data', uploaded_file.name)
    with open(save_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.success(f'Saved to {save_path}')

    text = ''
    try:
        if uploaded_file.name.lower().endswith('.pdf'):
            text = document_ai.extract_text_from_pdf(save_path)
        elif uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            text = document_ai.extract_text_from_image(save_path)
        else:
            with open(save_path, 'r', encoding='utf-8', errors='replace') as f:
                text = f.read()
    except Exception as e:
        st.warning(f'Could not extract using heavy libraries: {e}\nFalling back to reading bytes as text.')
        try:
            with open(save_path, 'r', encoding='utf-8', errors='replace') as f:
                text = f.read()
        except Exception:
            text = ''

    if not text:
        st.info('No text extracted. You can still enter text manually below.')

    st.subheader('Extracted Text')
    st.text_area('Text', value=text, height=200)

    entities = document_ai.extract_entities(text)
    st.subheader('Extracted Entities')
    st.json(entities)

    action = workflow.decide_next_action(entities)
    st.subheader('Suggested Action')
    st.write(action)

    doc_id = database.save_document(text, entities)
    st.success(f'Document saved with id: {doc_id}')

    summary = generative_ai.summarize_document(text)
    email = generative_ai.generate_email(entities, summary)
    st.subheader('Summary')
    st.write(summary)
    st.subheader('Generated Email')
    st.text_area('Email', value=email, height=200)
else:
    st.info('Upload a document to get started.')
