import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("MPHD")
st.header("Master of Hacking & Developing")
st.subheader("I will be a good MPHD")

st.write("I have completed my Diploma in Computer Enginerring.(Great Experience there)")
st.markdown("Currently I have took admission in Manglaytan University for Lateral entry in CSE.")
st.caption("Note:I am not sure about quality of education,infrastructure,teachers,students there.")


st.markdown("<br>",unsafe_allow_html=True)
st.write("Image:")
st.image("image.jpeg")

st.markdown("<br>",unsafe_allow_html=True)
st.write("Audio:")
st.audio("song.mp3")

st.markdown("<br>",unsafe_allow_html=True)
st.write("Video:")
st.video("video.mp4")



#to give line breaks
st.markdown("<br>",unsafe_allow_html=True)

#form

st.checkbox("Are you an Indian")

st.radio("Pick your City:",["Aligarh","Agra","Meerut","Delhi"])  #only one can be selected

st.selectbox("Select your age range:",["Below 18","Above 18","Above 45","Above 72"]) #Drop down with single select facility
st.multiselect("Choose your Subjects:",["Operating System","English","Hindi","DSA","DBMS"]) #Drop down with multi select facility

st.select_slider("Your experience at AMU:",['Bad',"Good","Excelent"])
st.slider("Your CGPA:",0,10)


on=st.toggle("Are you ready for this jurney :")
if on:
    st.toast("Please!Tight your seatbelt")





#to give line breaks
st.markdown("<br><br>",unsafe_allow_html=True)


#Various inputs in form
st.text_input("Enter name:")

st.number_input("Enter your age:",step=1) #step value to tell incrementing factor.default is 0.1


st.text_area("Write about yourself in 50 words.")

st.date_input("Enter your D.O.B:",value=None)

st.time_input("Enter your birth time",value=None)

st.file_uploader("Upload your photo",accept_multiple_files=False,)

st.color_picker("Choose your lucky colour:")


st.button("I am a Button")


#Adding sidebar

st.sidebar.title("MPHD")
st.sidebar.image("image.jpeg",width=100,)
st.sidebar.write("Home")
st.sidebar.write("About")
st.sidebar.write("Setting")




#to give line breaks
st.markdown("<br>",unsafe_allow_html=True)

#Ways to choose differnet types of message.
st.success("It is an example of success message")
st.error("It is an example of error message")
st.warning("It is an example of warning message")
st.info("It is an example of information message",)
st.exception(RuntimeError("Run-time error exception message example"))



#Internal progress meter

st.subheader("Progress meter")

with st.status("Communicating with server (Click for more details)"):
    st.write("Step 1:Validating details")
    time.sleep(0.1)
    st.write("Step 2:Fetching records")
    time.sleep(0.1)
    st.write("Step 3:Writing log details in PC")
    time.sleep(0.1)
    st.toast("Data fetched successfully")
st.button("Rerun")


#In Streamlit, pressing any button (like `st.button("")`) causes the entire script to rerun from the top.
# This is how Streamlit maintains the app's state and updates the UI on users actions(But it remember every widgets previous state)
#so inputs remains as they were previously


#Showing tables in different formats

st.subheader("Showing tables in different styles")

st.write("In dataframe form (preferred):")
st.dataframe(pd.DataFrame(np.random.randn(50,20),columns=("Col %d" % i for i in range(1,21))))

st.write("In table form:")
st.table(pd.DataFrame(np.random.randint(10,100,50).reshape(10,5),columns=[f"Col {i}" for i in range(1,6)]))


#Different types of plots:

st.header("Different types of plots:")

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])

#provide zooming facility

st.write("Area chart")
st.area_chart(chart_data)

st.write("Bar chart")
st.bar_chart(chart_data)

st.write("Line chart")
st.line_chart(chart_data)

st.write("Scatter chart")
st.scatter_chart(chart_data)


#Showing map
st.subheader("Map:")


df=pd.DataFrame({"lat":[27.9135063],"lon":[78.0756152]})

st.map(df)




#chat sort of interface
prompt=st.chat_input("Enter your question")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("ai"):
        st.write("Something went wrong...")






#   The with statement in Python is primarily used for resource management,
#
#    It gurrantes that all the resourse in block that acquired during entering the block
#   will be released upon exit of with block





#String formatting
#name = "Alice"
#age = 25
#print("Name: %s, Age: %d" % (name, age))



#st.markdown("<br><br><br>",unsafe_allow_html=True)   inplace of this we can use 
#st.write("")
#st.write("")
#st.write("")



