#!/usr/bin/env python
# coding: utf-8

# # Importing Librariers

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# # Loading the dataset

# In[59]:


df = pd.read_csv(r"C:\Users\sneha\Downloads\hotel_booking.csv")


# # Exploratory Data Cleaning & Analysis

# In[60]:


df.head()


# In[61]:


df.tail()


# In[62]:


df.shape


# In[63]:


df.columns


# In[64]:


df.info()


# In[65]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[66]:


df.info()


# In[67]:


df.describe(include = "object")


# In[68]:


for col in df.describe(include = "object").columns:
    print(col)
    print (df[col].unique())
    print("-"*50)


# In[69]:


df.isnull().sum()


# In[70]:


df.drop(["company","agent"], axis = 1, inplace = True)
df.dropna(inplace = True)


# In[71]:


df.isnull().sum()


# In[72]:


df = df[df['adr'] < 5000]


# # Data Analysis & Visualisation

# In[73]:


canceled_perc = df['is_canceled'].value_counts(normalize = True)
print (canceled_perc)

plt.figure(figsize = (5,4))
plt.title('Reservation Status Count')
plt.bar(['Not Canceled','Canceled'],df['is_canceled'].value_counts(), edgecolor = 'k', width = 0.7)
plt.show()


# In[82]:


plt.figure(figsize = (10,4))
ax1 = sns.countplot (x = 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_lables,_ = ax1. get_legend_handles_labels()
plt.title('Reservation status in different hotels', size = 20)
plt.xlabel('Hotel')
plt.ylabel('Number of Reservations')
plt.show()


# In[85]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel ['is_canceled'].value_counts(normalize = True)


# In[86]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel ['is_canceled'].value_counts(normalize = True)


# In[87]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[164]:


plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in City and Resort Hotel', fontsize = 30)
plt.plot (resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot (city_hotel.index, city_hotel['adr'], label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[166]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))
ax1 = sns.countplot (x = 'month', hue = 'is_canceled', data = df , palette = 'bright')
legend_labels,_ = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor = (1,1))
plt.title('Reservation Status Per Month', size = 20)
plt.xlabel('Month')
plt.ylabel('Number of Reservations')
plt.legend(['not canceled' , 'canceled'])
plt.show


# In[130]:


plt.figure(figsize = (15,8))
plt.title('ADR per month' , fontsize = 30)
sns.barplot(x='month', y='adr', data=df[df['is_canceled'] == 'Canceled'].groupby('month')[['adr']].sum().reset_index())
plt.show()


# In[133]:


cancelled_data = df[df['is_canceled'] == 'Canceled']
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('Top 10 Countries with Reservation Cancelled')
plt.pie(top_10_country, autopct = '%.2f', labels = top_10_country.index)
plt.show()


# In[118]:


df['market_segment'].value_counts()


# In[120]:


df['market_segment'].value_counts(normalize = True)


# In[134]:


cancelled_data ['market_segment'].value_counts(normalize = True)


# In[155]:


canceled_data = df[df['is_canceled'] == 'Canceled']
canceled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
canceled_df_adr.reset_index(inplace = True)
canceled_df_adr.sort_values('reservation_status_date', inplace = True)

Not_Canceled_data = df[df['is_canceled'] == 'Not Canceled']
not_canceled_df_adr = not_canceled_data.groupby('reservation_status_date')[['adr']].mean()
not_canceled_df_adr.reset_index(inplace = True)
not_canceled_df_adr.sort_values('reservation_status_date', inplace = True)

plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot(not_canceled_df_adr ['reservation_status_date'], not_canceled_df_adr['adr'], label = 'Not Canceled')
plt.plot(canceled_df_adr ['reservation_status_date'], canceled_df_adr['adr'], label = 'canceled')
plt.legend()

