# Minimal Streamlit demo UI
try:
    import streamlit as st
    from core.agent import DebugAgent

    agent = DebugAgent()
    st.title('Context-Aware Debugging Agent (Demo)')
    error = st.text_area('Paste an error message or stack trace here:')
    if st.button('Get Suggestions'):
        if not error.strip():
            st.info('Please provide an error message.')
        else:
            suggestions = agent.handle_error(error)
            for s in suggestions:
                st.write('-', s)
except Exception as e:
    print('Streamlit not installed or running in incompatible environment.') 
