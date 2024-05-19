#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\MY_Projects_Data_Analytics\T 20 world cup analysis\t20-world-cup-22 (1).csv")
print(data.head())


# In[6]:


# analysis of number of matches won by each team in the world cup:
figure = px.bar(data, 
                x=data["winner"],
                title="Number of Matches Won by teams in t20 World Cup 2022")
figure.show()
# As England won the t20 world cup 2022, England won five matches. And Both Pakistan and India won 4 matches.


# In[7]:


won_by = data["won by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['gold','lightgreen']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches Won By Runs Or Wickets')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()
# So in the t20 world cup 2022, 16 matches were won by batting first, and 13 matches were won by chasing.


# In[9]:


toss = data["toss decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['skyblue','yellow']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decisions in t20 World Cup 2022')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()
# So in 17 matches, the teams decided to bat first, and in 13 matches, the teams chose to field first. 


# In[14]:


figure = px.bar(data, 
                x=data["top scorer"], 
                y = data["highest score"], 
                color = data["highest score"],
                title="Top Scorers in t20 World Cup 2022")
figure.show()
# So, Virat Kohli scored the highest in 3 matches


# In[15]:


figure = px.bar(data, 
                x = data["player of the match"], 
                title="Player of the Match Awards in t20 World Cup 2022")
figure.show()
# Virat Kohli, Sam Curran, Taskin Ahmed, Suryakumar Yadav, and Shadab Khan got the player of the match in 2 matches. 
# No player got the player of the match award in more than two matches.


# In[16]:


figure = px.bar(data, 
                x=data["best bowler"],
                title="Best Bowlers in t20 World Cup 2022")
figure.show()
# Sam Curran was the only best bowler in 3 matches. Undoubtedly, he deserved to be the player of the tournament


# In[17]:


fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["first innings score"],
    name='First Innings Runs',
    marker_color='blue'
))
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["second innings score"],
    name='Second Innings Runs',
    marker_color='red'
))
fig.update_layout(barmode='group', 
                  xaxis_tickangle=-45, 
                  title="Best Stadiums to Bat First or Chase")
fig.show()
# So SCG was the only stadium in the world cup that was best for batting first. 
# Other stadiums didn’t make much difference while batting first or chasing.


# In[18]:


fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["first innings wickets"],
    name='First Innings Wickets',
    marker_color='blue'
))
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["second innings wickets"],
    name='Second Innings Wickets',
    marker_color='red'
))
fig.update_layout(barmode='group', 
                  xaxis_tickangle=-45, 
                  title="Best Statiums to Bowl First or Defend")
fig.show()
# SCG was the best stadium to bowl while defending the target.
# While the Optus Stadium was the best stadium to bowl first.


# In[ ]:


'''Summary
So some highlights of the t20 world cup 2022 we found from our analysis are:

1.England won the most number of matches
2.Virat Kohli scored highest in the most number of matches
3.Sam Curran was the best bowler in the most number of matches
4.More teams won by batting first
5.More teams decided to bat first
6.SCG was the best stadium to bat first
7.SCG was the best stadium to defend the target in the World Cup
8.The Optus Stadium was the best stadium to bowl first'''


# In[ ]:




