from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
from streamlit_flow.state import StreamlitFlowState
from streamlit_flow.layouts import RadialLayout
import streamlit as st

nodes = [
    StreamlitFlowNode(
        "main",
        (0, 0),
        {"content": "# Supercharging GTM with AI @eMazzanti"},
        "input",
        "bottom",
    ),
    StreamlitFlowNode(
        "code",
        (0, 0),
        {
            "content": """### Execution Layer
```python
print('Hello World')
```"""
        },
        "output",
        "bottom",
        "top",
    ),
    StreamlitFlowNode(
        "tasks",
        (0, 0),
        {
            "content": """## SOP's, Playbooks and Task Lists

* [ ] to do
* [x] done
"""
        },
        "output",
        "top",
        "bottom",
    ),
    StreamlitFlowNode(
        "image",
        (0, 0),
        {
            "content": """### Intent, Triggers and Proactivity
<img src="https://i.imgur.com/rKSV8m2.jpg" alt="Image 1" width="500">
<img src="https://i.imgur.com/6vrPiw6.jpg" alt="Image 2" width="500">
"""
        },
        "output",
        "top",
        "bottom",
    ),
]

edges = [
    StreamlitFlowEdge("main-code", "main", "code", animated=True),
    StreamlitFlowEdge("main-tasks", "main", "tasks", animated=True),
    StreamlitFlowEdge("main-image", "main", "image", animated=True),
]

if "markdown_node_state" not in st.session_state:
    st.session_state.markdown_node_state = StreamlitFlowState(nodes, edges)
streamlit_flow(
    "markdown_node_flow",
    st.session_state.markdown_node_state,
    layout=RadialLayout(),
    fit_view=True,
    height=1800,
)
