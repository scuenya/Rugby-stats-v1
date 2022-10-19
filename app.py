from email import header
import matplotlib
import streamlit as st
import pandas as pd
import numpy as np
import os
import time

# import Static
import matplotlib.pyplot as plt 
import seaborn as sns

# CSS para la pagina 
st.set_page_config(page_title='Data Profiling',layout='wide')

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)


sidebar= st.sidebar

st.header("Primera Version Rugby Markup -V1")

def validate_file(file):
    filename = file.name
    name, ext = os.path.splitext(filename)
    if ext in  ('.csv'):
        return ext
    else:
        return False
        
uploaded_file = st.file_uploader('Upload a csv file exported from Fulcrum Angles:')

def expander1(note,state):
     st.expander(note,expanded=state)

if uploaded_file is not None:  
    with st.expander('Check the Angles CSV uploadad:',expanded = False):
        ext = validate_file(uploaded_file)
        if ext:
            df = pd.read_csv(uploaded_file)
            list_of_columns = list(df.columns)
            list_of_rows = list(df["Row Name"].unique())
           
            # list_of_rows.insert(0,'All')
            list_of_teams = list(df["EQUIPO"].unique())
            list_of_teams.insert(0,'All')
            selected_columns = sidebar.multiselect('Select Columns',list_of_columns,('Row Name', 'EQUIPO', 'RESULTADO','ACTION'))
            selected_row = sidebar.selectbox('Select Row',list_of_rows,)
            df1 = df[selected_columns].fillna('0')
            if selected_row != 'All':
                st.write('true')
                df1 = df[df['Row Name']== selected_row]
            else:
                st.write('false')
                
            st.dataframe(df1)

else:
            st.error('Select a CSV file')


# Saco los DATOS
if uploaded_file is not None:
    # Tries
    df_triesA = df[(df['Row Name']=='TRY') & (df["EQUIPO"] == list_of_teams[1])]
    if len( df_triesA) != 0:
        triesA = list(df_triesA["Row Name"].value_counts())
    else:
        triesA = 0
   
    df_triesB = df[(df['Row Name']=='TRY') & (df["EQUIPO"] == list_of_teams[2])]
    if len(df_triesB) != 0:
        triesB = list(df_triesB["Row Name"].value_counts())
    else:
        triesB = 0
   
    # PENALTY TRIES
    df_p_triesA = df[(df['Row Name']=='PENALTY TRY') & (df["EQUIPO"] == list_of_teams[1])]
    if len(df_p_triesA) != 0  :
        p_triesA = list(df_p_triesA["Row Name"].value_counts())
    else:
        p_triesA = [0]
    
    df_p_triesB = df[(df['Row Name']=='PENALTY TRY') & (df["EQUIPO"] == list_of_teams[2])]
   
    if len(df_p_triesB) != 0  :
        p_triesB = list(df_p_triesB["Row Name"].value_counts())
    else:
        p_triesB = [0]

    # GOALS SUCCESS
    df_goalsA = df[(df['Row Name']=='GOAL') & (df["EQUIPO"] == list_of_teams[1]) & (df["RESULTADO"] == 'CONVERTIDO')]
    if len(df_goalsA) != 0  :
        goalsA = list(df_goalsA["Row Name"].value_counts())
    else:
        goalsA = [0]
    
    df_goalsB = df[(df['Row Name']=='GOAL') & (df["EQUIPO"] == list_of_teams[2]) & (df["RESULTADO"] == 'CONVERTIDO')]
    if len(df_goalsB) != 0  :
        goalsB = list(df_goalsB["Row Name"].value_counts())
    else:
        goalsB = [0]

   # GOALS ERROR
    df_no_goalsA = df[(df['Row Name']=='GOAL') & (df["EQUIPO"] == list_of_teams[1]) & (df["RESULTADO"] == 'ERRADO')]
    if len(df_no_goalsA) != 0:
        no_goalsA = list(df_no_goalsA["Row Name"].value_counts())
    else:
        no_goalsA = [0]
    
    df_no_goalsB = df[(df['Row Name']=='GOAL') & (df["EQUIPO"] == list_of_teams[2]) & (df["RESULTADO"] == 'ERRADO')]
    if len(df_no_goalsB) != 0  :
        no_goalsB = list(df_no_goalsB["Row Name"].value_counts())
    else:
        no_goalsB = [0]

    # PENALTY KICK SUCCESS
    df_pen_KickA = df[(df['Row Name']=='PENALTY KICK') & (df["EQUIPO"] == list_of_teams[1]) & (df["RESULTADO"] == 'CONVERTIDO')]
    if len(df_pen_KickA) != 0  :
        pen_KickA = list(df_pen_KickA["Row Name"].value_counts())
    else:
        pen_KickA = [0]
    
    df_pen_KickB = df[(df['Row Name']=='PENALTY KICK') & (df["EQUIPO"] == list_of_teams[1]) & (df["RESULTADO"] == 'CONVERTIDO')]
    if len(df_pen_KickB) != 0  :
        pen_KickB = list(df_pen_KickB["Row Name"].value_counts())
    else:
        pen_KickB = [0]

    # PENALTY KICK ERRORS
    df_no_pen_KickA = df[(df['Row Name']=='PENALTY KICK') & (df["EQUIPO"] == list_of_teams[1]) & (df["RESULTADO"] == 'ERRADO')]
    if len(df_no_pen_KickA) != 0  :
        no_pen_KickA = list(df_no_pen_KickA["Row Name"].value_counts())
    else:
        no_pen_KickA = [0]
    
    df_no_pen_KickB = df[(df['Row Name']=='PENALTY KICK') & (df["EQUIPO"] == list_of_teams[2]) & (df["RESULTADO"] == 'ERRADO')]
    if len(df_no_pen_KickB) != 0  :
        no_pen_KickB = list(df_no_pen_KickB["Row Name"].value_counts())
    else:
        no_pen_KickB = [0]


    # DROP GOALS
    df_drop_goalsA = df[(df['Row Name']=='DROP') & (df["EQUIPO"] == list_of_teams[1]) & (df["RESULTADO"] == 'CONVERTIDO')]
    if len(df_drop_goalsA) != 0  :
        drop_goalsA = list(df_drop_goalsA["Row Name"].value_counts())
    else:
        drop_goalsA = [0]
    
    df_drop_goalsB = df[(df['Row Name']=='DROP') & (df["EQUIPO"] == list_of_teams[2]) & (df["RESULTADO"] == 'CONVERTIDO')]
    if len(df_drop_goalsB) != 0  :
        drop_goalsB = list(df_drop_goalsB["Row Name"].value_counts())
    else:
        drop_goalsB = [0]

# DROP GOALS ERRADO
    df_no_drop_goalsA = df[(df['Row Name']=='DROP') & (df["EQUIPO"] == list_of_teams[1]) & (df["RESULTADO"] == 'ERRADO')]
    if len(df_no_drop_goalsA) != 0  :
        no_drop_goalsA = list(df_no_drop_goalsA["Row Name"].value_counts())
    else:
        no_drop_goalsA = [0]
    
    df_no_drop_goalsB = df[(df['Row Name']=='DROP') & (df["EQUIPO"] == list_of_teams[2]) & (df["RESULTADO"] == 'ERRADO')]
    if len(df_no_drop_goalsB) != 0  :
        no_drop_goalsB = list(df_no_drop_goalsB["Row Name"].value_counts())
    else:
        no_drop_goalsB = [0]

    # YELLOW CARD
    df_yellow_cardA = df[(df['Row Name']=='YELLOW CARD') & (df["EQUIPO"] == list_of_teams[1])]
    if len( df_yellow_cardA) != 0:
        yellow_cardA = list(df_yellow_cardA["Row Name"].value_counts())
    else:
        yellow_cardA = [0]
   
    df_yellow_cardB = df[(df['Row Name']=='YELLOW CARD') & (df["EQUIPO"] == list_of_teams[2])]
    if len(df_yellow_cardB) != 0:
        yellow_cardB = list(df_yellow_cardB["Row Name"].value_counts())
    else:
        yellow_cardB = [0]

    # RED CARD
    df_red_cardA = df[(df['Row Name']=='RED CARD') & (df["EQUIPO"] == list_of_teams[1])]
    if len(df_red_cardA) != 0:
        red_cardA = list(df_red_cardA["Row Name"].value_counts())
    else:
        red_cardA = [0]
   
    df_red_cardB = df[(df['Row Name']=='RED CARD') & (df["EQUIPO"] == list_of_teams[2])]
    if len(df_red_cardB) != 0:
        red_cardB = list(df_red_cardB["Row Name"].value_counts())
    else:
        red_cardB = [0]



    # SCRUMS GANADOS
    df_scrumA = df[(df['Row Name']=='SCRUM') & (df["EQUIPO"] == list_of_teams[1]) & (df["RESULTADO"]== 'GANADO')]
    if len(df_scrumA) != 0:
        scrumA = list(df_scrumA["Row Name"].value_counts())
    else:
        scrumA = [0]

    df_scrumB = df[(df['Row Name']=='SCRUM') & (df["EQUIPO"] == list_of_teams[2]) & (df["RESULTADO"]== 'GANADO')]
    if len(df_scrumB) != 0:
        scrumB = list(df_scrumB["Row Name"].value_counts())
    else:
        scrumB = [0]
 
    # LINEOUT GANADOS
    df_lineoutA = df[(df['Row Name']=='LINEOUT') & (df["EQUIPO"] == list_of_teams[1]) & (df["RESULTADO"]== 'GANADO')]
    if len(df_lineoutA) != 0:
        lineoutA = list(df_lineoutA["Row Name"].value_counts())
    else:
        lienoutA = [0]
    df_lineoutB = df[(df['Row Name']=='LINEOUT') & (df["EQUIPO"] == list_of_teams[2]) & (df["RESULTADO"]== 'GANADO')]
    if len(df_lineoutB) != 0:
        lineoutB = list(df_lineoutB["Row Name"].value_counts())
    else:
        lineoutB = [0]

# Armo la table (df2)
if uploaded_file is not None:
    df2 = pd.DataFrame([(triesA[0],'TRY',triesB[0]),
                        (p_triesA[0],"PENALTY TRY", p_triesB[0]),
                        (goalsA[0], 'CONVERSION SUCCESS', goalsB[0]),
                        (no_goalsA[0], "CONVERSION ERRORS", no_goalsB[0]),
                        (pen_KickA[0], "PENALTY KICK", pen_KickB[0]),
                        (no_pen_KickA[0], "PENALTY KICK ERRORS", no_pen_KickB[0]),
                        (drop_goalsA[0], "DROP GOALS", drop_goalsB[0]),
                        (no_drop_goalsA[0], "DROP GOALS ERRORS", no_drop_goalsB[0]),
                        (yellow_cardA[0], "YELLOW CARD", yellow_cardB[0]),
                        (red_cardA[0], "RED CARD", red_cardB[0]),
                        (scrumA[0], 'SCRUM', scrumB[0]),
                        (lineoutA[0], 'LINEOUT',lineoutB[0]),
                        ], columns=[list_of_teams[1], '',list_of_teams[2]])



c1, c2, c3, = st.columns(3)
if uploaded_file is not None:
    with c2:
        st.markdown('<div style="text-align: center;font-weight: bold;font-size: 23 px">FECHA</div>', unsafe_allow_html=True)
        st.table(df2)
    
    with c1:
        st.markdown('<div style="text-align: center;font-weight: bold;font-size: 23 px">Matplotly PIE</div>', unsafe_allow_html=True)
        st.caption('Pie Chart fro Team')
        with st.container():
            # 
            row_angles =df[df['Row Name'] == selected_row]
            st.subheader(selected_row)
            value_counts_teams = row_angles['EQUIPO'].value_counts()
            # draw pie chart
            fig,ax = plt.subplots()
            ax.pie(value_counts_teams, autopct='%0.2f%%',labels=[list_of_teams[1],list_of_teams[2]])
            st.pyplot(fig)
            
    with c3:
        st.markdown('<div style="text-align: center;font-weight: bold;font-size: 23 px">Matplotly BAR</div>', unsafe_allow_html=True)
        st.caption('Bar Chart from Try Count per Team')
        st.subheader(selected_row)

        # draw a bar_Chart
        fig,ax = plt.subplots()
        ax.bar([list_of_teams[1],list_of_teams[2]], value_counts_teams)
        st.pyplot(fig)

    with st.expander('Show Dataframe'):# in an expander
        st.dataframe(value_counts_teams)
        
