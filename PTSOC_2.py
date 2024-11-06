import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(
    page_title="PTSOC Info",
    page_icon="🚧",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.logo(
    'LOGO-BRANCO-RGB.png'
)

st.markdown("# PTSOC 2 🚧")
st.sidebar.markdown("# PTSOC 2 🚧")


st.text('Sobre registrar website...')

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
      "% value": [109-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [109, 0]
  })
    
  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="% value",
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
      theta="% value",
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

tlsa = len(df[df['HAS_WEB_TLSA'] == 'Y'])
# st.write(f'tlsa: {tlsa}')

https = len(df[df['is_redirect_1'] == 1])
# st.write(f'https: {https}')

cert = len(df[df['certificate_2'] == 1])
# st.write(f'cert: {cert}')

flag = len(df[df['x-content-type-options'] != ""])
# st.write(f'sec flag: {flag}')

hsts = len(df[df['HSTS'] == 1])
# st.write(f'hsts: {hsts}')

ttt = make_donut_2(dnssec, 'Inbound Migration', 'green')

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.header("A cat")
    st.altair_chart(ttt, use_container_width=True)

with col2:
    st.header("A dog")
    st.altair_chart(ttt, use_container_width=True)

with col3:
    st.header("An owl")
    st.altair_chart(ttt, use_container_width=True)

with col4:
    st.header("A cat", anchor=False)
    st.altair_chart(ttt, use_container_width=True)

with col5:
    st.header("A dog")
    st.altair_chart(ttt, use_container_width=True)

with col6:
    st.header("An owl")
    st.altair_chart(ttt, use_container_width=True)


st.markdown("## WEB 🚧")
row1 = st.columns(6)

row1[0].container(border=True).caption('DNSSEC')
# row1[0].container(border=True).text("HAS_DNSSEC")
row1[0].container(border=True).title(f"😐 {dnssec}", anchor=False)



row1[1].container(border=True).caption('TLSA')
# row1[1].container(border=True).text("HTTPS")
row1[1].container(border=True).title(f"😞 {tlsa}", anchor=False)

row1[2].container(border=True).caption('HTTPS')
# row1[2].container(border=True).text("redirect")
row1[2].container(border=True).title(f"🙂 {https}", anchor=False)

row1[3].container(border=True).caption('cert')
# row1[4].container(border=True).text("cert")
row1[3].container(border=True).title(f"🙂 {cert}", anchor=False)

row1[4].container(border=True).caption('sec flag')
# row1[5].container(border=True).text("sec flag")
row1[4].container(border=True).title(f"✅ {flag}", anchor=False)

row1[5].container(border=True).caption('HSTS')
# row1[6].container(border=True).text("HSTS")
row1[5].container(border=True).title(f"😞 {hsts}", anchor=False)





############################################



spf = len(df[df['HAS_TXT_SPF'] == 'Y'])
# st.write(f'spf: {spf}')

dmarc = len(df[df['HAS_TXT_DMARC'] == 'Y'])
# st.write(f'dmarc: {dmarc}')

dkim = len(df[df['HAS_TXT_DKIM'] == 'Y'])
# st.write(f'dkim: {dkim}')

dnssec = len(df[df['HAS_DNSSEC'] == 'Y'])
# st.write(f'dnssec: {dnssec}')


st.markdown("## EMAIL 🚧")
row1 = st.columns(4)

row1[0].container(border=True).caption('TXT_SPF')
# row1[0].container(border=True).text("TXT_SPF")
row1[0].container(border=True).title(f"🙂 {spf}", anchor=False)

row1[1].container(border=True).caption('TXT_DMARC')
# row1[1].container(border=True).text("TXT_DMARC")
row1[1].container(border=True).title(f"🙂 {dmarc}", anchor=False)

row1[2].container(border=True).caption('TXT_DKIM')
# row1[2].container(border=True).text("TXT_DKIM")
row1[2].container(border=True).title(f"😕 {dkim}", anchor=False)

row1[3].container(border=True).caption('DNSSEC')
# row1[3].container(border=True).text("DNSSEC")
row1[3].container(border=True).title("🚧...", anchor=False)





regular_search_term = df['domain'].unique().tolist()
choices = st.multiselect(" ",regular_search_term)

df_registrar = df[['domain',
                   'HAS_DNSSEC', 
                   'HAS_WEB_TLSA', 
                   'is_redirect_1', 
                   'certificate_2', 
                   'x-content-type-options',
                   'HSTS',
                   'HAS_TXT_SPF',
                   'HAS_TXT_DMARC',
                   'HAS_TXT_DKIM'
                   ]]

if len(choices) == 0:
    st.dataframe(df_registrar)
else:
    st.write(df_registrar[df_registrar['domain'].isin(choices)])


# Define the scoring function
def calculate_security_score(row):
    score = 0
    
    # Assign points based on each protocol
    score += 10 if row['HAS_DNSSEC'] == 'Y' else 0
    score += 5 if row['HAS_WEB_TLSA'] == 'Y' else 0
    score += 5 if row['is_redirect_1'] == True else 0
    score += 5 if row['certificate_2'] == True else 0
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
    score += 5 if row['HAS_WEB_TLSA'] == 'Y' else 0
    score += 5 if row['is_redirect_1'] == True else 0
    score += 5 if row['certificate_2'] == True else 0
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


col1, col2, col3 = st.columns(3)

with col1:
    st.header("All 🚧 ...")
    # Display the top 10 ranked domains
    st.dataframe(ranked_data[['domain', 'security_score']].head(10), hide_index=True,

        column_config={
            "security_score": st.column_config.NumberColumn(
            "security_score",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            format="%d ⭐"

        )
    })


with col2:
    st.header("Web 🌐 ...")
    # Display the top 10 ranked domains
    st.dataframe(ranked_data[['domain', 'security_score_web']].head(5).sort_values(by='security_score_web', ascending=False), hide_index=True)


with col3:
    st.header("Email 📧 ...")
    # Display the top 10 ranked domains
    st.dataframe(ranked_data[['domain', 'security_score_mail']].head(5).sort_values(by='security_score_mail', ascending=False), hide_index=True)



