import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(
    page_title="PTSOC",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.logo(
    'LOGO-BRANCO-RGB.png'
)

st.markdown("# PTSOC Scorecard Dashboard")
# st.sidebar.markdown("# Scorecard ")


st.text('Sobre registrar website...')

from datetime import datetime
st.code(f'Update time : {datetime.today().strftime("%d-%m-%Y %H:%M:%S")}')

# Donut chart
def make_donut_2(input_response, input_text, input_color):
  if input_color == 'blue':
      chart_color = ['#29b5e8', '#155F7A']
  if input_color == 'green':
      chart_color = ['#27AE60', '#12783D']
  if input_color == 'orange':
      chart_color = ['#F39C12', '#875A12']
  if input_color == 'red':
      chart_color = ['#E74C3C', '#781F16']
    
  source = pd.DataFrame({
      "Topic": ['', input_text],
      "value": [109-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "value": [109, 0]
  })
    
  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
  ).properties(width=130, height=130)
    
  text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response}'))
  plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
  ).properties(width=130, height=130)
  return plot_bg + plot + text



import duckdb

# create a connection to a file called 'file.db'
con = duckdb.connect("pages/dns_crowler_database.db", read_only=False)

df = con.sql("""
        SELECT 
        *
        FROM dns_crowler_database.main.dns_dados_tratados;
        """).df()


dnssec = len(df[df['HAS_DNSSEC'] == 'Y'])
# st.write(f'dnssec: {dnssec}')

tlsa = len(df[df['HAS_WEB_DANE'] == 'Y'])
# st.write(f'tlsa: {tlsa}')

is_redirect = len(df[df['is_redirect'] == 'Y'])
# st.write(f'https: {https}')

cert = len(df[df['certificate'] == 'Y'])
# st.write(f'cert: {cert}')


hsts = len(df[df['HSTS'] == 'Y'])
# st.write(f'hsts: {hsts}')


st.markdown("## WEB 🌐")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    #st.header("DNSSEC", anchor=False)
    st.markdown("#### DNSSEC")
    st.altair_chart(make_donut_2(dnssec, 'DNSSEC', 'green'), use_container_width=True)
    # st.container().container(border=True).caption('Note...')

with col2:
    # st.header("Dane", anchor=False)
    st.markdown("#### Dane")
    st.altair_chart(make_donut_2(tlsa, 'Protocolo TLSA', 'green'), use_container_width=True)
    # st.container().container(border=True).caption('Note...')

with col3:
    # st.header("Is Redirect", anchor=False)
    st.markdown("#### Is Redirect")
    st.altair_chart(make_donut_2(is_redirect, 'Is Redirect', 'green'), use_container_width=True)
    # st.container().container(border=True).caption('Note...')

with col4:
    # st.header("Certificate", anchor=False)
    st.markdown("#### Certificate")
    st.altair_chart(make_donut_2(cert, 'Certificate', 'green'), use_container_width=True)
   # st.container().container(border=True).caption('Note...')

with col5:
    # st.header("HSTS", anchor=False)
    st.markdown("#### HSTS")
    st.altair_chart(make_donut_2(hsts, 'HSTS', 'green'), use_container_width=True)
    # st.container().container(border=True).caption('Note...')

with col6:
    # st.header("DNS Abuse", anchor=False)
    st.markdown("#### DNS Abuse")
    st.altair_chart(make_donut_2(5, 'Abuse', 'green'), use_container_width=True)
    # st.container().container(border=True).caption('Note...')



############################################



spf = len(df[df['HAS_TXT_SPF'] == 'Y'])
# st.write(f'spf: {spf}')

dmarc = len(df[df['HAS_TXT_DMARC'] == 'Y'])
# st.write(f'dmarc: {dmarc}')

dkim = len(df[df['HAS_TXT_DKIM'] == 'Y'])
# st.write(f'dkim: {dkim}')

dnssec = len(df[df['HAS_DNSSEC'] == 'Y'])
# st.write(f'dnssec: {dnssec}')


st.divider()



st.markdown("## EMAIL 📧")

col1, col2, col3, col4 = st.columns(4)

with col1:
    # st.header("SPF", anchor=False)
    st.markdown("#### SPF")
    st.altair_chart(make_donut_2(spf, 'TXT_SPF', 'green'), use_container_width=True)
    # st.container().container(border=True).caption('Note...')

with col2:
    # st.header("DMARC", anchor=False)
    st.markdown("#### DMARC")
    st.altair_chart(make_donut_2(dmarc, 'TXT_DMARC', 'green'), use_container_width=True)
    # st.container().container(border=True).caption('Note...')

with col3:
    # st.header("DKIM", anchor=False)
    st.markdown("#### DKIM")
    st.altair_chart(make_donut_2(dkim, 'TXT_DKIM', 'orange'), use_container_width=True)
   # st.container().container(border=True).caption('Note...')

with col4:
    # st.header("DNSSEC", anchor=False)
    st.markdown("#### DNSSEC")
    st.altair_chart(make_donut_2(dnssec, 'DNSSEC', 'orange'), use_container_width=True)
    # st.container().container(border=True).caption('Note...')


st.divider()


tab1, tab2 = st.tabs(["Top Registrar", "Registrar"])



df_registrar = df[:]

# if len(choices) == 0:
#     st.dataframe(df_registrar)
# else:
#     st.write(df_registrar[df_registrar['domain'].isin(choices)])


# Define the scoring function
def calculate_security_score(row):
    score = 0
    
    # Assign points based on each protocol
    score += 10 if row['HAS_DNSSEC'] == 'Y' else 0
    score += 5 if row['HAS_WEB_DANE'] == 'Y' else 0
    score += 5 if row['is_redirect'] == True else 0
    score += 5 if row['certificate'] == True else 0
    score += 5 if pd.notna(row['x-content-type-options']) else 0
    score += 5 if row['HSTS'] == True else 0
    score += 5 if row['HAS_TXT_SPF'] == 'Y' else 0
    score += 10 if row['HAS_TXT_DMARC'] == 'Y' else 0
    score += 5 if row['HAS_TXT_DKIM'] == 'Y' else 0
    
    return score


# Define the scoring function web
def calculate_security_score_web(row):
    score = 0
    
    # Assign points based on each protocol
    score += 10 if row['HAS_DNSSEC'] == 'Y' else 0
    score += 5 if row['HAS_WEB_DANE'] == 'Y' else 0
    score += 5 if row['is_redirect'] == True else 0
    score += 5 if row['certificate'] == True else 0
    score += 5 if pd.notna(row['x-content-type-options']) else 0
    score += 5 if row['HSTS'] == True else 0

    return score

# Define the scoring function mail
def calculate_security_score_mail(row):
    score = 0

    # Assign points based on each protocol
    score += 5 if row['HAS_TXT_SPF'] == 'Y' else 0
    score += 10 if row['HAS_TXT_DMARC'] == 'Y' else 0
    score += 5 if row['HAS_TXT_DKIM'] == 'Y' else 0

    return score


# Apply the function to each row
df_registrar['security_score'] = df_registrar.apply(calculate_security_score, axis=1)

# web
df_registrar['security_score_web'] = df_registrar.apply(calculate_security_score_web, axis=1)

# mail
df_registrar['security_score_mail'] = df_registrar.apply(calculate_security_score_mail, axis=1)

# Sort the domains by the security score in descending order
ranked_data = df_registrar[['domain', 'security_score', 'security_score_web', 'security_score_mail']].sort_values(by='security_score', ascending=False)



with tab1:

    with st.expander('Sobre o cálculo do score... ', expanded=False, icon="🚨"):
        st.write('''
            - Web
                - :orange[**DNSSEC**]: Pontuação 10 para dominio com o protocolo configurado.
                - :orange[**DANE**]: Pontuação 5 para dominio com o protocolo configurado.
                - :orange[**Redirect**]: Pontuação 5 para dominio com o protocolo configurado.
                - :orange[**Certificado**]: Pontuação 10 para dominio com o protocolo configurado.
                - :orange[**HSTS**]: Pontuação 10 para dominio com o protocolo configurado.
            - Email  
                - :orange[**SPF**]: Pontuação 10 para dominio com o protocolo configurado.
                - :orange[**DMARC**]: Pontuação 10 para dominio com o protocolo configurado.
                - :orange[**DKIM**]: Pontuação 10 para dominio com o protocolo configurado.
            ''')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Top 10 Registrar ...")
        # Display the top 10 ranked domains
        st.dataframe(ranked_data[['domain', 'security_score']].head(10), hide_index=True,

            column_config={
                "security_score": st.column_config.NumberColumn(
                "security_score",
                help="Streamlit **widget** commands 🎈",
                width="medium",
                min_value=30,
                max_value=1000,
                step=1,
                format="%d ⭐"

            )
        })


    with col2:
        st.header("Top 10 by Web protocol 🌐 ...")
        # Display the top 10 ranked domains
        st.dataframe(ranked_data[['domain', 'security_score_web']].head(10).sort_values(by='security_score_web', ascending=False)
                     , hide_index=True
                     ,column_config={
                "security_score_web": st.column_config.NumberColumn(
                "security_score_web",
                help="Streamlit **widget** commands 🎈",
                width="medium",
                min_value=30,
                max_value=1000,
                step=1,
                format="%d ⭐"

            )
        })


    with col3:
        st.header("Top 10 by Email protocol 📧 ...")
        # Display the top 10 ranked domains
        st.dataframe(ranked_data[['domain', 'security_score_mail']].head(10).sort_values(by='security_score_mail', ascending=False)
                     , hide_index=True
                     ,column_config={
                "security_score_mail": st.column_config.NumberColumn(
                "security_score_mail",
                help="Streamlit **widget** commands 🎈",
                width="medium",
                min_value=30,
                max_value=1000,
                step=1,
                format="%d ⭐"

            )
        })



with tab2:
    st.header("Dados ...")
    
    regular_search_term = df['domain'].unique().tolist()
    choices = st.multiselect(" ",regular_search_term)
    # st.dataframe(df, height=10*len(df)+10, hide_index=True)

    if len(choices) == 0:
        st.dataframe(df, height=6*len(df), hide_index=True)
    else:
        st.dataframe(df[df['domain'].isin(choices)], hide_index=True)

