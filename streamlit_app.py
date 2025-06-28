import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.video("PC_Builder_Video_Request_Fulfilled.mp4")
st.title("PC Builder")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    response = model.invoke(input_text)
    st.markdown(response.content)


with st.form("my_form"):
    
    size = st.selectbox("Go ahead and choose the desired size of your PC:", ["Very small", "Small", "Medium", "Large", "Extra Large - typically custom/unusual cases"])
    usage = st.selectbox("What will you use the PC for: ", ["Gaming PC", "PC for basic studying/work", "PC for instensive apps like Blender"])
    games = ''
    if usage=="Gaming PC":
        games = st.selectbox("How demanding games do you plan on playing:", ["I do not plan to play games ", "Light games - Terraria, Stardew Valley", "Medium games - Minecraft, Fortnite", "Intesive games - Cyberpunk 2077, Black Myth Wukong"])
    storage = st.selectbox("How big of a storage drive you want:", ["Small - Browsing internet, small games/apps", "Medium - A few games, storing some movies/videos", "Big - Storing many games/photos/videos"])
    also = st.text_area(
        "If you have any other requirements or you want to add something put in the this box:",
        "f.e. I want the PC case to have LED lights",
    )
    
    text = f'Search for parts for a PC of a {size} size, it will be a {usage} {games} the storage should be {storage}. Make a single build make a list of all the parts with their most important specs, names and pricepoints: motherboard, CPU, GPU if needed, case, RAM, storage, power supply. Put a price (sum of the parts) for the PC. {also}. Dont ask any more questions just lists the possibilities (you can add shorts comments to the parts/whole set). Double check, that the parts will fit in the case'
    
    
    submitted = st.form_submit_button("Submit")
    
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
        
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
